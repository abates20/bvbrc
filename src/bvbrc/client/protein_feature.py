from bvbrc.client.client import Client
from bvbrc.RQL import Field


class ProteinFeatureClient(Client):
    """
    Data Type : protein_feature

    Primary Key : id
    """

    aa_sequence_md5 = Field("aa_sequence_md5")
    "string"

    classification = Field("classification")
    "array of strings"

    comments = Field("comments")
    "array of case insensitive strings"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    description = Field("description")
    "case insensitive string"

    e_value = Field("e_value")
    "string"

    end = Field("end")
    "integer"

    evidence = Field("evidence")
    "string"

    feature_id = Field("feature_id")
    "string"

    feature_type = Field("feature_type")
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

    interpro_description = Field("interpro_description")
    "case insensitive string"

    interpro_id = Field("interpro_id")
    "string"

    length = Field("length")
    "integer"

    patric_id = Field("patric_id")
    "string"

    product = Field("product")
    "case insensitive string"

    publication = Field("publication")
    "array of strings"

    refseq_locus_tag = Field("refseq_locus_tag")
    "string"

    score = Field("score")
    "number"

    segments = Field("segments")
    "array of strings"

    sequence = Field("sequence")
    "string"

    source = Field("source")
    "string"

    source_id = Field("source_id")
    "string"

    start = Field("start")
    "integer"

    taxon_id = Field("taxon_id")
    "integer"

    def __init__(self, api_key=None):
        super().__init__(datatype="protein_feature", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
