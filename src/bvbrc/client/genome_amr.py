from bvbrc.client.client import Client
from bvbrc.RQL import Field


class GenomeAmrClient(Client):
    """
    Data Type : genome_amr

    Primary Key : id
    """

    _version_ = Field("_version_")
    "number"

    antibiotic = Field("antibiotic")
    "string"

    computational_method = Field("computational_method")
    "case insensitive string"

    computational_method_performance = Field("computational_method_performance")
    "string"

    computational_method_version = Field("computational_method_version")
    "string"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    evidence = Field("evidence")
    "case insensitive string"

    genome_id = Field("genome_id")
    "string"

    genome_name = Field("genome_name")
    "case insensitive string"

    id = Field("id")
    """
    **primary key**

    string
    """

    laboratory_typing_method = Field("laboratory_typing_method")
    "case insensitive string"

    laboratory_typing_method_version = Field("laboratory_typing_method_version")
    "string"

    laboratory_typing_platform = Field("laboratory_typing_platform")
    "case insensitive string"

    measurement = Field("measurement")
    "string"

    measurement_sign = Field("measurement_sign")
    "string"

    measurement_unit = Field("measurement_unit")
    "string"

    measurement_value = Field("measurement_value")
    "string"

    owner = Field("owner")
    "string"

    pmid = Field("pmid")
    "array of integers"

    public = Field("public")
    "boolean"

    resistant_phenotype = Field("resistant_phenotype")
    "string"

    source = Field("source")
    "case insensitive string"

    taxon_id = Field("taxon_id")
    "integer"

    testing_standard = Field("testing_standard")
    "case insensitive string"

    testing_standard_year = Field("testing_standard_year")
    "integer"

    user_read = Field("user_read")
    "array of strings"

    user_write = Field("user_write")
    "array of strings"

    vendor = Field("vendor")
    "case insensitive string"

    def __init__(self, api_key=None):
        super().__init__(datatype="genome_amr", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
