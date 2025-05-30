from bvbrc.client.client import Client
from bvbrc.RQL import Field


class MiscNiaidSgcClient(Client):
    """
    Data Type : misc_niaid_sgc

    Primary Key : target_id
    """

    _version_ = Field("_version_")
    "number"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    gene_symbol_collection = Field("gene_symbol_collection")
    "array of strings"

    genus = Field("genus")
    "string"

    has_clones = Field("has_clones")
    "string"

    has_proteins = Field("has_proteins")
    "string"

    selection_criteria = Field("selection_criteria")
    "string"

    species = Field("species")
    "string"

    strain = Field("strain")
    "string"

    target_id = Field("target_id")
    """
    **primary key**

    string
    """

    target_status = Field("target_status")
    "string"

    def __init__(self, api_key=None):
        super().__init__(datatype="misc_niaid_sgc", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
