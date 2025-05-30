import re
import io
import os
from typing import TYPE_CHECKING, Union, Optional

from requests import Response

from bvbrc.return_format import ReturnFormat
from bvbrc.errors import ToDataFrameError
from bvbrc._utils import requires_dep

if TYPE_CHECKING:  # Optional dependencies for type hinting
    import polars
    import pandas


class BVBRCResponse(Response):
    """
    A BVBRCResponse object.

    Inherits from requests.Response and adds some additional properties and
    methods to make interacting with a response from the BV-BRC API more
    convenient.
    """

    def __init__(self):
        super().__init__()

    @property
    def all_results_received(self) -> bool:
        """
        Whether or not all of the possible results for the query were received.

        This is based on the "Content-Range" attribute of the repsonse header.
        For example, if 0-25 results out of 100 were received, then this will be
        False. On the other hand, if 0-25 results out of 25 possible results
        were received, then this will be True.

        Whether or not all possible results are received will be based on the
        limit that was set in the submitted request. If no limit is provided
        BV-BRC has a default limit of 25. Additionally, BV-BRC seems to have a
        maximum limit of 25,000.
        """

        start, end, total = self.content_range
        return total == (end - start)

    @property
    def content_range(self) -> Optional[tuple[int, int, int]]:
        """
        The "Content-Range" attribute of the response header as a tuple of three
        integers: start index, stop index (not inclusive), and total possible
        results.

        For example, if "Content-Range" is "0-25/100" then this property will
        return a value of (0, 25, 100), which indicates that the first 25 out of
        100 possible results were received.

        If the "Content-Range" attribute is not found in the response header,
        then this property will be `None`.
        """

        content_range = self.headers.get("content-range")
        if content_range is None:
            raise None

        crange_pattern = re.compile(r"items (\d+)-(\d+)/(\d+)")
        matches = crange_pattern.findall(content_range)
        if len(matches) == 0:
            raise Exception(
                "Content range header did not match expected pattern. Expected "
                f"{repr(crange_pattern.pattern)} but got {repr(content_range)}."
            )

        return tuple(int(x) for x in matches[0])

    @property
    def return_format(self) -> Optional[ReturnFormat]:
        """
        The return format of the response content, as specified in the
        "Content-Type" header. If the "Content-Type" header is not found or does
        not contain a valid return format, then this will be `None`.
        """

        ctype_header = self.headers.get("content-type")
        if ctype_header is None:
            return None
        return ReturnFormat.extract(ctype_header)

    @requires_dep("pandas")
    def to_pandas(self) -> "pandas.DataFrame":
        """
        Convert the response content to a pandas DataFrame if possible.

        The following return formats can be converted to a pandas DataFrame:

        - JSON (application/json)
        - SOLR_JSON (application/solr+json)
        - CSV (text/csv)
        - TSV (text/tsv)
        - EXCEL (application/vnd.openxmlformats)

        Returns
        -------
        pandas.DataFrame
            The response content parsed into a pandas DataFrame.

        Raises
        ------
        ImportError
            If pandas cannot be imported.
        ToDataFrameError
            If the response content is in a format that cannot be converted to a
            pandas DataFrame.

        Examples
        --------
        Search for recently collected *E. coli* genomes and convert the response
        into a pandas DataFrame:

        >>> import bvbrc as bv
        >>> genome = bv.GenomeClient()
        >>> response = genome.search(
        ...     genome.collection_year > 2015,
        ...     species="Escherichia coli",
        ...     genome_quality="Good",
        ...     select=["genome_id", "genome_name", "collection_year", "host_name"],
        ...     limit="max",
        ...     return_format=bv.ReturnFormat.CSV
        ... )
        >>> df = response.to_pandas()
        >>> print(df.head())
            genome_id              genome_name  collection_year host_name
        0  562.160986  Escherichia coli FG92-1             2018       NaN
        1  562.160987  Escherichia coli FG31-1             2018       NaN
        2  562.160990  Escherichia coli B19429             2019       NaN
        3  562.161162   Escherichia coli 495R2             2018       Fly
        4  562.161166    Escherichia coli 520R             2018       Fly
        """

        import pandas as pd

        fmt = self.return_format  # Get the format of the response's content

        if fmt in [ReturnFormat.CSV, ReturnFormat.TSV]:
            return pd.read_csv(
                io.StringIO(self.text),
                sep="," if fmt == ReturnFormat.CSV else "\t",
                dtype={"genome_id": str},  # Make sure genome_id is parsed as string
            )

        elif fmt == ReturnFormat.JSON:
            return pd.read_json(io.StringIO(self.text))

        elif fmt == ReturnFormat.SOLR_JSON:
            solr_json: dict[str, dict] = self.json()
            dicts: dict = solr_json.get("response", {}).get("docs")
            if dicts is None:
                raise Exception("Unable to find data in SOLR JSON response.")
            return pd.DataFrame.from_records(dicts)

        elif fmt == ReturnFormat.EXCEL:
            return pd.read_excel(io.BytesIO(self.content))

        raise ToDataFrameError(fmt, "pandas")

    @requires_dep("polars")
    def to_polars(self) -> "polars.DataFrame":
        """
        Convert the response content to a polars DataFrame if possible.

        The following return formats can be converted to a polars DataFrame:

        - JSON (application/json)
        - SOLR_JSON (application/solr+json)
        - CSV (text/csv)
        - TSV (text/tsv)
        - EXCEL (application/vnd.openxmlformats)

        .. note::
            Polars would typically parse BV-BRC genome IDs as floats when
            reading a response in CSV or TSV format, so this method includes a
            schema override to force genome IDs to be parsed as strings.

        Returns
        -------
        polars.DataFrame
            The response content parsed into a polars DataFrame.

        Raises
        ------
        ImportError
            If polars cannot be imported.
        ToDataFrameError
            If the response content is in a format that cannot be converted to a
            polars DataFrame.

        Examples
        --------
        Search for recently collected *E. coli* genomes and convert the response
        into a polars DataFrame:

        >>> import bvbrc as bv
        >>> genome = bv.GenomeClient()
        >>> response = genome.search(
        ...     genome.collection_year > 2015,
        ...     species="Escherichia coli",
        ...     genome_quality="Good",
        ...     select=["genome_id", "genome_name", "collection_year", "host_name"],
        ...     limit="max",
        ...     return_format=bv.ReturnFormat.CSV
        ... )
        >>> df = response.to_polars()
        >>> print(df.head())
        shape: (5, 4)
        ┌────────────┬─────────────────────────┬─────────────────┬───────────┐
        │ genome_id  ┆ genome_name             ┆ collection_year ┆ host_name │
        │ ---        ┆ ---                     ┆ ---             ┆ ---       │
        │ str        ┆ str                     ┆ i64             ┆ str       │
        ╞════════════╪═════════════════════════╪═════════════════╪═══════════╡
        │ 562.160986 ┆ Escherichia coli FG92-1 ┆ 2018            ┆ null      │
        │ 562.160987 ┆ Escherichia coli FG31-1 ┆ 2018            ┆ null      │
        │ 562.160990 ┆ Escherichia coli B19429 ┆ 2019            ┆ null      │
        │ 562.161162 ┆ Escherichia coli 495R2  ┆ 2018            ┆ Fly       │
        │ 562.161166 ┆ Escherichia coli 520R   ┆ 2018            ┆ Fly       │
        └────────────┴─────────────────────────┴─────────────────┴───────────┘
        """

        import polars as pl

        fmt = self.return_format  # Get the format of the response's content

        if fmt in [ReturnFormat.CSV, ReturnFormat.TSV]:
            return pl.read_csv(
                io.StringIO(self.text),
                separator="," if fmt == ReturnFormat.CSV else "\t",
                schema_overrides={
                    "genome_id": str
                },  # Make sure genome_id is parsed as string
            )

        elif fmt == ReturnFormat.JSON:
            return pl.read_json(io.StringIO(self.text))

        elif fmt == ReturnFormat.SOLR_JSON:
            solr_json: dict[str, dict] = self.json()
            dicts: dict = solr_json.get("response", {}).get("docs")
            if dicts is None:
                raise Exception("Unable to find data in SOLR JSON response.")
            return pl.from_dicts(dicts)

        elif fmt == ReturnFormat.EXCEL:
            return pl.read_excel(io.BytesIO(self.content))

        raise ToDataFrameError(fmt, "polars")

    def write_file(self, filepath: Union[str, os.PathLike]):
        """
        Write the response content to the specified file path.

        Parameters
        ----------
        filepath: str | PathLike
            A path to the file where the contents of the response will be
            written to.

        Examples
        --------
        Download all the annotated protein sequences for a genome in FASTA
        format and save to a file:

        >>> import bvbrc as bv
        >>> gf = bv.GenomeFeatureClient()
        >>> response = gf.search(
        ...     genome_id="511145.12", # genome ID for a reference E. coli genome,
        ...     annotation="PATRIC", # only get PATRIC annotations (and not RefSeq ones)
        ...     feature_type="CDS", # only get coding sequence annotations
        ...     limit="max",
        ...     return_format=bv.ReturnFormat.PROTEIN_FASTA
        ... )
        >>> response.write_file("511145.12.fasta") # writes FASTA response to file
        """

        with open(filepath, "wb") as file:
            file.write(self.content)

    @classmethod
    def from_response(cls, response: Response):
        """
        Create a BVBRCResponse instance from a requests.Response object

        Parameters
        ----------
        response: requests.Response
            A requests response object that the BVBRCResponse will be created
            from.

        Returns
        -------
        BVBRCResponse
            A BVBRCResponse object containing all the properties and contents of
            the requests.Response object it was derived from.
        """

        instance = cls.__new__(cls)
        instance.__dict__.update(response.__dict__)
        return instance
