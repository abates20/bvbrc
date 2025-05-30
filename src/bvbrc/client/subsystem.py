from bvbrc.client.client import Client
from bvbrc.RQL import Field


class SubsystemClient(Client):
    """
    Data Type : subsystem

    Primary Key : id
    """

    _version_ = Field("_version_")
    "number"

    active = Field("active")
    "string"

    class_ = Field("class")
    "string"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    feature_id = Field("feature_id")
    "string"

    gene = Field("gene")
    "string"

    genome_id = Field("genome_id")
    "string"

    genome_name = Field("genome_name")
    "case insensitive string"

    id = Field("id")
    """
    **primary key**

    string
    """

    owner = Field("owner")
    "string"

    patric_id = Field("patric_id")
    "string"

    product = Field("product")
    "string"

    public = Field("public")
    "boolean"

    refseq_locus_tag = Field("refseq_locus_tag")
    "string"

    role_id = Field("role_id")
    "string"

    role_name = Field("role_name")
    "string"

    subclass = Field("subclass")
    "string"

    subsystem_id = Field("subsystem_id")
    "string"

    subsystem_name = Field("subsystem_name")
    "string"

    superclass = Field("superclass")
    "string"

    taxon_id = Field("taxon_id")
    "integer"

    user_read = Field("user_read")
    "array of strings"

    user_write = Field("user_write")
    "array of strings"

    def __init__(self, api_key=None):
        super().__init__(datatype="subsystem", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
