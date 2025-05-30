bvbrc documentation
===================

Welcome to the documentation for :code:`bvbrc`!

The `Bacterial and Viral Bioinformatics Resource Center (BV-BRC)`_ is an online
resource for research in bacterial and viral infectious disease. BV-BRC provides
a `Data API`_ that can be used to request data from BV-BRC in your own
workflows.

:code:`bvbrc` is a python package that is intended to make interacting with the
BV-BRC Data API within python code feel straightfoward and intuitive.

Installation
------------

:code:`bvbrc` can be installed from PyPI using pip::

   pip install bvbrc

If you want to be able to convert the API responses to a :code:`pandas` or
:code:`polars` DataFrame, then you must also install the appropriate package::
      
      pip install pandas

or ::

      pip install polars

Contributing
------------

This project is open source and contributions are welcome! If you are interested
in contributing, please visit the `GitHub page`_ to find out more.

.. toctree::
   :hidden:
   
   quickstart
   api_reference/index
   bvbrc @ GitHub <https://github.com/abates20/bvbrc>

.. Links
.. _Bacterial and Viral Bioinformatics Resource Center (BV-BRC): https://bv-brc.org
.. _Data API: https://bv-brc.org/api
.. _GitHub page: https://github.com/abates20/bvbrc
