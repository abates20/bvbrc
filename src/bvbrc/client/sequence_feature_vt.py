from bvbrc.client.client import Client
from bvbrc.RQL import Field


class SequenceFeatureVtClient(Client):
    """
    Data Type : sequence_feature_vt

    Primary Key : id
    """

    additional_metadata = Field("additional_metadata")
    "array of case insensitive strings"

    comments = Field("comments")
    "array of case insensitive strings"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    id = Field("id")
    """
    **primary key**

    string
    """

    sf_category = Field("sf_category")
    "string"

    sf_id = Field("sf_id")
    "string"

    sf_name = Field("sf_name")
    "case insensitive string"

    sf_sequence = Field("sf_sequence")
    "string"

    sf_sequence_md5 = Field("sf_sequence_md5")
    "string"

    sfvt_genome_count = Field("sfvt_genome_count")
    "string"

    sfvt_genome_ids = Field("sfvt_genome_ids")
    "array of strings"

    sfvt_id = Field("sfvt_id")
    "string"

    sfvt_sequence = Field("sfvt_sequence")
    "string"

    sfvt_sequence_md5 = Field("sfvt_sequence_md5")
    "string"

    sfvt_variations = Field("sfvt_variations")
    "string"

    def __init__(self, api_key=None):
        super().__init__(datatype="sequence_feature_vt", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
