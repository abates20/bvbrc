from bvbrc.client.client import Client
from bvbrc.RQL import Field


class AntibioticsClient(Client):
    """
    Data Type : antibiotics

    Primary Key : pubchem_cid
    """

    _version_ = Field("_version_")
    "number"

    antibiotic_name = Field("antibiotic_name")
    "case insensitive string"

    atc_classification = Field("atc_classification")
    "array of strings"

    canonical_smiles = Field("canonical_smiles")
    "string"

    cas_id = Field("cas_id")
    "string"

    date_inserted = Field("date_inserted")
    "date"

    date_modified = Field("date_modified")
    "date"

    description = Field("description")
    "array of strings"

    drugbank_interactions = Field("drugbank_interactions")
    "array of strings"

    inchi_key = Field("inchi_key")
    "string"

    isomeric_smiles = Field("isomeric_smiles")
    "string"

    mechanism_of_action = Field("mechanism_of_action")
    "array of strings"

    molecular_formula = Field("molecular_formula")
    "string"

    molecular_weight = Field("molecular_weight")
    "string"

    pharmacological_classes = Field("pharmacological_classes")
    "array of strings"

    pharmacology = Field("pharmacology")
    "array of strings"

    pubchem_cid = Field("pubchem_cid")
    """
    **primary key**

    string
    """

    pubchem_cid_i = Field("pubchem_cid_i")
    "integer"

    synonyms = Field("synonyms")
    "array of case insensitive strings"

    def __init__(self, api_key=None):
        super().__init__(datatype="antibiotics", api_key=api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
