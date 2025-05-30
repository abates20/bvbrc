from bvbrc.client.client import Client
from bvbrc.RQL import Field


class SpGeneClient(Client):
    """
    Data Type : sp_gene

    Primary Key : id
    """

    _version_ = Field("_version_")
    "number"

    alt_locus_tag = Field("alt_locus_tag")
    "string"

    antibiotics = Field("antibiotics")
    "array of strings"

    antibiotics_class = Field("antibiotics_class")
    "string"

    classification = Field("classification")
    "array of strings"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    e_value = Field("e_value")
    "string"

    evidence = Field("evidence")
    "string"

    feature_id = Field("feature_id")
    "string"

    function = Field("function")
    "string"

    gene = Field("gene")
    "string"

    genome_id = Field("genome_id")
    "string"

    genome_name = Field("genome_name")
    "string"

    id = Field("id")
    """
    **primary key**

    string
    """

    identity = Field("identity")
    "integer"

    organism = Field("organism")
    "string"

    owner = Field("owner")
    "string"

    patric_id = Field("patric_id")
    "string"

    pmid = Field("pmid")
    "array of strings"

    product = Field("product")
    "string"

    property = Field("property")
    "string"

    property_source = Field("property_source")
    "string"

    public = Field("public")
    "boolean"

    query_coverage = Field("query_coverage")
    "integer"

    refseq_locus_tag = Field("refseq_locus_tag")
    "string"

    same_genome = Field("same_genome")
    "integer"

    same_genus = Field("same_genus")
    "integer"

    same_species = Field("same_species")
    "integer"

    source = Field("source")
    "string"

    source_id = Field("source_id")
    "string"

    subject_coverage = Field("subject_coverage")
    "integer"

    taxon_id = Field("taxon_id")
    "integer"

    user_read = Field("user_read")
    "array of strings"

    user_write = Field("user_write")
    "array of strings"

    def __init__(self, api_key=None):
        super().__init__(datatype="sp_gene", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
