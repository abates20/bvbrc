from bvbrc.client.client import Client
from bvbrc.RQL import Field


class PathwayRefClient(Client):
    """
    Data Type : pathway_ref

    Primary Key : id
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
    "string"

    id = Field("id")
    """
    **primary key**

    string
    """

    map_location = Field("map_location")
    "array of strings"

    map_name = Field("map_name")
    "string"

    map_type = Field("map_type")
    "string"

    occurrence = Field("occurrence")
    "integer"

    pathway_class = Field("pathway_class")
    "string"

    pathway_id = Field("pathway_id")
    "string"

    pathway_name = Field("pathway_name")
    "string"

    def __init__(self, api_key=None):
        super().__init__(datatype="pathway_ref", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
