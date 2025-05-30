"""
The Resource Query Language (RQL) module. Defines objects that
are meant to make building RQL queries feel intuitive.
"""

from typing import Union, Any, Optional, Literal
from collections.abc import Iterable
import warnings
import re
from copy import copy

from bvbrc import _utils


MAX_RESULTS = 25000
"The maximum number of results that BV-BRC will return for one request"


class RQLExpr:
    """
    A Resource Query Language (RQL) expression.

    This class represents a single RQL expression that can be combined with
    other expressions using logical operators (AND, OR) to build complex queries.

    Attributes
    ----------
    expr : str
        The RQL expression string.

    Examples
    --------
    >>> expr = RQLExpr("eq(genome_name,Mycobacterium)")
    >>> print(expr)
    eq(genome_name,Mycobacterium)

    >>> combined = RQLExpr("eq(genome_name,Mycobacterium)") & RQLExpr("gt(contigs,1)")
    >>> print(combined)
    and(eq(genome_name,Mycobacterium),gt(contigs,1))
    """

    def __init__(self, expr: str):
        """
        Initialize a Resource Query Language (RQL) expression object.

        Attributes
        ----------
        expr : str
            The RQL expression string.

        Examples
        --------
        >>> expr = RQLExpr("eq(genome_name,Mycobacterium)")
        """

        self.expr: str = str(expr)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self.expr)})"

    def __str__(self) -> str:
        return self.expr

    def __and__(self, other: Union["RQLExpr", str]) -> "RQLExpr":
        """
        Combine two RQL expressions with logical AND.

        Parameters
        ----------
        other : RQLExpr or str
            The other expression to combine with this one.

        Returns
        -------
        RQLExpr
            A new RQLExpr representing the AND combination.

        Examples
        --------
        >>> expr1 = RQLExpr("eq(genome_name,Mycobacterium)")
        >>> expr2 = RQLExpr("gt(contigs,1)")
        >>> combined = expr1 & expr2
        >>> print(combined)
        and(eq(genome_name,Mycobacterium),gt(contigs,1))
        """

        return _and(self, other)

    def __rand__(self, other: str) -> "RQLExpr":
        """
        Combine two RQL expressions with logical AND.

        Used if the left side of the expression is a string instead of an
        RQLExpr object.

        Parameters
        ----------
        other : str
            The other expression to combine with this one.

        Returns
        -------
        RQLExpr
            A new RQLExpr representing the AND combination.

        Examples
        --------
        >>> expr1 = RQLExpr("eq(genome_name,Mycobacterium)")
        >>> expr2 = "gt(contigs,1)"
        >>> combined = expr2 & expr1
        >>> print(combined)
        and(gt(contigs,1),eq(genome_name,Mycobacterium))
        """

        return _and(other, self)

    def __or__(self, other: Union["RQLExpr", str]) -> "RQLExpr":
        """
        Combine two RQL expressions with logical OR.

        Parameters
        ----------
        other : RQLExpr or str
            The other expression to combine with this one.

        Returns
        -------
        RQLExpr
            A new RQLExpr representing the OR combination.

        Examples
        --------
        >>> expr1 = RQLExpr("eq(genome_name,Mycobacterium)")
        >>> expr2 = RQLExpr("eq(genome_name,Escherichia)")
        >>> combined = expr1 | expr2
        >>> print(combined)
        or(eq(genome_name,Mycobacterium),eq(genome_name,Escherichia))
        """

        return _or(self, other)

    def __ror__(self, other: str) -> "RQLExpr":
        """
        Combine two RQL expressions with logical OR.

        Used if the left side of the expression is a string instead of an
        RQLExpr object.

        Parameters
        ----------
        other : str
            The other expression to combine with this one.

        Returns
        -------
        RQLExpr
            A new RQLExpr representing the OR combination.

        Examples
        --------
        >>> expr1 = "eq(genome_name,Mycobacterium)"
        >>> expr2 = RQLExpr("eq(genome_name,Escherichia)")
        >>> combined = expr1 | expr2
        >>> print(combined)
        or(eq(genome_name,Mycobacterium),eq(genome_name,Escherichia))
        """

        return _or(other, self)

    def __copy__(self) -> "RQLExpr":
        """
        Create a shallow copy of the RQLExpr.

        Returns
        -------
        RQLExpr
            A copy of this RQLExpr instance.
        """

        return RQLExpr(self.expr)


class Field:
    """
    Represents a field in an RQL query.

    This class provides a convenient interface for building RQL expressions
    involving database fields, supporting comparison operations and sorting.

    Attributes
    ----------
    name : str
        The field name.

    Examples
    --------
    >>> field = Field("genome_name")
    >>> expr = field == "Mycobacterium"
    >>> print(expr)
    eq(genome_name,Mycobacterium)

    >>> sort_field = +Field("genome_name")  # ascending sort
    >>> print(sort_field)
    +genome_name
    """

    def __init__(self, name: str):
        """
        Initialize a Field object.

        Parameters
        ----------
        name : str
            The field name.

        Examples
        --------
        >>> field = Field("genome_name")
        """

        self.name: str = name

    def __repr__(self) -> str:
        return f"Field({repr(self.name)})"

    def __str__(self) -> str:
        return self.name

    def __pos__(self) -> "Field":
        """
        Mark field for ascending sort order.

        Returns
        -------
        Field
            A new Field instance where the name is prefixed with '+' for
            ascending sort.

        Examples
        --------
        >>> field = Field("genome_length")
        >>> ascending = +field
        >>> print(ascending)
        +genome_length
        """

        name = self.name.lstrip("+-")
        return Field(f"+{name}")

    def __neg__(self) -> "Field":
        """
        Mark field for descending sort order.

        Returns
        -------
        Field
            A new Field instance where the name is prefixed with '-' for
            descending sort.

        Examples
        --------
        >>> field = Field("genome_length")
        >>> descending = -field
        >>> print(descending)
        -genome_length
        """

        name = self.name.lstrip("+-")
        return Field(f"-{name}")

    def __eq__(self, value: Any) -> RQLExpr:
        """
        Create an RQL equality expression for filtering (i.e., the field must be
        equal to the specified value).

        Parameters
        ----------
        value : Any
            The value that the field should be equal to.

        Returns
        -------
        RQLExpr
            An RQL equality expression.

        Examples
        --------
        >>> field = Field("genome_name")
        >>> expr = field == "Mycobacterium"
        >>> print(expr)
        eq(genome_name,Mycobacterium)
        """

        return _eq(self, value)

    def __ne__(self, value: Any) -> RQLExpr:
        """
        Create a not-equal RQL expression for filtering (i.e., the field must be
        not equal to the specified value).

        Parameters
        ----------
        value : Any
            The value that the field should be not equal to.

        Returns
        -------
        RQLExpr
            An RQL not-equal expression.

        Examples
        --------
        >>> field = Field("genome_name")
        >>> expr = field != "Mycobacterium"
        >>> print(expr)
        ne(genome_name,Mycobacterium)
        """

        return _ne(self, value)

    def __gt__(self, value: Any) -> RQLExpr:
        """
        Create a greater-than RQL expression for filtering (i.e., the field must
        be greater than the specified value).

        Parameters
        ----------
        value : Any
            The value to compare the field against.

        Returns
        -------
        RQLExpr
            An RQL greater-than expression.

        Examples
        --------
        >>> field = Field("contigs")
        >>> expr = field > 10
        >>> print(expr)
        gt(contigs,10)
        """

        return _gt(self, value)

    def __lt__(self, value: Any) -> RQLExpr:
        """
        Create a less-than RQL expression for filtering (i.e., the field must be
        less than the specified value).

        Parameters
        ----------
        value : Any
            The value to compare the field against.

        Returns
        -------
        RQLExpr
            An RQL less-than expression.

        Examples
        --------
        >>> field = Field("contigs")
        >>> expr = field < 100
        >>> print(expr)
        lt(contigs,100)
        """

        return _lt(self, value)

    def __ge__(self, value: Any) -> RQLExpr:
        """
        Create a greater-than-or-equal RQL expression for filtering (i.e., the
        field must be greater than or equal to the specified value).

        Parameters
        ----------
        value : Any
            The value to compare the field against.

        Returns
        -------
        RQLExpr
            An RQL greater-than-or-equal expression (implemented as OR of > and
            ==).

        Examples
        --------
        >>> field = Field("contigs")
        >>> expr = field >= 10
        >>> print(expr)
        or(gt(contigs,10),eq(contigs,10))
        """

        return _or(_gt(self, value), _eq(self, value))

    def __le__(self, value: Any) -> RQLExpr:
        """
        Create a less-than-or-equal RQL expression for filtering (i.e., the
        field must be less than or equal to the specified value).

        Parameters
        ----------
        value : Any
            The value to compare the field against.

        Returns
        -------
        RQLExpr
            An RQL less-than-or-equal expression (implemented as OR of < and
            ==).

        Examples
        --------
        >>> field = Field("contigs")
        >>> expr = field <= 100
        >>> print(expr)
        or(lt(contigs,100),eq(contigs,100))
        """

        return _or(_lt(self, value), _eq(self, value))

    def isin(self, values: Iterable[Any]) -> RQLExpr:
        """
        Create an 'in' RQL expression for checking if field value is in a list
        (i.e., the field must be equal to one of the values in the list).

        Parameters
        ----------
        values : Iterable[Any]
            An iterable of values to check against.

        Returns
        -------
        RQLExpr
            An RQL 'in' expression.

        Examples
        --------
        >>> field = Field("genome_name")
        >>> expr = field.isin(["Mycobacterium", "Escherichia", "Salmonella"])
        >>> print(expr)
        in(genome_name,(Mycobacterium,Escherichia,Salmonella))
        """

        return _in(self, *values)


class RQLQuery:
    """
    A class representing an RQL query (i.e., a combination of RQL expressions).

    This class provides a fluent interface for building complex RQL queries
    with filtering, selection, sorting, and limiting capabilities.

    Attributes
    ----------
    content_type : str
        The content type for the RQL query. This is incorporated into the
        request header when the query is submitted.

    Examples
    --------
    >>> query = RQLQuery.build(
    ...     Field("genome_name") == "Mycobacterium",
    ...     select=["genome_id", "genome_name"],
    ...     sort=["+genome_name"],
    ...     limit=100
    ... )
    >>> print(query.expression)
    and(eq(genome_name,Mycobacterium))&select(genome_id,genome_name)&sort(+genome_name)&limit(100,0)
    """

    content_type = "application/rqlquery+x-www-form-urlencoded"

    def __init__(
        self,
        filter: Optional[RQLExpr] = None,
        select: Optional[RQLExpr] = None,
        sort: Optional[RQLExpr] = None,
        limit: Optional[RQLExpr] = None,
    ):
        """
        Initialize an RQL query object.

        Parameters
        ----------
        filter : RQLExpr, optional
            A filter expression for the query. Can be a single constraint for
            filtering such as 'eq', 'ne', etc. or multiple constraints combined
            with 'and'/'or'.
        select : RQLExpr, optional
            A 'select' expression specifying which fields to return.
        sort : RQLExpr, optional
            A 'sort' expression specifying how to order results that are
            retrieved.
        limit : RQLExpr, optional
            A 'limit' expression for specifying a limit to how many results will
            be returned as well as the starting index of the first result.
        """

        self._exprs: dict[str, RQLExpr] = dict(
            filter=filter, select=select, sort=sort, limit=limit
        )

    def __repr__(self) -> str:
        kwargs = []
        for key, value in self._exprs.items():
            if value is not None:
                kwargs.append(f"{key}={repr(value)}")
        return f"RQLQuery({', '.join(kwargs)})"

    def __str__(self) -> str:
        return f"RQL query: {repr(self.expression)}"

    def __deepcopy__(self, memo) -> "RQLQuery":
        """
        Create a deep copy of the RQLQuery.

        Parameters
        ----------
        memo : dict
            Memoization dictionary for the copy operation.

        Returns
        -------
        RQLQuery
            A deep copy of this RQLQuery instance.
        """

        return RQLQuery(**{key: copy(expr) for key, expr in self._exprs.items()})

    @property
    def expression(self) -> str:
        """
        Get the full RQL query expression.

        Returns
        -------
        str
            The complete RQL query as a string. Any spaces are replaced by '+'.

        Examples
        --------
        >>> query = RQLQuery(filter=RQLExpr("eq(genome_name,Mycobacterium)"))
        >>> print(query.expression)
        eq(genome_name%,Mycobacterium)
        """

        query_str = "&".join(str(e) for e in self._exprs.values() if e is not None)
        return _utils.url_encode(query_str)

    @property
    def no_limit(self) -> bool:
        """
        Check if the query limit is set to `None` (unlimited).

        Returns
        -------
        bool
            True if the limit is set to `None`, False otherwise.

        Examples
        --------
        >>> query = RQLQuery(limit=RQLExpr("limit(None,0)"))
        >>> print(query.no_limit)
        True
        """

        limit_pattern = re.compile(r"limit\((\d+|None),(\d+)\)")
        limit_expr = str(self._exprs.get("limit"))
        matches = limit_pattern.findall(limit_expr)
        if len(matches) > 0:
            limit, start = matches[0]
            return limit == "None"
        return False

    @classmethod
    def build(
        cls,
        *predicates: RQLExpr,
        select: Iterable[Union[str, Field]] = ...,
        sort: Iterable[Union[str, Field]] = ...,
        limit: Union[int, Literal["max"]] = ...,
        start: int = 0,
        **constraints: Any,
    ) -> "RQLQuery":
        """
        Build an RQL query object.

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
        RQLQuery
            A complete RQL query object.

        Examples
        --------
        >>> query = RQLQuery.build(
        ...     Field("genome_name") == "Mycobacterium",
        ...     select=["genome_id", "genome_name"],
        ...     sort=["+genome_name"],
        ...     limit=100,
        ...     taxon_lineage_names="Bacteria"
        ... )
        >>> print(query)
        RQL query: 'and(eq(genome_name,Mycobacterium),eq(taxon_lineage_names,Bacteria))&select(genome_id,genome_name)&sort(+genome_name)&limit(100,0)'
        """

        query = cls()
        query = query.filter(*predicates, **constraints)

        if select is not Ellipsis:
            query = query.select(*select)
        if sort is not Ellipsis:
            query = query.sort(*sort)

        if limit is not Ellipsis:
            if limit == "max":
                limit = MAX_RESULTS
            query = query.limit(limit, start)
        elif start != 0:  # Warn if start is given without limit
            limit = 25  # default limit
            warnings.warn(
                f"Start was specified without limit. Using default limit of {limit}."
                " Please specifiy the limit if also setting the start value."
            )
            query = query.limit(limit, start)

        return query

    @_utils.copy_self
    def filter(self_copy, *predicates: RQLExpr, **constraints: Any) -> "RQLQuery":
        """
        Add filter expressions to the query, replacing any previous filter
        expressions that the query may have contained.

        The query object is copied before being modified, and then the copied
        instance is returned.

        Parameters
        ----------
        \*predicates : RQL.RQLExpr
            Variable number of RQL expression objects that define the search
            criteria. These are combined using a logical AND operation.
        \*\*constraints : any
            Additional `field=value` keyword arguments that specify field
            constraints or filters. Each key-value pair represents a field name
            and its required value.

        Returns
        -------
        RQLQuery
            A new RQLQuery instance with the specified filters.

        Examples
        --------
        >>> import bvbrc as bv
        >>> query = bv.query().filter(
        ...     bv.fld("genome_name") == "Mycobacterium",
        ...     taxon_lineage_names="Bacteria"
        ... )
        >>> print(query)
        RQL query: 'and(eq(genome_name,Mycobacterium),eq(taxon_lineage_names,Bacteria))'
        """

        more_predicates = tuple(_eq(field, val) for field, val in constraints.items())
        all_predicates = predicates + more_predicates

        if len(all_predicates) > 1:
            self_copy._exprs["filter"] = _and(*(predicates + more_predicates))
        elif len(all_predicates) == 1:
            self_copy._exprs["filter"] = all_predicates[0]

        return self_copy

    @_utils.copy_self
    def select(self_copy, *fields: Union[str, Field]) -> "RQLQuery":
        """
        Specify which fields to include in query results, replacing the previous
        select expression if the query contained one.

        The query object is copied before being modified, and then the copied
        instance is returned.

        Parameters
        ----------
        \*fields : Union[str, Field]
            Variable number of field names or Field objects to select.

        Returns
        -------
        RQLQuery
            A new RQLQuery instance with the select clause.

        Examples
        --------
        >>> import bvbrc as bv
        >>> query = bv.query().select(
        ...     "genome_id",
        ...     "genome_name",
        ...     "taxon_lineage_names"
        ... )
        >>> print(query)
        RQL query: 'select(genome_id,genome_name,taxon_lineage_names)'
        """

        self_copy._exprs["select"] = _select(*fields)
        return self_copy

    @_utils.copy_self
    def sort(self_copy, *fields: Union[str, Field]) -> "RQLQuery":
        """
        Specify sorting for query results. replacing any previously specified
        sorting that the query may have contained.

        Parameters
        ----------
        \*fields : Union[str, Field]
            Variable number of field names or Field objects to sort by.
            Fields must start with '+' for ascending or '-' for descending
            order.

        Returns
        -------
        RQLQuery
            A new RQLQuery instance with the sort clause.

        Examples
        --------
        >>> import bvbrc as bv
        >>> query = bv.query().sort("+genome_name", "-genome_length")
        >>> print(query)
        RQL query: 'sort(+genome_name,-genome_length)'
        """

        self_copy._exprs["sort"] = _sort(*fields)
        return self_copy

    @_utils.copy_self
    def limit(self_copy, count: int, start: int = 0) -> "RQLQuery":
        """
        Specifiy the limit for the number of results returned and (optionally)
        the starting index for the first result. Replaces the previously set
        limit if the query contained one.

        Parameters
        ----------
        count : int
            Maximum number of results to return.
        start : int, default 0
            Starting offset for first result returned.

        Returns
        -------
        RQLQuery
            A new RQLQuery instance with the limit clause.

        Examples
        --------
        >>> import bvbrc as bv
        >>> query = bv.query().limit(100, start=50)  # Get results 50-149
        >>> print(query)
        RQL query: 'limit(100,50)'
        """

        self_copy._exprs["limit"] = _limit(count, start)
        return self_copy


def keyword(value: Any) -> RQLExpr:
    """
    Create a keyword RQL search expression.

    Keyword expressions are used to search for a keyword across all fields.

    Parameters
    ----------
    value : Any
        The keyword or phrase to search for.

    Returns
    -------
    RQLExpr
        An RQL keyword search expression.

    Examples
    --------
    >>> expr = keyword("mycobacterium tuberculosis")
    >>> print(expr)
    keyword(mycobacterium tuberculosis)
    """

    return _keyword(value)


# ------------------------------------------------------------------------- #
# Private methods for each of the RQL operators available in the BV-BRC API #
# ------------------------------------------------------------------------- #


def _eq(field: Union[str, Field], value: Any) -> RQLExpr:
    return RQLExpr(f"eq({field},{value})")


def _ne(field: Union[str, Field], value: Any) -> RQLExpr:
    return RQLExpr(f"ne({field},{value})")


def _gt(field: Union[str, Field], value: Any) -> RQLExpr:
    return RQLExpr(f"gt({field},{value})")


def _lt(field: Union[str, Field], value: Any) -> RQLExpr:
    return RQLExpr(f"lt({field},{value})")


def _keyword(value: Any) -> RQLExpr:
    return RQLExpr(f"keyword({value})")


def _in(field: Union[str, Field], *values: Any) -> RQLExpr:
    return RQLExpr(f"in({field},({','.join([str(x) for x in values])}))")


def _and(*exprs: RQLExpr) -> RQLExpr:
    return RQLExpr(f"and({','.join([str(x) for x in exprs])})")


def _or(*exprs: RQLExpr) -> RQLExpr:
    return RQLExpr(f"or({','.join(str(x) for x in exprs)})")


def _select(*fields: Union[str, Field]) -> RQLExpr:
    return RQLExpr(f"select({','.join(str(f) for f in fields)})")


def _sort(*fields: Union[str, Field]) -> RQLExpr:
    for field in fields:
        if not (field.startswith("+") or field.startswith("-")):
            raise ValueError(
                f"Field '{field}' must start with '+' or '-' to specify sort direction."
            )
    return RQLExpr(f"sort({','.join(str(f) for f in fields)})")


def _limit(count: int, start: int = 0) -> RQLExpr:
    return RQLExpr(f"limit({count},{start})")


def _facet(*facets: tuple[Any]) -> RQLExpr:
    facet_strs = [f"({','.join([str(x) for x in f])})" for f in facets]
    return RQLExpr(f"facet({','.join(facet_strs)})")
