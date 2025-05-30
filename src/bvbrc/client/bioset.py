from bvbrc.client.client import Client
from bvbrc.RQL import Field


class BiosetClient(Client):
    """
    Data Type : bioset

    Primary Key : bioset_id
    """

    _version_ = Field("_version_")
    "number"

    additional_data = Field("additional_data")
    "array of strings"

    additional_metadata = Field("additional_metadata")
    "array of case insensitive strings"

    analysis_group_1 = Field("analysis_group_1")
    "case insensitive string"

    analysis_group_2 = Field("analysis_group_2")
    "case insensitive string"

    analysis_method = Field("analysis_method")
    "case insensitive string"

    bioset_criteria = Field("bioset_criteria")
    "case insensitive string"

    bioset_description = Field("bioset_description")
    "case insensitive string"

    bioset_id = Field("bioset_id")
    """
    **primary key**

    string
    """

    bioset_name = Field("bioset_name")
    "case insensitive string"

    bioset_result = Field("bioset_result")
    "array of strings"

    bioset_type = Field("bioset_type")
    "case insensitive string"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    entity_count = Field("entity_count")
    "case insensitive string"

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

    genome_id = Field("genome_id")
    "array of strings"

    organism = Field("organism")
    "case insensitive string"

    protocol = Field("protocol")
    "array of strings"

    result_type = Field("result_type")
    "case insensitive string"

    strain = Field("strain")
    "case insensitive string"

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
    "integer"

    taxon_lineage_ids = Field("taxon_lineage_ids")
    "array of strings"

    treatment_amount = Field("treatment_amount")
    "case insensitive string"

    treatment_duration = Field("treatment_duration")
    "case insensitive string"

    treatment_name = Field("treatment_name")
    "case insensitive string"

    treatment_type = Field("treatment_type")
    "case insensitive string"

    def __init__(self, api_key=None):
        super().__init__(datatype="bioset", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
