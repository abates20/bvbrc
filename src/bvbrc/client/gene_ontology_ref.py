from bvbrc.client.client import Client
from bvbrc.RQL import Field


class GeneOntologyRefClient(Client):
    """
    Data Type : gene_ontology_ref

    Primary Key : go_id
    """

    _version_ = Field("_version_")
    "number"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    definition = Field("definition")
    "string"

    go_id = Field("go_id")
    """
    **primary key**

    string
    """

    go_name = Field("go_name")
    "string"

    ontology = Field("ontology")
    "string"

    def __init__(self, api_key=None):
        super().__init__(datatype="gene_ontology_ref", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
