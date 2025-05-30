from bvbrc.client.client import Client
from bvbrc.RQL import Field


class BiosetResultClient(Client):
    """
    Data Type : bioset_result

    Primary Key : id
    """

    _version_ = Field("_version_")
    "number"

    bioset_description = Field("bioset_description")
    "case insensitive string"

    bioset_id = Field("bioset_id")
    "string"

    bioset_name = Field("bioset_name")
    "case insensitive string"

    bioset_type = Field("bioset_type")
    "case insensitive string"

    counts = Field("counts")
    "number"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    entity_id = Field("entity_id")
    "string"

    entity_name = Field("entity_name")
    "string"

    entity_type = Field("entity_type")
    "case insensitive string"

    exp_id = Field("exp_id")
    "string"

    exp_name = Field("exp_name")
    "case insensitive string"

    exp_title = Field("exp_title")
    "case insensitive string"

    exp_type = Field("exp_type")
    "case insensitive string"

    feature_id = Field("feature_id")
    "string"

    fpkm = Field("fpkm")
    "number"

    gene = Field("gene")
    "case insensitive string"

    gene_id = Field("gene_id")
    "string"

    genome_id = Field("genome_id")
    "array of strings"

    id = Field("id")
    """
    **primary key**

    string
    """

    locus_tag = Field("locus_tag")
    "string"

    log2_fc = Field("log2_fc")
    "number"

    organism = Field("organism")
    "case insensitive string"

    other_ids = Field("other_ids")
    "array of strings"

    other_value = Field("other_value")
    "number"

    p_value = Field("p_value")
    "number"

    patric_id = Field("patric_id")
    "string"

    product = Field("product")
    "case insensitive string"

    protein_id = Field("protein_id")
    "string"

    result_type = Field("result_type")
    "case insensitive string"

    strain = Field("strain")
    "case insensitive string"

    taxon_id = Field("taxon_id")
    "integer"

    tpm = Field("tpm")
    "number"

    treatment_amount = Field("treatment_amount")
    "case insensitive string"

    treatment_duration = Field("treatment_duration")
    "case insensitive string"

    treatment_name = Field("treatment_name")
    "case insensitive string"

    treatment_type = Field("treatment_type")
    "case insensitive string"

    uniprot_id = Field("uniprot_id")
    "string"

    z_score = Field("z_score")
    "number"

    def __init__(self, api_key=None):
        super().__init__(datatype="bioset_result", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
