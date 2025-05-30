from bvbrc.client.client import Client
from bvbrc.RQL import Field


class FeatureSequenceClient(Client):
    """
    Data Type : feature_sequence

    Primary Key : md5
    """

    _version_ = Field("_version_")
    "number"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    md5 = Field("md5")
    """
    **primary key**

    string
    """

    sequence = Field("sequence")
    ""

    sequence_type = Field("sequence_type")
    "string"

    def __init__(self, api_key=None):
        super().__init__(datatype="feature_sequence", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
