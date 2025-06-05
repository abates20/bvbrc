Quickstart
==========

This guide will go through some of the basic functionality in :code:`bvbrc`. If
you are unfamiliar with the data in BV-BRC or the BV-BRC Data API, it may be
useful to consult the `BV-BRC documentation <https://www.bv-brc.org/docs/>`_ and
the `BV-BRC API documentation <https://www.bv-brc.org/api/doc/>`_.

Installation
------------

:code:`bvbrc` can be installed from PyPI using pip::

   pip install bvbrc

If you want to be able to convert the API responses to a :code:`pandas` or
:code:`polars` DataFrame, then you must also install the appropriate package:

|

.. tabs::

      .. tab:: pandas

            ::

                  pip install pandas

      .. tab:: polars

            ::

                  pip install polars

Basic Usage
-----------

.. note::

      The outputs from the code snippets below were run with BV-BRC version
      3.49.1 so the outputs may differ if you run the code snippets with a
      different version of BV-BRC.

Import the package in your Python code:

.. code-block:: python
      
      import bvbrc as bv

:code:`bvbrc` has a client object for each of the main data types in BV-BRC. You
can retrieve data of a specific type by using the corresponding client. For
example, to get data for genomes on BV-BRC, initialize the :code:`GenomeClient`:

.. code-block:: python

      genome_client = bv.GenomeClient()

Each client offers three main methods for retrieving data: :code:`get`,
:code:`search`, and :code:`submit_query`. All three of these methods return a
BVBRCResponse object. 

Retrieving single records
~~~~~~~~~~~~~~~~~~~~~~~~~

The :code:`get` method is for retreiving a single record of the desired data
type based on its ID. For example, with the :code:`GenomeClient`, you can get a
single genome entry from BV-BRC if you know its genome_id:

.. code-block:: python

      response = genome_client.get("1313.5458")
      print(response)

Output::
      
      <Response [200]>

The response code :code:`200` is an 'OK' response meaning that your request
did not encounter any errors. If you requested the data in the default
'application/json' format, then the retreived data can then be accessed in a
dictionary by calling :code:`response.json()`.

.. code-block:: python

      genome_data = response.json() # Returns a dictionary with the retrieved data
      print(genome_data.get("genome_id"))
      print(genome_data.get("species"))

Output::

      1313.5458
      Streptococcus pneumoniae

Searching BV-BRC with queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alternatively, you can use queries to search for and retrieve data on BV-BRC in
a more powerful and flexible way using the :code:`search` method. This method
allows the user to provide constraints, select which fields are returned, and
even sort the returned data. For example, using the :code:`GenomeClient`, you
can retrieve all genomes for *E. coli* where the genome_status is "Complete":

.. code-block:: python

      response = genome_client.search(
            genome_client.species == "Escherichia coli",
            genome_client.genome_status == "Complete"
      )
      start, end, total_results = response.content_range
      print(f"{end - start} out of {total_results} total results were retrieved.")

Output::

      25 out of 4495 total results were retrieved.

You'll notice that even though 4495 results met the search parameters, only 25
were returned. This is because BV-BRC has a default limit of 25 on how many
results are returned for one query. Consequently, getting the remaining results
requires either sending multiple requests and adjusting the starting point each
time or simply increasing the limit:

.. tip::

      Whenever you specify the starting index of the returned results, you also
      should specify the limit even if you want to get the default 25 results.

.. code-block:: python

      # Get the next 25 results
      next_response = genome_client.search(
            genome_client.species == "Escherichia coli",
            genome_client.genome_status == "Complete",
            limit=25, # Set the limit to return 25 results
            start=25, # Return results starting at index 25
      )
      start, end, total_results = next_response.content_range
      print(f"Results {start}-{end} out of {total_results} total results were retrieved.")

Output::

      Results 25-50 out of 4495 total results were retrieved.

You can also specify :code:`limit="max"` to set the limit to the maximum allowed
which is currently 25,000.

.. code-block:: python

      response = genome_client.search(
            genome_client.species == "Escherichia coli",
            genome_client.genome_status == "Complete",
            limit="max"
      )
      start, end, total_results = response.content_range
      print(f"Results {start}-{end} out of {total_results} total results were retrieved.")

Output::

      Results 0-4495 out of 4495 total results were retrieved.

Accessing retrieved data
~~~~~~~~~~~~~~~~~~~~~~~~

Since searches can retreive multiple results, calling :code:`response.json()`
returns a list of dictionaries instead of a single dictionary. Each dictionary
contains the data for one of the retrieved results (similar to the dictionary
from the :code:`get` method).

.. code-block:: python

      response = genome_client.search(
            genome_client.species == "Escherichia coli",
            genome_client.genome_status == "Complete",
            select=["genome_id", "species", "genome_status"] # Select fields to return
      )
      results = response.json()
      print("Type of the results:", type(results))
      print(len(results), "results returned")

      # Print the dictionary for the first result
      print("First result:", results[0])

Output::

      Type of the results: <class 'list'>
      25 results returned
      First result: {'genome_id': '562.160986', 'species': 'Escherichia coli', 'genome_status': 'Complete'}

Alternatively, the :code:`BVBRCResponse` object also provides methods for
converting the retrieved results into either a :code:`pandas` or :code:`polars`
DataFrame. This can be especially useful when trying to work with lots of
results and wanting to work with these results in a table-like format.

|

.. tabs::

      .. tab:: pandas

            .. code-block:: python

                  df = response.to_pandas()
                  print(df.head())

            |

            Output::

                      genome_id           species genome_status
                  0  562.160986  Escherichia coli      Complete
                  1  562.160987  Escherichia coli      Complete
                  2  562.160990  Escherichia coli      Complete
                  3  562.161161  Escherichia coli      Complete
                  4  562.161188  Escherichia coli      Complete

      .. tab:: polars

            .. code-block:: python

                  df = response.to_polars()
                  print(df.head())
            
            |

            Output::

                  shape: (5, 3)
                  ┌────────────┬──────────────────┬───────────────┐
                  │ genome_id  ┆ species          ┆ genome_status │
                  │ ---        ┆ ---              ┆ ---           │
                  │ str        ┆ str              ┆ str           │
                  ╞════════════╪══════════════════╪═══════════════╡
                  │ 562.160986 ┆ Escherichia coli ┆ Complete      │
                  │ 562.160987 ┆ Escherichia coli ┆ Complete      │
                  │ 562.160990 ┆ Escherichia coli ┆ Complete      │
                  │ 562.161161 ┆ Escherichia coli ┆ Complete      │
                  │ 562.161188 ┆ Escherichia coli ┆ Complete      │
                  └────────────┴──────────────────┴───────────────┘

Need Help?
----------

If you encounter issues, please open an issue on GitHub or consult the
:doc:`API Reference <api_reference/index>`.
