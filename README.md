# bvbrc

The [Bacterial and Viral Bioinformatics Resource Center (BV-BRC)](https://bv-brc.org)
is an online resource for research in bacterial and viral infectious disease.
BV-BRC provides a [Data API](https://bv-brc.org/api) that can be used to request
data from BV-BRC in your own workflows.

`bvbrc` is a python package that is intended to make interacting with the BV-BRC
Data API within python code feel straightfoward and intuitive. Please reference
the [bvbrc documentation](https://bvbrc.readthedocs.io) for help using `bvbrc`.

## Installation

`bvbrc` can be installed from PyPI using pip:

```shell
pip install bvbrc
```

If you want to be able to convert the API responses to a `pandas` or `polars`
DataFrame, then you must also install the appropriate package:

```shell
pip install pandas
```

or

```shell
pip install polars
```

## Contributing

This project is open source and contributions are welcome! If you are interested
in contributing, please take a look at the [contributing guidelines][contributing].

[contributing]: https://github.com/abates20/bvbrc/blob/main/.github/CONTRIBUTING.md
