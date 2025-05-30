from enum import Enum
import re


class ReturnFormat(Enum):
    """
    Enumerator with return formats supported by the BV-BRC API.

    This enumerator is intended to be used when submitting a request with one of
    the client objects to specify what the format of the reponse content should
    be.

    .. note::
        Many of the alternate return formats (besides the default JSON) do not
        work with the `Client.get()` method and can only be used with the
        `Client.search()` method.

    Examples
    --------
    Search for reference genomes and return the result in csv format:

    >>> import bvbrc as bv
    >>> genome = bv.GenomeClient()
    >>> response = genome.search(
    ...     reference_genome="Reference",
    ...     select=["genome_id", "genome_name"],
    ...     limit=5,
    ...     return_format=bv.ReturnFormat.CSV,
    ... )
    >>> print(response.text)
    genome_id,genome_name
    "11053.35","Dengue virus 1"
    "1561705.5","Bovine polyomavirus 3 3S5"
    "1303334.4","Human polyomavirus 12 hu1403"
    "2051550.4","Cabbage cytorhabdovirus 1 FERA_050726"
    "185639.16","Acheta domestica densovirus"

    Get a protein sequence in FASTA format:

    >>> gf = bv.GenomeFeatureClient()
    >>> response = gf.search(
    ...     feature_id=""PATRIC.511145.12.NC_000913.CDS.650021.651079.rev"",
    ...     return_format=bv.ReturnFormat.PROTEIN_FASTA
    ... )
    >>> print(response.text)
    >fig|511145.12.peg.648|b0618|VBIEscCol129921_0648| [Citrate [pro-3S]-lyase] ligase (EC 6.2.1.22) [Escherichia coli str. K-12 substr. MG1655 | 511145.12]
    MFGNDIFTRVKRSENKKMAEIAQFLHENDLSVDTTVEVFITVTRDEKLIACGGIAGNIIK
    CVAISESVRGEGLALTLATELINLAYERHSTHLFIYTKTEYEALFRQCGFSTLTSVPGVM
    VLMENSATRLKRYAESLKKFRHPGNKIGCIVMNANPFTNGHRYLIQQAAAQCDWLHLFLV
    KEDSSRFPYEDRLDLVLKGTADIPRLTVHRGSEYIISRATFPCYFIKEQSVINHCYTEID
    LKIFRQYLAPALGVTHRFVGTEPFCRVTAQYNQDMRYWLETPTISAPPIELVEIERLRYQ
    EMPISASRVRQLLAKNDLTAIAPLVPAVTLHYLQNLLEHSRQDAAARQKTPA
    """

    JSON = "application/json"
    "Standard JSON format (the default format)"

    SOLR_JSON = "application/solr+json"
    "SOLR JSON format"

    CSV = "text/csv"
    "A text response in CSV format"

    TSV = "text/tsv"
    "A text response in TSV format"

    EXCEL = "application/vnd.openxmlformats"
    "Return objects as an MS Excel document"

    DNA_FASTA = "application/dna+fasta"
    "DNA sequences in FASTA format"

    PROTEIN_FASTA = "application/protein+fasta"
    "Protein sequences in FASTA format"

    DNA_JSONH_FASTA = "application/dna+jsonh+fasta"
    "DNA sequences in JSONH-FASTA format"

    PROTEIN_JSONH_FASTA = "application/protein+jsonh+fasta"
    "Protein sequences in JSONH-FASTA format"

    GFF = "application/gff"
    "GFF format for genomic features"

    @staticmethod
    def extract(string: str) -> "ReturnFormat":
        """
        Extract a return format from a string using regex.

        Parameters
        ----------
        string : str
            A string containing a return format specification within it to
            extract.

        Returns
        -------
        ReturnFormat
            The extracted return format as an enumerator value.

        Examples
        --------
        >>> from bvbrc import ReturnFormat
        >>> string = "this string has a return format in it (application/json)"
        >>> ReturnFormat.extract(string)
        <ReturnFormat.JSON: 'application/json'>
        """

        fmts_str = "|".join(re.escape(fmt.value) for fmt in ReturnFormat)
        fmt_pattern = re.compile(f"({fmts_str})")
        match = fmt_pattern.search(string)
        return ReturnFormat(match.group()) if match is not None else None
