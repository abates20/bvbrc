from bvbrc.client.client import Client
from bvbrc.RQL import Field


class SpikeVariantClient(Client):
    """
    Data Type : spike_variant

    Primary Key : id
    """

    _version_ = Field("_version_")
    "number"

    aa_variant = Field("aa_variant")
    "string"

    country = Field("country")
    "case insensitive string"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    growth_rate = Field("growth_rate")
    "number"

    id = Field("id")
    """
    **primary key**

    string
    """

    lineage_count = Field("lineage_count")
    "integer"

    month = Field("month")
    "string"

    prevalence = Field("prevalence")
    "number"

    region = Field("region")
    "case insensitive string"

    sequence_features = Field("sequence_features")
    "array of strings"

    total_isolates = Field("total_isolates")
    "integer"

    def __init__(self, api_key=None):
        super().__init__(datatype="spike_variant", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
