from bvbrc.client.client import Client
from bvbrc.RQL import Field


class ProteinStructureClient(Client):
    """
    Data Type : protein_structure

    Primary Key : pdb_id
    """

    alignments = Field("alignments")
    "array of strings"

    authors = Field("authors")
    "array of strings"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    feature_id = Field("feature_id")
    "string"

    file_path = Field("file_path")
    "string"

    gene = Field("gene")
    "array of strings"

    genome_id = Field("genome_id")
    "string"

    institution = Field("institution")
    "string"

    method = Field("method")
    "array of strings"

    organism_name = Field("organism_name")
    "array of case insensitive strings"

    patric_id = Field("patric_id")
    "string"

    pdb_id = Field("pdb_id")
    """
    **primary key**

    string
    """

    pmid = Field("pmid")
    "array of strings"

    product = Field("product")
    "array of strings"

    release_date = Field("release_date")
    "date"

    resolution = Field("resolution")
    "string"

    sequence = Field("sequence")
    "array of strings"

    sequence_md5 = Field("sequence_md5")
    "array of strings"

    taxon_id = Field("taxon_id")
    "array of integers"

    taxon_lineage_ids = Field("taxon_lineage_ids")
    "array of strings"

    taxon_lineage_names = Field("taxon_lineage_names")
    "array of strings"

    title = Field("title")
    "case insensitive string"

    uniprotkb_accession = Field("uniprotkb_accession")
    "array of strings"

    def __init__(self, api_key=None):
        super().__init__(datatype="protein_structure", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
