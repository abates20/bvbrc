from bvbrc.client.client import Client
from bvbrc.RQL import Field


class SpGeneRefClient(Client):
    """
    Data Type : sp_gene_ref

    Primary Key : id
    """

    _version_ = Field("_version_")
    "number"

    antibiotics = Field("antibiotics")
    "array of strings"

    antibiotics_class = Field("antibiotics_class")
    "string"

    assertion = Field("assertion")
    "string"

    classification = Field("classification")
    "array of strings"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    function = Field("function")
    "string"

    gene_id = Field("gene_id")
    "string"

    gene_name = Field("gene_name")
    "string"

    genus = Field("genus")
    "string"

    gi = Field("gi")
    "string"

    id = Field("id")
    """
    **primary key**

    string
    """

    locus_tag = Field("locus_tag")
    "string"

    organism = Field("organism")
    "string"

    pmid = Field("pmid")
    "array of strings"

    product = Field("product")
    "string"

    property = Field("property")
    "string"

    source = Field("source")
    "string"

    source_id = Field("source_id")
    "string"

    species = Field("species")
    "string"

    def __init__(self, api_key=None):
        super().__init__(datatype="sp_gene_ref", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
