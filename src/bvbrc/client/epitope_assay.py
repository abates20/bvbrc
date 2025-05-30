from bvbrc.client.client import Client
from bvbrc.RQL import Field


class EpitopeAssayClient(Client):
    """
    Data Type : epitope_assay

    Primary Key : assay_id
    """

    _version_ = Field("_version_")
    "number"

    assay_group = Field("assay_group")
    "string"

    assay_id = Field("assay_id")
    """
    **primary key**

    string
    """

    assay_measurement = Field("assay_measurement")
    "string"

    assay_measurement_unit = Field("assay_measurement_unit")
    "string"

    assay_method = Field("assay_method")
    "string"

    assay_result = Field("assay_result")
    "string"

    assay_type = Field("assay_type")
    "string"

    authors = Field("authors")
    "string"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    end = Field("end")
    "integer"

    epitope_id = Field("epitope_id")
    "string"

    epitope_sequence = Field("epitope_sequence")
    "string"

    epitope_type = Field("epitope_type")
    "string"

    host_name = Field("host_name")
    "case insensitive string"

    host_taxon_id = Field("host_taxon_id")
    "string"

    mhc_allele = Field("mhc_allele")
    "string"

    mhc_allele_class = Field("mhc_allele_class")
    "string"

    organism = Field("organism")
    "case insensitive string"

    pdb_id = Field("pdb_id")
    "string"

    pmid = Field("pmid")
    "string"

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

    title = Field("title")
    "case insensitive string"

    def __init__(self, api_key=None):
        super().__init__(datatype="epitope_assay", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
