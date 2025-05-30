from bvbrc.client.client import Client
from bvbrc.RQL import Field


class PathwayClient(Client):
    """
    Data Type : pathway

    Primary Key : id
    """

    _version_ = Field("_version_")
    "number"

    accession = Field("accession")
    "case insensitive string"

    alt_locus_tag = Field("alt_locus_tag")
    "string"

    annotation = Field("annotation")
    "case insensitive string"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    ec_description = Field("ec_description")
    "case insensitive string"

    ec_number = Field("ec_number")
    "string"

    feature_id = Field("feature_id")
    "string"

    gene = Field("gene")
    "case insensitive string"

    genome_ec = Field("genome_ec")
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

    pathway_class = Field("pathway_class")
    "case insensitive string"

    pathway_ec = Field("pathway_ec")
    "string"

    pathway_id = Field("pathway_id")
    "string"

    pathway_name = Field("pathway_name")
    "case insensitive string"

    patric_id = Field("patric_id")
    "string"

    product = Field("product")
    "case insensitive string"

    public = Field("public")
    "boolean"

    refseq_locus_tag = Field("refseq_locus_tag")
    "string"

    sequence_id = Field("sequence_id")
    "string"

    taxon_id = Field("taxon_id")
    "integer"

    user_read = Field("user_read")
    "array of strings"

    user_write = Field("user_write")
    "array of strings"

    def __init__(self, api_key=None):
        super().__init__(datatype="pathway", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
