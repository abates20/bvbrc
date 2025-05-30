from bvbrc.client.client import Client
from bvbrc.RQL import Field


class PPIClient(Client):
    """
    Data Type : ppi

    Primary Key : id
    """

    _version_ = Field("_version_")
    "number"

    category = Field("category")
    "string"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    detection_method = Field("detection_method")
    "array of case insensitive strings"

    domain_a = Field("domain_a")
    "string"

    domain_b = Field("domain_b")
    "string"

    evidence = Field("evidence")
    "array of strings"

    feature_id_a = Field("feature_id_a")
    "string"

    feature_id_b = Field("feature_id_b")
    "string"

    gene_a = Field("gene_a")
    "string"

    gene_b = Field("gene_b")
    "string"

    genome_id_a = Field("genome_id_a")
    "string"

    genome_id_b = Field("genome_id_b")
    "string"

    genome_name_a = Field("genome_name_a")
    "case insensitive string"

    genome_name_b = Field("genome_name_b")
    "case insensitive string"

    id = Field("id")
    """
    **primary key**

    string
    """

    interaction_type = Field("interaction_type")
    "array of case insensitive strings"

    interactor_a = Field("interactor_a")
    "string"

    interactor_b = Field("interactor_b")
    "string"

    interactor_desc_a = Field("interactor_desc_a")
    "case insensitive string"

    interactor_desc_b = Field("interactor_desc_b")
    "case insensitive string"

    interactor_type_a = Field("interactor_type_a")
    "string"

    interactor_type_b = Field("interactor_type_b")
    "string"

    pmid = Field("pmid")
    "array of strings"

    refseq_locus_tag_a = Field("refseq_locus_tag_a")
    "string"

    refseq_locus_tag_b = Field("refseq_locus_tag_b")
    "string"

    score = Field("score")
    "array of strings"

    source_db = Field("source_db")
    "array of strings"

    source_id = Field("source_id")
    "array of strings"

    taxon_id_a = Field("taxon_id_a")
    "integer"

    taxon_id_b = Field("taxon_id_b")
    "integer"

    def __init__(self, api_key=None):
        super().__init__(datatype="ppi", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
