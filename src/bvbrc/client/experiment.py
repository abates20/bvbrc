from bvbrc.client.client import Client
from bvbrc.RQL import Field


class ExperimentClient(Client):
    """
    Data Type : experiment

    Primary Key : exp_id
    """

    _version_ = Field("_version_")
    "number"

    additional_data = Field("additional_data")
    "array of strings"

    additional_metadata = Field("additional_metadata")
    "array of case insensitive strings"

    biosets = Field("biosets")
    "integer"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    detection_instrument = Field("detection_instrument")
    "case insensitive string"

    doi = Field("doi")
    "string"

    exp_description = Field("exp_description")
    "case insensitive string"

    exp_id = Field("exp_id")
    """
    **primary key**

    string
    """

    exp_name = Field("exp_name")
    "case insensitive string"

    exp_poc = Field("exp_poc")
    "case insensitive string"

    exp_protocol = Field("exp_protocol")
    "array of case insensitive strings"

    exp_title = Field("exp_title")
    "case insensitive string"

    exp_type = Field("exp_type")
    "case insensitive string"

    experimenters = Field("experimenters")
    "case insensitive string"

    genome_id = Field("genome_id")
    "array of strings"

    measurement_technique = Field("measurement_technique")
    "case insensitive string"

    organism = Field("organism")
    "array of case insensitive strings"

    pmid = Field("pmid")
    "string"

    public_identifier = Field("public_identifier")
    "string"

    public_repository = Field("public_repository")
    "string"

    samples = Field("samples")
    "integer"

    strain = Field("strain")
    "array of case insensitive strings"

    study_description = Field("study_description")
    "case insensitive string"

    study_institution = Field("study_institution")
    "case insensitive string"

    study_name = Field("study_name")
    "case insensitive string"

    study_pi = Field("study_pi")
    "case insensitive string"

    study_title = Field("study_title")
    "case insensitive string"

    taxon_id = Field("taxon_id")
    "array of integers"

    taxon_lineage_ids = Field("taxon_lineage_ids")
    "array of strings"

    treatment_amount = Field("treatment_amount")
    "array of case insensitive strings"

    treatment_duration = Field("treatment_duration")
    "array of case insensitive strings"

    treatment_name = Field("treatment_name")
    "array of case insensitive strings"

    treatment_type = Field("treatment_type")
    "array of case insensitive strings"

    def __init__(self, api_key=None):
        super().__init__(datatype="experiment", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
