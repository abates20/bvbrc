from bvbrc.client.client import Client
from bvbrc.RQL import Field


class SerologyClient(Client):
    """
    Data Type : serology

    Primary Key : id
    """

    additional_metadata = Field("additional_metadata")
    "array of case insensitive strings"

    collection_city = Field("collection_city")
    "case insensitive string"

    collection_country = Field("collection_country")
    "case insensitive string"

    collection_date = Field("collection_date")
    "date"

    collection_state = Field("collection_state")
    "case insensitive string"

    collection_year = Field("collection_year")
    "case insensitive string"

    comments = Field("comments")
    "array of case insensitive strings"

    contributing_institution = Field("contributing_institution")
    "case insensitive string"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    genbank_accession = Field("genbank_accession")
    "array of case insensitive strings"

    geographic_group = Field("geographic_group")
    "case insensitive string"

    host_age = Field("host_age")
    "case insensitive string"

    host_age_group = Field("host_age_group")
    "case insensitive string"

    host_common_name = Field("host_common_name")
    "case insensitive string"

    host_health = Field("host_health")
    "case insensitive string"

    host_identifier = Field("host_identifier")
    "string"

    host_sex = Field("host_sex")
    "case insensitive string"

    host_species = Field("host_species")
    "case insensitive string"

    host_type = Field("host_type")
    "array of case insensitive strings"

    id = Field("id")
    """
    **primary key**

    string
    """

    positive_definition = Field("positive_definition")
    "case insensitive string"

    project_identifier = Field("project_identifier")
    "string"

    sample_accession = Field("sample_accession")
    "string"

    sample_identifier = Field("sample_identifier")
    "string"

    serotype = Field("serotype")
    "array of case insensitive strings"

    strain = Field("strain")
    "case insensitive string"

    taxon_lineage_ids = Field("taxon_lineage_ids")
    "array of strings"

    test_antigen = Field("test_antigen")
    "case insensitive string"

    test_interpretation = Field("test_interpretation")
    "case insensitive string"

    test_pathogen = Field("test_pathogen")
    "case insensitive string"

    test_result = Field("test_result")
    "case insensitive string"

    test_type = Field("test_type")
    "case insensitive string"

    virus_identifier = Field("virus_identifier")
    "case insensitive string"

    def __init__(self, api_key=None):
        super().__init__(datatype="serology", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
