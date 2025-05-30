"""
Errors module
-------------

Defines custom error types for the bvbrc package.
"""

__all__ = ["BVBRCError", "ToDataFrameError"]


from bvbrc.return_format import ReturnFormat


class BVBRCError(Exception):
    """
    The base BVBRCError class that all other bvbrc errors inherit from.
    """

    pass


class ToDataFrameError(BVBRCError):
    """
    An error caused by trying to convert a response to a DataFrame when the
    format of the response contents cannot be converted to a DataFrame.
    """

    def __init__(self, return_format: ReturnFormat, df_module: str):
        msg = f"{return_format} cannot be converted to a {df_module} DataFrame."
        super().__init__(msg)
