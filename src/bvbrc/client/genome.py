from bvbrc.client.client import Client
from bvbrc.RQL import Field


class GenomeClient(Client):
    """
    Data Type : genome

    Primary Key : genome_id
    """

    _version_ = Field("_version_")
    "number"

    additional_metadata = Field("additional_metadata")
    "array of case insensitive strings"

    altitude = Field("altitude")
    "case insensitive string"

    antimicrobial_resistance = Field("antimicrobial_resistance")
    "array of case insensitive strings"

    antimicrobial_resistance_evidence = Field("antimicrobial_resistance_evidence")
    "case insensitive string"

    assembly_accession = Field("assembly_accession")
    "string"

    assembly_method = Field("assembly_method")
    "case insensitive string"

    authors = Field("authors")
    "case insensitive string"

    bioproject_accession = Field("bioproject_accession")
    "string"

    biosample_accession = Field("biosample_accession")
    "string"

    biovar = Field("biovar")
    "case insensitive string"

    body_sample_site = Field("body_sample_site")
    "case insensitive string"

    body_sample_subsite = Field("body_sample_subsite")
    "case insensitive string"

    cds = Field("cds")
    "integer"

    cds_ratio = Field("cds_ratio")
    "number"

    cell_shape = Field("cell_shape")
    "case insensitive string"

    checkm_completeness = Field("checkm_completeness")
    "number"

    checkm_contamination = Field("checkm_contamination")
    "number"

    chromosomes = Field("chromosomes")
    "integer"

    city = Field("city")
    "case insensitive string"

    clade = Field("clade")
    "string"

    class_ = Field("class")
    "case insensitive string"

    coarse_consistency = Field("coarse_consistency")
    "number"

    collection_date = Field("collection_date")
    "string"

    collection_year = Field("collection_year")
    "integer"

    comments = Field("comments")
    "array of case insensitive strings"

    common_name = Field("common_name")
    "string"

    completion_date = Field("completion_date")
    "date"

    contig_l50 = Field("contig_l50")
    "integer"

    contig_n50 = Field("contig_n50")
    "integer"

    contigs = Field("contigs")
    "integer"

    core_families = Field("core_families")
    "integer"

    core_family_ratio = Field("core_family_ratio")
    "number"

    county = Field("county")
    "case insensitive string"

    culture_collection = Field("culture_collection")
    "case insensitive string"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    depth = Field("depth")
    "case insensitive string"

    disease = Field("disease")
    "array of case insensitive strings"

    family = Field("family")
    "case insensitive string"

    fine_consistency = Field("fine_consistency")
    "number"

    gc_content = Field("gc_content")
    "number"

    genbank_accessions = Field("genbank_accessions")
    "case insensitive string"

    genome_id = Field("genome_id")
    """
    **primary key**

    string
    """

    genome_length = Field("genome_length")
    "integer"

    genome_name = Field("genome_name")
    "case insensitive string"

    genome_quality = Field("genome_quality")
    "string"

    genome_quality_flags = Field("genome_quality_flags")
    "array of strings"

    genome_status = Field("genome_status")
    "case insensitive string"

    genus = Field("genus")
    "case insensitive string"

    geographic_group = Field("geographic_group")
    "case insensitive string"

    geographic_location = Field("geographic_location")
    "case insensitive string"

    gram_stain = Field("gram_stain")
    "case insensitive string"

    h1_clade_global = Field("h1_clade_global")
    "array of strings"

    h1_clade_us = Field("h1_clade_us")
    "array of strings"

    h3_clade = Field("h3_clade")
    "array of strings"

    h5_clade = Field("h5_clade")
    "array of strings"

    h_type = Field("h_type")
    "integer"

    habitat = Field("habitat")
    "case insensitive string"

    host_age = Field("host_age")
    "case insensitive string"

    host_common_name = Field("host_common_name")
    "case insensitive string"

    host_gender = Field("host_gender")
    "case insensitive string"

    host_group = Field("host_group")
    "case insensitive string"

    host_health = Field("host_health")
    "case insensitive string"

    host_name = Field("host_name")
    "case insensitive string"

    host_scientific_name = Field("host_scientific_name")
    "case insensitive string"

    hypothetical_cds = Field("hypothetical_cds")
    "integer"

    hypothetical_cds_ratio = Field("hypothetical_cds_ratio")
    "number"

    isolation_comments = Field("isolation_comments")
    "case insensitive string"

    isolation_country = Field("isolation_country")
    "case insensitive string"

    isolation_site = Field("isolation_site")
    "case insensitive string"

    isolation_source = Field("isolation_source")
    "case insensitive string"

    kingdom = Field("kingdom")
    "case insensitive string"

    lab_host = Field("lab_host")
    "case insensitive string"

    latitude = Field("latitude")
    "case insensitive string"

    lineage = Field("lineage")
    "string"

    longitude = Field("longitude")
    "case insensitive string"

    mat_peptide = Field("mat_peptide")
    "integer"

    missing_core_family_ids = Field("missing_core_family_ids")
    "array of strings"

    mlst = Field("mlst")
    "case insensitive string"

    motility = Field("motility")
    "case insensitive string"

    n_type = Field("n_type")
    "integer"

    ncbi_project_id = Field("ncbi_project_id")
    "string"

    nearest_genomes = Field("nearest_genomes")
    "array of strings"

    optimal_temperature = Field("optimal_temperature")
    "case insensitive string"

    order = Field("order")
    "case insensitive string"

    organism_name = Field("organism_name")
    "case insensitive string"

    other_clinical = Field("other_clinical")
    "array of case insensitive strings"

    other_environmental = Field("other_environmental")
    "array of case insensitive strings"

    other_names = Field("other_names")
    "array of case insensitive strings"

    other_typing = Field("other_typing")
    "array of case insensitive strings"

    outgroup_genomes = Field("outgroup_genomes")
    "array of strings"

    owner = Field("owner")
    "string"

    oxygen_requirement = Field("oxygen_requirement")
    "case insensitive string"

    p2_genome_id = Field("p2_genome_id")
    "integer"

    partial_cds = Field("partial_cds")
    "integer"

    partial_cds_ratio = Field("partial_cds_ratio")
    "number"

    passage = Field("passage")
    "case insensitive string"

    pathovar = Field("pathovar")
    "case insensitive string"

    patric_cds = Field("patric_cds")
    "integer"

    ph1n1_like = Field("ph1n1_like")
    "string"

    phenotype = Field("phenotype")
    "array of case insensitive strings"

    phylum = Field("phylum")
    "case insensitive string"

    plasmids = Field("plasmids")
    "integer"

    plfam_cds = Field("plfam_cds")
    "integer"

    plfam_cds_ratio = Field("plfam_cds_ratio")
    "number"

    public = Field("public")
    "boolean"

    publication = Field("publication")
    "string"

    reference_genome = Field("reference_genome")
    "string"

    refseq_accessions = Field("refseq_accessions")
    "case insensitive string"

    refseq_cds = Field("refseq_cds")
    "integer"

    refseq_project_id = Field("refseq_project_id")
    "string"

    rrna = Field("rrna")
    "integer"

    salinity = Field("salinity")
    "case insensitive string"

    season = Field("season")
    "string"

    segment = Field("segment")
    "string"

    segments = Field("segments")
    "integer"

    sequencing_centers = Field("sequencing_centers")
    "case insensitive string"

    sequencing_depth = Field("sequencing_depth")
    "case insensitive string"

    sequencing_platform = Field("sequencing_platform")
    "case insensitive string"

    sequencing_status = Field("sequencing_status")
    "case insensitive string"

    serovar = Field("serovar")
    "case insensitive string"

    species = Field("species")
    "case insensitive string"

    sporulation = Field("sporulation")
    "case insensitive string"

    sra_accession = Field("sra_accession")
    "string"

    state_province = Field("state_province")
    "case insensitive string"

    strain = Field("strain")
    "case insensitive string"

    subclade = Field("subclade")
    "string"

    subtype = Field("subtype")
    "string"

    superkingdom = Field("superkingdom")
    "case insensitive string"

    taxon_id = Field("taxon_id")
    "integer"

    taxon_lineage_ids = Field("taxon_lineage_ids")
    "array of strings"

    taxon_lineage_names = Field("taxon_lineage_names")
    "array of strings"

    temperature_range = Field("temperature_range")
    "case insensitive string"

    trna = Field("trna")
    "integer"

    type_strain = Field("type_strain")
    "case insensitive string"

    user_read = Field("user_read")
    "array of strings"

    user_write = Field("user_write")
    "array of strings"

    def __init__(self, api_key=None):
        super().__init__(datatype="genome", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
