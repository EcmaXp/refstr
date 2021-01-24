"""refstr: Referenceable String"""

__all__ = ["refstr"]

from typing import Generic, TypeVar

T = TypeVar('T')


class refstr(Generic[T], str):
    """
    refstr[...] -> import path (eg. sys.version, sys:version)
    refstr[T] -> attribute for T

    A referenceable string.
    """
    pass
