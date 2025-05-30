from bvbrc.client.client import Client
from bvbrc.RQL import Field


class TaxonomyClient(Client):
    """
    Data Type : taxonomy

    Primary Key : taxon_id
    """

    _version_ = Field("_version_")
    "number"

    cds_mean = Field("cds_mean")
    "number"

    cds_sd = Field("cds_sd")
    "number"

    core_families = Field("core_families")
    "integer"

    core_family_ids = Field("core_family_ids")
    "array of strings"

    description = Field("description")
    "string"

    division = Field("division")
    "string"

    genetic_code = Field("genetic_code")
    "integer"

    genome_count = Field("genome_count")
    "integer"

    genome_length_mean = Field("genome_length_mean")
    "number"

    genome_length_sd = Field("genome_length_sd")
    "number"

    genomes = Field("genomes")
    "integer"

    genomes_f = Field("genomes_f")
    "string"

    hypothetical_cds_ratio_mean = Field("hypothetical_cds_ratio_mean")
    "number"

    hypothetical_cds_ratio_sd = Field("hypothetical_cds_ratio_sd")
    "number"

    lineage = Field("lineage")
    "string"

    lineage_ids = Field("lineage_ids")
    "array of integers"

    lineage_names = Field("lineage_names")
    "array of strings"

    lineage_ranks = Field("lineage_ranks")
    "array of strings"

    other_names = Field("other_names")
    "array of case insensitive strings"

    parent_id = Field("parent_id")
    "integer"

    plfam_cds_ratio_mean = Field("plfam_cds_ratio_mean")
    "number"

    plfam_cds_ratio_sd = Field("plfam_cds_ratio_sd")
    "number"

    taxon_id = Field("taxon_id")
    """
    **primary key**

    string
    """

    taxon_id_i = Field("taxon_id_i")
    "integer"

    taxon_name = Field("taxon_name")
    "case insensitive string"

    taxon_rank = Field("taxon_rank")
    "string"

    def __init__(self, api_key=None):
        super().__init__(datatype="taxonomy", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
