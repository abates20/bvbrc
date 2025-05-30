from pathlib import Path
import re


CLASS_DEF_PATTERN = re.compile(r"class (\w+Client)\(Client\):")

PROJ_PATH = Path()
CLIENT_SRC_DIR = PROJ_PATH.joinpath("src", "bvbrc", "client")
CLIENT_DOC_DIR = PROJ_PATH.joinpath("docs", "api_reference", "clients")

DOC_TEMPLATE = """
bvbrc.{client}
{headerlines}

.. autoclass:: bvbrc.{client}
    :members:
    :inherited-members:
    :member-order: groupwise
""".lstrip()


def make_doc(client_name):
    global DOC_TEMPLATE
    len_header = len("bvbrc.") + len(client_name)
    headerlines = "=" * len_header
    return DOC_TEMPLATE.format(client=client_name, headerlines=headerlines)


for client_file in CLIENT_SRC_DIR.glob("*.py"):
    if client_file.name in ["__init__.py", "client.py"]:
        continue

    # Read in the source code for the client
    with client_file.open("r") as f:
        client_src = f.read()

    # Extract the name of the client class
    client_name = CLASS_DEF_PATTERN.findall(client_src)[0]

    # Create the doc file
    doc_file = CLIENT_DOC_DIR.joinpath(client_file.with_suffix(".rst").name)
    with doc_file.open("w") as f:
        f.write(make_doc(client_name))
