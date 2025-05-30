from bvbrc.client.client import Client
from bvbrc.RQL import Field


class GenomeFeatureClient(Client):
    """
    Data Type : genome_feature

    Primary Key : feature_id
    """

    aa_length = Field("aa_length")
    "integer"

    aa_sequence_md5 = Field("aa_sequence_md5")
    "string"

    accession = Field("accession")
    "string"

    alt_locus_tag = Field("alt_locus_tag")
    "string"

    annotation = Field("annotation")
    "string"

    brc_id = Field("brc_id")
    "string"

    classifier_round = Field("classifier_round")
    "integer"

    classifier_score = Field("classifier_score")
    "number"

    codon_start = Field("codon_start")
    "integer"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    end = Field("end")
    "integer"

    feature_id = Field("feature_id")
    """
    **primary key**

    string
    """

    feature_type = Field("feature_type")
    "string"

    figfam_id = Field("figfam_id")
    "string"

    gene = Field("gene")
    "case insensitive string"

    gene_id = Field("gene_id")
    "number"

    genome_id = Field("genome_id")
    "string"

    genome_name = Field("genome_name")
    "case insensitive string"

    go = Field("go")
    "array of case insensitive strings"

    location = Field("location")
    "string"

    na_length = Field("na_length")
    "integer"

    na_sequence_md5 = Field("na_sequence_md5")
    "string"

    notes = Field("notes")
    "array of strings"

    og_id = Field("og_id")
    "string"

    owner = Field("owner")
    "string"

    p2_feature_id = Field("p2_feature_id")
    "number"

    patric_id = Field("patric_id")
    "string"

    pdb_accession = Field("pdb_accession")
    "array of strings"

    pgfam_id = Field("pgfam_id")
    "string"

    plfam_id = Field("plfam_id")
    "string"

    product = Field("product")
    "case insensitive string"

    property = Field("property")
    "array of strings"

    protein_id = Field("protein_id")
    "string"

    public = Field("public")
    "boolean"

    refseq_locus_tag = Field("refseq_locus_tag")
    "string"

    segments = Field("segments")
    "array of strings"

    sequence_id = Field("sequence_id")
    "string"

    sog_id = Field("sog_id")
    "string"

    start = Field("start")
    "integer"

    strand = Field("strand")
    "string"

    taxon_id = Field("taxon_id")
    "integer"

    uniprotkb_accession = Field("uniprotkb_accession")
    "string"

    user_read = Field("user_read")
    "array of strings"

    user_write = Field("user_write")
    "array of strings"

    def __init__(self, api_key=None):
        super().__init__(datatype="genome_feature", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
