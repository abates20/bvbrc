from bvbrc.client.client import Client
from bvbrc.RQL import Field


class ProteinFamilyRefClient(Client):
    """
    Data Type : protein_family_ref

    Primary Key : family_id
    """

    _version_ = Field("_version_")
    "number"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    family_id = Field("family_id")
    """
    **primary key**

    string
    """

    family_product = Field("family_product")
    "string"

    family_type = Field("family_type")
    "string"

    def __init__(self, api_key=None):
        super().__init__(datatype="protein_family_ref", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
