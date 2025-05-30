from bvbrc.client.client import Client
from bvbrc.RQL import Field


class StrainClient(Client):
    """
    Data Type : strain

    Primary Key : id
    """

    _1_pb2 = Field("1_pb2")
    "array of strings"

    _2_pb1 = Field("2_pb1")
    "array of strings"

    _3_pa = Field("3_pa")
    "array of strings"

    _4_ha = Field("4_ha")
    "array of strings"

    _5_np = Field("5_np")
    "array of strings"

    _6_na = Field("6_na")
    "array of strings"

    _7_mp = Field("7_mp")
    "array of strings"

    _8_ns = Field("8_ns")
    "array of strings"

    _version_ = Field("_version_")
    "number"

    collection_date = Field("collection_date")
    "string"

    collection_year = Field("collection_year")
    "integer"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    family = Field("family")
    "case insensitive string"

    genbank_accessions = Field("genbank_accessions")
    "array of strings"

    genome_ids = Field("genome_ids")
    "array of strings"

    genus = Field("genus")
    "case insensitive string"

    geographic_group = Field("geographic_group")
    "case insensitive string"

    h_type = Field("h_type")
    "integer"

    host_common_name = Field("host_common_name")
    "case insensitive string"

    host_group = Field("host_group")
    "case insensitive string"

    host_name = Field("host_name")
    "case insensitive string"

    id = Field("id")
    """
    **primary key**

    string
    """

    isolation_country = Field("isolation_country")
    "case insensitive string"

    l = Field("l")  # noqa: E741
    "array of strings"

    lab_host = Field("lab_host")
    "case insensitive string"

    m = Field("m")
    "array of strings"

    n_type = Field("n_type")
    "integer"

    other_segments = Field("other_segments")
    "array of strings"

    owner = Field("owner")
    "string"

    passage = Field("passage")
    "case insensitive string"

    public = Field("public")
    "boolean"

    s = Field("s")
    "array of strings"

    season = Field("season")
    "string"

    segment_count = Field("segment_count")
    "integer"

    species = Field("species")
    "case insensitive string"

    status = Field("status")
    "string"

    strain = Field("strain")
    "case insensitive string"

    subtype = Field("subtype")
    "string"

    taxon_id = Field("taxon_id")
    "integer"

    taxon_lineage_ids = Field("taxon_lineage_ids")
    "array of strings"

    taxon_lineage_names = Field("taxon_lineage_names")
    "array of strings"

    user_read = Field("user_read")
    "array of strings"

    user_write = Field("user_write")
    "array of strings"

    def __init__(self, api_key=None):
        super().__init__(datatype="strain", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
