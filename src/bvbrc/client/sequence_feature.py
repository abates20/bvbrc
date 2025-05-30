from bvbrc.client.client import Client
from bvbrc.RQL import Field


class SequenceFeatureClient(Client):
    """
    Data Type : sequence_feature

    Primary Key : id
    """

    aa_sequence_md5 = Field("aa_sequence_md5")
    "string"

    aa_variant = Field("aa_variant")
    "string"

    additional_metadata = Field("additional_metadata")
    "array of case insensitive strings"

    comments = Field("comments")
    "array of case insensitive strings"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    end = Field("end")
    "integer"

    evidence_code = Field("evidence_code")
    "string"

    feature_id = Field("feature_id")
    "string"

    genbank_accession = Field("genbank_accession")
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

    segment = Field("segment")
    "string"

    segments = Field("segments")
    "array of strings"

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

    source = Field("source")
    "string"

    source_aa_sequence = Field("source_aa_sequence")
    "string"

    source_id = Field("source_id")
    "string"

    source_sf_location = Field("source_sf_location")
    "string"

    source_strain = Field("source_strain")
    "string"

    start = Field("start")
    "integer"

    subtype = Field("subtype")
    "string"

    taxon_id = Field("taxon_id")
    "integer"

    variant_types = Field("variant_types")
    "string"

    def __init__(self, api_key=None):
        super().__init__(datatype="sequence_feature", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
