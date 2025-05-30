from bvbrc.client.client import Client
from bvbrc.RQL import Field


class EpitopeClient(Client):
    """
    Data Type : epitope

    Primary Key : epitope_id
    """

    _version_ = Field("_version_")
    "number"

    assay_results = Field("assay_results")
    "array of strings"

    bcell_assays = Field("bcell_assays")
    "string"

    comments = Field("comments")
    "array of case insensitive strings"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    end = Field("end")
    "integer"

    epitope_id = Field("epitope_id")
    """
    **primary key**

    string
    """

    epitope_sequence = Field("epitope_sequence")
    "string"

    epitope_type = Field("epitope_type")
    "string"

    host_name = Field("host_name")
    "array of case insensitive strings"

    mhc_assays = Field("mhc_assays")
    "string"

    organism = Field("organism")
    "case insensitive string"

    protein_accession = Field("protein_accession")
    "string"

    protein_id = Field("protein_id")
    "string"

    protein_name = Field("protein_name")
    "case insensitive string"

    start = Field("start")
    "integer"

    taxon_id = Field("taxon_id")
    "integer"

    taxon_lineage_ids = Field("taxon_lineage_ids")
    "array of strings"

    taxon_lineage_names = Field("taxon_lineage_names")
    "array of strings"

    tcell_assays = Field("tcell_assays")
    "string"

    total_assays = Field("total_assays")
    "integer"

    def __init__(self, api_key=None):
        super().__init__(datatype="epitope", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
