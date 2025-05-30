from bvbrc.client.client import Client
from bvbrc.RQL import Field


class EnzymeClassRefClient(Client):
    """
    Data Type : enzyme_class_ref

    Primary Key : ec_number
    """

    _version_ = Field("_version_")
    "number"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    ec_description = Field("ec_description")
    "string"

    ec_number = Field("ec_number")
    """
    **primary key**

    string
    """

    go = Field("go")
    "array of case insensitive strings"

    def __init__(self, api_key=None):
        super().__init__(datatype="enzyme_class_ref", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
