from typing import Union, Any, Optional, Literal
from collections.abc import Iterable

import requests

from bvbrc import RQL
from bvbrc.response import BVBRCResponse
from bvbrc.return_format import ReturnFormat


BASE_URL = "https://www.bv-brc.org/api"
"The entry point to the BV-BRC Data API"

DOC_URL = BASE_URL + "/doc"
"The URL to the BV-BRC Data API documentation"

_Timeout = Union[float, tuple[float, float]]
"Type representing a timeout specification"


class Client:
    """
    The base client class defining methods for interacting with BV-BRC
    (Bacterial and Viral Bioinformatics Resource Center) through its data API.

    All client objects are derived from this base class.

    Attributes
    ----------
    BASE_URL : str
        The base URL for the BV-BRC service.
    datatype : str
        The data type this client instance is configured for.
    URL : str
        The complete URL endpoint for the specified datatype.
    DOC_URL : str
        The documentation URL for the specified datatype.
    API_KEY : str or None
        The API key for authentication, if provided.
    """

    def __init__(
        self, datatype: str, base_url: str = BASE_URL, api_key: Optional[str] = None
    ):
        """
        Initialize a new BV-BRC client instance.

        Parameters
        ----------
        datatype : str
            The type of data to work with (e.g., 'genome', 'genome_feature',
            'protein_family'). This determines which BV-BRC data collection the
            client will interact with.
        base_url : str, default BASE_URL
            The base URL for the BV-BRC API service. Uses the default BV-BRC URL
            if not specified.
        api_key : str, optional
            API key for authentication.
        """

        self.BASE_URL: str = base_url
        self.datatype: str = datatype
        self.URL: str = f"{base_url}/{datatype}"
        self.DOC_URL: str = f"{base_url}/doc/{datatype}"
        self.API_KEY: Optional[str] = api_key

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}({repr(self.BASE_URL)}, {repr(self.datatype)})"
        )

    def get(
        self,
        id: str,
        *,
        return_format: Union[str, ReturnFormat] = ReturnFormat.JSON,
        timeout: Optional[_Timeout] = None,
    ) -> BVBRCResponse:
        """
        Retrieve a specific record by its unique identifier.

        Fetches a single data record from the BV-BRC database using its unique
        ID. This is useful when you know the exact identifier of the record you
        want to retrieve.

        Parameters
        ----------
        id : str
            The unique identifier of the record to retrieve. The format depends
            on the datatype (e.g., genome IDs, feature IDs, etc.).
        return_format : str or ReturnFormat, default ReturnFormat.JSON
            The desired format for the returned data. See the
            `BV-BRC documentation <https://bv-brc.org/api/doc>`_ for allowed
            return formats.
        timeout : float or tuple, optional
            Timeout for the HTTP request. Can be a single float (total timeout)
            or a tuple of (connect_timeout, read_timeout).

        Returns
        -------
        BVBRCResponse
            A response object (derived from the requests.Response object)
            containing the retrieved data and associated response metadata.

        Examples
        --------
        Retrieve a genome by ID:

        >>> import bvbrc as bv
        >>> genome_client = bv.GenomeClient()
        >>> response = genome_client.get("1313.5458")

        Retrieve with custom format and timeout:

        >>> response = genome_client.get(
        ...     "1313.5458",
        ...     return_format=bv.ReturnFormat.CSV,
        ...     timeout=30
        ... )
        """

        rq_response = requests.get(
            f"{self.URL}/{id}",
            headers={"Accept": ReturnFormat(return_format).value},
            timeout=timeout,
        )
        return BVBRCResponse.from_response(rq_response)

    def search(
        self,
        *predicates: RQL.RQLExpr,
        select: Iterable[Union[str, RQL.Field]] = ...,
        sort: Iterable[Union[str, RQL.Field]] = ...,
        limit: Union[int, Literal["max"]] = ...,
        start: int = 0,
        return_format: Union[str, ReturnFormat] = ReturnFormat.JSON,
        timeout: Optional[_Timeout] = None,
        **constraints: Any,
    ) -> BVBRCResponse:
        """
        Search for records using provided parameters.

        Sends a query to the BV-BRC API using Resource Query Language (RQL)
        expressions and field constraints. This is the primary method for
        finding records that match specific criteria.

        Parameters
        ----------
        \*predicates : RQL.RQLExpr
            Variable number of RQL expression objects that define the search
            criteria. These are combined using a logical AND operation.
        select : iterable of str or RQL.Field, optional
            Fields to include in the query results. Can be field names as
            strings or RQL.Field objects. If not specified, fields are returned
            based on the default behavior of the BV-BRC API (which may vary by
            return format).
        sort : iterable of str or RQL.Field, optional
            Fields to sort the results by. Can be field names as strings or
            RQL.Field objects. Multiple fields create a multi-level sort. Sort
            direction must be specified with '+' (ascending) or '-'
            (descending).
        limit : int or "max", optional
            Maximum number of results to return. Can be an integer or the string
            "max" to return all matching results (up to a maximum of 25,000).
        start : int, default 0
            Starting offset for pagination (0-based index).
        return_format : str or ReturnFormat, default ReturnFormat.JSON
            The desired format for the returned data. See the
            `BV-BRC documentation <https://bv-brc.org/api/doc>`_ for allowed
            return formats.
        timeout : float or tuple, optional
            Timeout for the HTTP request. Can be a single float (total timeout)
            or a tuple of (connect_timeout, read_timeout).
        \*\*constraints : any
            Additional keyword arguments that specify field constraints or
            filters. Each key-value pair represents a field name and its
            required value.

        Returns
        -------
        BVBRCResponse
            A response object (derived from the requests.Response object)
            containing the query results and associated response metadata.

        Examples
        --------
        Basic search with field constraints:

        >>> import bvbrc as bv
        >>> genome_client = bv.GenomeClient()
        >>> response = genome_client.search(species="Escherichia coli", limit=10)

        Advanced search with predicates:

        >>> response = genome_client.search(
        ...     bv.fld("genome_length") > 5000000,
        ...     bv.fld("genome_status") == "Complete",
        ...     select=["genome_id", "genome_name", "genome_length"],
        ...     sort=["+genome_length"],
        ...     limit=50
        ... )

        Or searching using the field attributes of the client object:

        >>> response = genome_client.search(
        ...     genome_client.genome_length > 5000000,
        ...     genome_client.genome_status == "Complete",
        ...     select=[
        ...         genome_client.genome_id,
        ...         genome_client.genome_name,
        ...         genome_client.genome_length
        ...     ],
        ...     sort=[+genome_client.genome_length],
        ...     limit=50
        ... )
        """

        query = RQL.RQLQuery.build(
            *predicates,
            select=select,
            sort=sort,
            limit=limit,
            start=start,
            **constraints,
        )
        return self.submit_query(query, return_format=return_format, timeout=timeout)

    def submit_query(
        self,
        query: RQL.RQLQuery,
        *,
        return_format: Union[str, ReturnFormat] = ReturnFormat.JSON,
        timeout: Optional[_Timeout] = None,
    ) -> BVBRCResponse:
        """
        Submit a pre-built RQL query to the BV-BRC API.

        This method is useful when you have already built a query using the
        `bvbrc.query` method and want to submit it with a client.

        Parameters
        ----------
        query : RQL.RQLQuery
            A pre-built RQL query object containing the search criteria, field
            selections, sorting, and other query parameters.
        return_format : str or ReturnFormat, default ReturnFormat.JSON
            The desired format for the returned data. See the
            `BV-BRC documentation <https://bv-brc.org/api/doc>`_ for allowed
            return formats.
        timeout : float or tuple, optional
            Timeout for the HTTP request. Can be a single float (total timeout)
            or a tuple of (connect_timeout, read_timeout).

        Returns
        -------
        BVBRCResponse
            A response object (derived from the requests.Response object)
            containing the query results and associated response metadata.

        Examples
        --------
        Build and submit a query:

        >>> import bvbrc as bv
        >>> q = bv.query(
        ...     bv.fld("genome_name") == "Escherichia coli",
        ...     select=["genome_id", "genome_name"],
        ...     limit=10
        ... )
        >>> client = bv.GenomeClient()
        >>> response = client.submit_query(q)

        Specify the return format:

        >>> response = client.submit_query(
        ...     q,
        ...     return_format=bv.ReturnFormat.CSV
        )
        """

        if query.no_limit:
            # TODO: figure out how to handle query with no limit (have to iteratively get all results)
            ...
        return self._exec_query(
            query.expression,
            content_type=query.content_type,
            return_format=ReturnFormat(return_format).value,
            timeout=timeout,
        )

    def _exec_query(
        self,
        query: str,
        *,
        content_type: str = "application/x-www-form-urlencoded",
        return_format: str = "application/json",
        timeout: Optional[_Timeout] = None,
    ) -> BVBRCResponse:
        """
        Execute a raw query string against the BV-BRC API.

        This is a low-level method that sends a raw query string directly to the
        BV-BRC API endpoint. It's primarily used internally by other methods, but
        can be used directly for advanced use cases where you need full control
        over the query format.

        Parameters
        ----------
        query : str
            The raw query string to send to the API. This should be properly
            formatted according to the expected API specification.
        content_type : str, default "application/x-www-form-urlencoded"
            The MIME type of the query content being sent.
        return_format : str, default "application/json"
            The MIME type of the desired response format.
        timeout : float or tuple, optional
            Timeout for the HTTP request. Can be a single float (total timeout)
            or a tuple of (connect_timeout, read_timeout).

        Returns
        -------
        BVBRCResponse
            A response object containing the query results and metadata.

        Examples
        --------
        Execute a raw RQL query:

        >>> import bvbrc as bv
        >>> client = bv.GenomeClient()
        >>> raw_query = "eq(species,Escherichia%20coli)&limit(10)"
        >>> response = client._exec_query(raw_query)
        """

        rq_response = requests.post(
            self.URL,
            data=query,
            headers={"Content-Type": content_type, "Accept": return_format},
            timeout=timeout,
        )
        return BVBRCResponse.from_response(rq_response)
