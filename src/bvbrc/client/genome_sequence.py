from bvbrc.client.client import Client
from bvbrc.RQL import Field


class GenomeSequenceClient(Client):
    """
    Data Type : genome_sequence

    Primary Key : sequence_id
    """

    _version_ = Field("_version_")
    "number"

    accession = Field("accession")
    "string"

    chromosome = Field("chromosome")
    "case insensitive string"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    description = Field("description")
    "case insensitive string"

    gc_content = Field("gc_content")
    "number"

    genome_id = Field("genome_id")
    "string"

    genome_name = Field("genome_name")
    "case insensitive string"

    gi = Field("gi")
    "integer"

    length = Field("length")
    "integer"

    mol_type = Field("mol_type")
    "case insensitive string"

    owner = Field("owner")
    "string"

    p2_sequence_id = Field("p2_sequence_id")
    "integer"

    plasmid = Field("plasmid")
    "case insensitive string"

    public = Field("public")
    "boolean"

    release_date = Field("release_date")
    "date"

    segment = Field("segment")
    "case insensitive string"

    sequence = Field("sequence")
    ""

    sequence_id = Field("sequence_id")
    """
    **primary key**

    string
    """

    sequence_md5 = Field("sequence_md5")
    "string"

    sequence_status = Field("sequence_status")
    "string"

    sequence_type = Field("sequence_type")
    "case insensitive string"

    taxon_id = Field("taxon_id")
    "integer"

    topology = Field("topology")
    "case insensitive string"

    user_read = Field("user_read")
    "array of strings"

    user_write = Field("user_write")
    "array of strings"

    version = Field("version")
    "integer"

    def __init__(self, api_key=None):
        super().__init__(datatype="genome_sequence", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
