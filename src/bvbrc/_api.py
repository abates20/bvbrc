__all__ = [
    "query",
    "fld",
    "keyword",
    "Client",
    "BVBRCResponse",
    "ReturnFormat",
    "BASE_URL",
    "DOC_URL",
    "AntibioticsClient",
    "BiosetResultClient",
    "BiosetClient",
    "EnzymeClassRefClient",
    "EpitopeAssayClient",
    "EpitopeClient",
    "ExperimentClient",
    "FeatureSequenceClient",
    "GeneOntologyRefClient",
    "GenomeAmrClient",
    "GenomeFeatureClient",
    "GenomeSequenceClient",
    "GenomeClient",
    "IdRefClient",
    "MiscNiaidSgcClient",
    "PathwayRefClient",
    "PathwayClient",
    "PPIClient",
    "ProteinFamilyRefClient",
    "ProteinFeatureClient",
    "ProteinStructureClient",
    "SequenceFeatureVtClient",
    "SequenceFeatureClient",
    "SerologyClient",
    "SpGeneRefClient",
    "SpGeneClient",
    "SpikeLineageClient",
    "SpikeVariantClient",
    "StrainClient",
    "StructuredAssertionClient",
    "SubsystemRefClient",
    "SubsystemClient",
    "SurveillanceClient",
    "TaxonomyClient",
]

from typing import Union, Any, Literal
from collections.abc import Iterable

from bvbrc import RQL
from bvbrc.return_format import ReturnFormat
from bvbrc.response import BVBRCResponse
from bvbrc.client import (
    Client,
    BASE_URL,
    DOC_URL,
    AntibioticsClient,
    BiosetResultClient,
    BiosetClient,
    EnzymeClassRefClient,
    EpitopeAssayClient,
    EpitopeClient,
    ExperimentClient,
    FeatureSequenceClient,
    GeneOntologyRefClient,
    GenomeAmrClient,
    GenomeFeatureClient,
    GenomeSequenceClient,
    GenomeClient,
    IdRefClient,
    MiscNiaidSgcClient,
    PathwayRefClient,
    PathwayClient,
    PPIClient,
    ProteinFamilyRefClient,
    ProteinFeatureClient,
    ProteinStructureClient,
    SequenceFeatureVtClient,
    SequenceFeatureClient,
    SerologyClient,
    SpGeneRefClient,
    SpGeneClient,
    SpikeLineageClient,
    SpikeVariantClient,
    StrainClient,
    StructuredAssertionClient,
    SubsystemRefClient,
    SubsystemClient,
    SurveillanceClient,
    TaxonomyClient,
)


def query(
    *predicates: RQL.RQLExpr,
    select: Iterable[Union[str, RQL.Field]] = ...,
    sort: Iterable[Union[str, RQL.Field]] = ...,
    limit: Union[int, Literal["max"]] = ...,
    start: int = 0,
    **constraints: Any,
) -> RQL.RQLQuery:
    """
    Build an RQL query with specified predicates and options.

    This function constructs a Resource Query Language (RQL) query object that
    can be used to search and filter data in the BV-BRC database. It accepts
    multiple predicates and various query options to customize the search
    behavior.

    Parameters
    ----------
    \*predicates : RQL.RQLExpr
        Variable number of RQL expression objects that define the search
        criteria. These are combined using a logical AND operation.
    select : iterable of str or RQL.Field, optional
        Fields to include in the query results. Can be field names as strings
        or RQL.Field objects. If not specified, fields are returned based on
        the default behavior of the BV-BRC API (which may vary by return
        format).
    sort : iterable of str or RQL.Field, optional
        Fields to sort the results by. Can be field names as strings or
        RQL.Field objects. Multiple fields create a multi-level sort. Sort
        direction must be specified with '+' (ascending) or '-' (descending).
    limit : int or "max", optional
        Maximum number of results to return. Can be an integer or the string
        "max" to return all matching results (up to a maximum of 25,000).
    start : int, default 0
        Starting offset for pagination (0-based index).
    \*\*constraints : any
        Additional keyword arguments that specify field constraints or filters.
        Each key-value pair represents a field name and its required value.

    Returns
    -------
    RQL.RQLQuery
        A constructed RQL query object that can be submitted to the BV-BRC Data
        API using one of the provided Client objects.

    Examples
    --------
    Basic query with field constraints:

    >>> import bvbrc as bv
    >>> q = bv.query(species="Escherichia coli", limit=100)

    Query with predicates and sorting:

    >>> q = bv.query(
    ...     bv.fld("genome_length") > 5000000,
    ...     select=["genome_id", "genome_name", "genome_length"],
    ...     sort=["+genome_length"], # '+' means ascending and '-' means descending
    ...     limit=50
    ... )

    Queries can also be built step by step:

    >>> q = (
    ...     bv.query()
    ...     .filter(species="Escherichia coli")
    ...     .select("genome_id", "genome_name", "checkm_completeness")
    ...     .sort(-bv.fld("checkm_completeness"))
    ...     .limit(10)
    ... )

    A query object can then be submitted using a Client object:

    >>> client = bv.GenomeClient()
    >>> response = client.submit_query(q)
    """

    return RQL.RQLQuery.build(
        *predicates, select=select, sort=sort, limit=limit, start=start, **constraints
    )


def fld(field_name: str) -> RQL.Field:
    """
    Create an RQL field object for use in query expressions.

    This function creates a field reference that can be used to build RQL
    expressions with comparison operators and other query predicates.

    Parameters
    ----------
    field_name : str
        The name of the database field to reference. This should correspond to a
        valid field name in the target BV-BRC data collection.

    Returns
    -------
    RQL.Field
        A field object that can be used with comparison operators (==, !=, >, <,
        etc.) and other RQL operations.

    Examples
    --------
    Create field references for comparisons:

    >>> import bvbrc as bv
    >>> genome_length_field = bv.fld("genome_length")
    >>> large_genomes = genome_length_field > 1000000 # Creates an RQLExpr

    Use in query building:

    >>> q = bv.query(
    ...     bv.fld("species") == "Escherichia coli",
    ...     bv.fld("genome_status") == "Complete"
    ... )

    Each client object also contains the its corresponding fields as attributes:

    >>> genome_client = bv.GenomeClient()
    >>> q = bv.query(
    ...     genome_client.species == "Escherichia coli",
    ...     genome_client.genome_status == "Complete"
    ... )
    """

    return RQL.Field(field_name)


def keyword(value: Any) -> RQL.RQLExpr:
    """
    Create an RQL keyword search expression.

    This function creates a keyword search expression that performs text-based
    searching across searchable fields in the database. It's useful for
    performing full-text or fuzzy searches when you don't know the exact field
    to search in.

    Parameters
    ----------
    value : any
        The search term or value to look for (typically a string). The search is
        case-insensitive and supports '*' as a wildcard.

    Returns
    -------
    RQL.RQLExpr
        An RQL expression object representing the keyword search that can be used as
        a predicate in query construction.

    Examples
    --------
    Simple keyword search:

    >>> import bvbrc as bv
    >>> q = bv.query(bv.keyword("tuberculosis"), limit=100)

    Combine keyword search with other constraints:

    >>> q = bv.query(
    ...     bv.keyword("antibiotic resistance"),
    ...     bv.fld("genome_status") == "Complete",
    ...     limit=50
    ... )

    Multiple search terms:

    >>> q = bv.query(
    ...     bv.keyword("SARS-CoV-2"),
    ...     select=["genome_id", "genome_name", "collection_date"],
    ...     sort=["-collection_date"]
    ... )
    """

    return RQL.keyword(value)
