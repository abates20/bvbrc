from bvbrc.client.client import Client
from bvbrc.RQL import Field


class SubsystemRefClient(Client):
    """
    Data Type : subsystem_ref

    Primary Key : id
    """

    _version_ = Field("_version_")
    "number"

    class_ = Field("class")
    "string"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    description = Field("description")
    "string"

    id = Field("id")
    """
    **primary key**

    string
    """

    notes = Field("notes")
    "array of strings"

    pmid = Field("pmid")
    "array of strings"

    role_id = Field("role_id")
    "array of strings"

    role_name = Field("role_name")
    "array of strings"

    subclass = Field("subclass")
    "string"

    subsystem_id = Field("subsystem_id")
    "string"

    subsystem_name = Field("subsystem_name")
    "string"

    superclass = Field("superclass")
    "string"

    def __init__(self, api_key=None):
        super().__init__(datatype="subsystem_ref", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
