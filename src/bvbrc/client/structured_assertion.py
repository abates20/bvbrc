from bvbrc.client.client import Client
from bvbrc.RQL import Field


class StructuredAssertionClient(Client):
    """
    Data Type : structured_assertion

    Primary Key : id
    """

    _version_ = Field("_version_")
    "number"

    comment = Field("comment")
    "string"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    evidence_code = Field("evidence_code")
    "string"

    feature_id = Field("feature_id")
    "string"

    id = Field("id")
    """
    **primary key**

    string
    """

    owner = Field("owner")
    "string"

    patric_id = Field("patric_id")
    "string"

    pmid = Field("pmid")
    "string"

    property = Field("property")
    "string"

    public = Field("public")
    "boolean"

    refseq_locus_tag = Field("refseq_locus_tag")
    "string"

    score = Field("score")
    "string"

    source = Field("source")
    "string"

    user_read = Field("user_read")
    "array of strings"

    user_write = Field("user_write")
    "array of strings"

    value = Field("value")
    "string"

    def __init__(self, api_key=None):
        super().__init__(datatype="structured_assertion", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
