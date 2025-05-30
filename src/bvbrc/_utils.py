import functools
from copy import deepcopy
from types import ModuleType
import importlib


def copy_self(func):
    """
    Decorator for bound methods that passes in a deepcopy of the instance
    instead of the instance itself.
    """

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        return func(deepcopy(self), *args, **kwargs)

    return wrapper


def url_encode(string: str, /):
    """
    Format the string for placement in a url.

    Currently just replaces spaces with '+'.
    """
    return string.replace(" ", "+")


def import_optional_dep(name: str) -> ModuleType:
    """
    Import an optional dependency, raising an ImportError with an informative
    message if the dependency is missing.

    This was based on the `import_optional_dependency` function in the
    [pandas source code](https://github.com/pandas-dev/pandas).

    Raises
    ------
    ImportError
        If the dependency to be imported is not found.
    """

    msg = (
        f"Missing optional dependency {name}. "
        f"Please install {name} (with pip/conda/etc.)"
    )
    try:
        module = importlib.import_module(name)
    except ImportError as err:
        raise ImportError(msg) from err
    else:
        return module


def requires_dep(name: str):
    """
    Creates a decorator that imports the specified optional dependency before
    calling the decorated function.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import_optional_dep(name)
            return func(*args, **kwargs)

        return wrapper

    return decorator
