import re
from pathlib import Path

import bvbrc as bv
import requests
from bs4 import BeautifulSoup


def get_data_types(doc_url: str) -> list[tuple[str, str]]:
    """
    Gets all the data types in the BV-BRC Data API with the link
    to their respective documentation pages.
    """

    res = requests.get(doc_url)
    soup = BeautifulSoup(res.text, "html.parser")
    body = soup.body

    data_types = []
    data_type_header = body.find("h2", string="Data Types")
    data_type_list = data_type_header.find_next_sibling("ul")
    for ele in data_type_list.find_all("a"):
        text = ele.get_text(strip=True)
        ref = doc_url + "/" + ele.get("href")
        data_types.append((text, ref))
    return data_types


def clean_text(string: str):
    """
    Cleans up a string taken from scraping the BV-BRC docs by removing
    parantheses, stripping whitespace from the ends, and collapsing internal
    whitespace into single spaces.
    """
    string = string.replace("(", "").replace(")", "")
    white_space_pattern = re.compile("\s+")
    return white_space_pattern.sub(" ", string).strip()


def to_camel_case(string: str):
    """
    Convert a string in snake_case to CamelCase.
    """
    pieces = []
    for piece in string.split("_"):
        if piece == "ppi":
            pieces.append("PPI")  # Convert ppi to PPI instead of Ppi
        else:
            pieces.append(piece[0].upper() + piece[1:])
    return "".join(pieces)


def scrape_doc(
    datatype: str,
    endpoint_doc_url: str,
    cls_template: str,
    attr_template: str,
    pk_attr_template: str,
) -> str:
    """
    Scrapes the doc page for a datatype in the BV-BRC Data API to build
    python code for a class with each of the fields for that datatype.
    Returns a string containing the python code.
    """
    res = requests.get(endpoint_doc_url)
    soup = BeautifulSoup(res.text, "html.parser")

    attrs = []
    primary_key = ""
    header = soup.body.find("h3", string="Attributes")
    attr_list = header.find_next_sibling("ul")
    for ele in attr_list.find_all("li"):
        attr_name, attr_type, _ = [
            clean_text(child.get_text()) for child in ele.children
        ]

        # Handle primary keys attributes
        if attr_name.endswith("*"):
            attr_name = attr_name.removesuffix("*").rstrip()
            primary_key = attr_name
            template = pk_attr_template
        else:
            template = attr_template

        # Fix some attribute names that don't work as variable names in python
        if attr_name == "class":
            attr_name_py = attr_name + "_"
        elif attr_name[0].isnumeric():
            attr_name_py = "_" + attr_name
        else:
            attr_name_py = attr_name

        # Add the formatted attribute to the list of attributes
        attrs.append(
            template.format(
                attr_name_py=attr_name_py, attr_name=attr_name, attr_type=attr_type
            )
        )

    cls_def = cls_template.format(
        cls_name=to_camel_case(datatype) + "Client",
        datatype=datatype,
        primary_key=primary_key,
        attributes="".join(attrs).strip(),
    )
    return cls_def


# Template strings to make constructing the class for each datatype simple
CLS_TEMPLATE = """
class {cls_name}(Client):
    \"\"\"
    Data Type : {datatype}
    
    Primary Key : {primary_key}
    \"\"\"
    
    {attributes}

    def __init__(self, api_key = None):
        super().__init__(datatype="{datatype}", api_key=api_key)

    def __repr__(self) -> str:
        return f"{{self.__class__.__name__}}()"
"""

ATTR_TEMPLATE = """
    {attr_name_py} = Field("{attr_name}")
    "{attr_type}"
"""

PK_ATTR_TEMPLATE = """
    {attr_name_py} = Field("{attr_name}")
    \"""
    **primary key**

    {attr_type}
    \"""
"""

MODULE_TEMPLATE = """
from bvbrc.client.client import Client
from bvbrc.RQL import Field

{cls}
""".strip()


# Build a module file for each datatype
for datatype, url in get_data_types(bv.DOC_URL):
    cls_str = scrape_doc(datatype, url, CLS_TEMPLATE, ATTR_TEMPLATE, PK_ATTR_TEMPLATE)
    module = MODULE_TEMPLATE.format(cls=cls_str)

    module_path = Path().joinpath("src", "bvbrc", "client", f"{datatype}.py")
    with module_path.open("w") as file:
        file.write(module)
