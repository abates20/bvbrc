from bvbrc.client.client import Client
from bvbrc.RQL import Field


class SurveillanceClient(Client):
    """
    Data Type : surveillance

    Primary Key : id
    """

    additional_metadata = Field("additional_metadata")
    "array of case insensitive strings"

    alcohol_or_other_drug_dependence = Field("alcohol_or_other_drug_dependence")
    "case insensitive string"

    breastfeeding = Field("breastfeeding")
    "case insensitive string"

    chest_imaging_interpretation = Field("chest_imaging_interpretation")
    "case insensitive string"

    chronic_conditions = Field("chronic_conditions")
    "array of case insensitive strings"

    collection_city = Field("collection_city")
    "case insensitive string"

    collection_country = Field("collection_country")
    "case insensitive string"

    collection_date = Field("collection_date")
    "date"

    collection_latitude = Field("collection_latitude")
    "number"

    collection_longitude = Field("collection_longitude")
    "number"

    collection_poi = Field("collection_poi")
    "case insensitive string"

    collection_season = Field("collection_season")
    "case insensitive string"

    collection_state_province = Field("collection_state_province")
    "case insensitive string"

    collection_year = Field("collection_year")
    "case insensitive string"

    collector_institution = Field("collector_institution")
    "case insensitive string"

    collector_name = Field("collector_name")
    "array of case insensitive strings"

    comments = Field("comments")
    "array of case insensitive strings"

    contact_email_address = Field("contact_email_address")
    "case insensitive string"

    contributing_institution = Field("contributing_institution")
    "case insensitive string"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    daycare_attendance = Field("daycare_attendance")
    "case insensitive string"

    days_elapsed_to_disease_status = Field("days_elapsed_to_disease_status")
    "case insensitive string"

    days_elapsed_to_sample_collection = Field("days_elapsed_to_sample_collection")
    "case insensitive string"

    days_elapsed_to_vaccination = Field("days_elapsed_to_vaccination")
    "array of case insensitive strings"

    diagnosis = Field("diagnosis")
    "array of case insensitive strings"

    dialysis = Field("dialysis")
    "case insensitive string"

    disease_severity = Field("disease_severity")
    "case insensitive string"

    disease_status = Field("disease_status")
    "case insensitive string"

    duration_of_exposure = Field("duration_of_exposure")
    "array of case insensitive strings"

    duration_of_treatment = Field("duration_of_treatment")
    "array of case insensitive strings"

    ecmo = Field("ecmo")
    "case insensitive string"

    education = Field("education")
    "case insensitive string"

    embargo_end_date = Field("embargo_end_date")
    "date"

    exposure = Field("exposure")
    "array of case insensitive strings"

    exposure_type = Field("exposure_type")
    "array of case insensitive strings"

    genome_id = Field("genome_id")
    "array of strings"

    geographic_group = Field("geographic_group")
    "case insensitive string"

    hospitalization_duration = Field("hospitalization_duration")
    "case insensitive string"

    hospitalized = Field("hospitalized")
    "case insensitive string"

    host_age = Field("host_age")
    "case insensitive string"

    host_capture_status = Field("host_capture_status")
    "case insensitive string"

    host_common_name = Field("host_common_name")
    "case insensitive string"

    host_ethnicity = Field("host_ethnicity")
    "array of case insensitive strings"

    host_group = Field("host_group")
    "case insensitive string"

    host_habitat = Field("host_habitat")
    "case insensitive string"

    host_health = Field("host_health")
    "case insensitive string"

    host_height = Field("host_height")
    "case insensitive string"

    host_id_type = Field("host_id_type")
    "case insensitive string"

    host_identifier = Field("host_identifier")
    "string"

    host_natural_state = Field("host_natural_state")
    "case insensitive string"

    host_race = Field("host_race")
    "array of case insensitive strings"

    host_sex = Field("host_sex")
    "case insensitive string"

    host_species = Field("host_species")
    "case insensitive string"

    host_weight = Field("host_weight")
    "case insensitive string"

    human_leukocyte_antigens = Field("human_leukocyte_antigens")
    "case insensitive string"

    id = Field("id")
    """
    **primary key**

    string
    """

    infections_within_five_years = Field("infections_within_five_years")
    "array of case insensitive strings"

    influenza_like_illness_over_the_past_year = Field(
        "influenza_like_illness_over_the_past_year"
    )
    "case insensitive string"

    initiation_of_treatment = Field("initiation_of_treatment")
    "array of case insensitive strings"

    intensive_care_unit = Field("intensive_care_unit")
    "case insensitive string"

    last_update_date = Field("last_update_date")
    "date"

    longitudinal_study = Field("longitudinal_study")
    "case insensitive string"

    maintenance_medication = Field("maintenance_medication")
    "array of case insensitive strings"

    nursing_home_residence = Field("nursing_home_residence")
    "case insensitive string"

    onset_hours = Field("onset_hours")
    "case insensitive string"

    other_vaccinations = Field("other_vaccinations")
    "case insensitive string"

    oxygen_saturation = Field("oxygen_saturation")
    "case insensitive string"

    packs_per_day_for_how_many_years = Field("packs_per_day_for_how_many_years")
    "case insensitive string"

    pathogen_test_interpretation = Field("pathogen_test_interpretation")
    "array of case insensitive strings"

    pathogen_test_result = Field("pathogen_test_result")
    "array of case insensitive strings"

    pathogen_test_type = Field("pathogen_test_type")
    "array of case insensitive strings"

    pathogen_type = Field("pathogen_type")
    "case insensitive string"

    post_visit_medications = Field("post_visit_medications")
    "array of case insensitive strings"

    pre_visit_medications = Field("pre_visit_medications")
    "array of case insensitive strings"

    pregnancy = Field("pregnancy")
    "case insensitive string"

    primary_living_situation = Field("primary_living_situation")
    "case insensitive string"

    profession = Field("profession")
    "case insensitive string"

    project_identifier = Field("project_identifier")
    "string"

    sample_accession = Field("sample_accession")
    "string"

    sample_identifier = Field("sample_identifier")
    "string"

    sample_material = Field("sample_material")
    "case insensitive string"

    sample_receipt_date = Field("sample_receipt_date")
    "case insensitive string"

    sample_transport_medium = Field("sample_transport_medium")
    "case insensitive string"

    sequence_accession = Field("sequence_accession")
    "array of strings"

    source_of_vaccine_information = Field("source_of_vaccine_information")
    "array of case insensitive strings"

    species = Field("species")
    "case insensitive string"

    strain = Field("strain")
    "case insensitive string"

    submission_date = Field("submission_date")
    "date"

    subtype = Field("subtype")
    "case insensitive string"

    sudden_onset = Field("sudden_onset")
    "case insensitive string"

    symptoms = Field("symptoms")
    "array of case insensitive strings"

    taxon_lineage_ids = Field("taxon_lineage_ids")
    "array of strings"

    tobacco_use = Field("tobacco_use")
    "case insensitive string"

    travel_history = Field("travel_history")
    "array of case insensitive strings"

    treatment = Field("treatment")
    "array of case insensitive strings"

    treatment_dosage = Field("treatment_dosage")
    "array of case insensitive strings"

    treatment_type = Field("treatment_type")
    "array of case insensitive strings"

    trimester_of_pregnancy = Field("trimester_of_pregnancy")
    "case insensitive string"

    types_of_allergies = Field("types_of_allergies")
    "array of case insensitive strings"

    use_of_personal_protective_equipment = Field("use_of_personal_protective_equipment")
    "array of case insensitive strings"

    vaccination_type = Field("vaccination_type")
    "case insensitive string"

    vaccine_dosage = Field("vaccine_dosage")
    "array of case insensitive strings"

    vaccine_lot_number = Field("vaccine_lot_number")
    "array of case insensitive strings"

    vaccine_manufacturer = Field("vaccine_manufacturer")
    "array of case insensitive strings"

    ventilation = Field("ventilation")
    "case insensitive string"

    def __init__(self, api_key=None):
        super().__init__(datatype="surveillance", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
