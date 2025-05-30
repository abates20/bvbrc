from bvbrc.client.client import Client
from bvbrc.RQL import Field


class IdRefClient(Client):
    """
    Data Type : id_ref

    Primary Key : id
    """

    _version_ = Field("_version_")
    "number"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    id = Field("id")
    """
    **primary key**

    string
    """

    id_type = Field("id_type")
    "string"

    id_value = Field("id_value")
    "string"

    uniprotkb_accession = Field("uniprotkb_accession")
    "string"

    def __init__(self, api_key=None):
        super().__init__(datatype="id_ref", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
