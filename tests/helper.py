"""Collection of useful helpers
"""
from contextlib import contextmanager


@contextmanager
def not_raises(exc):
    try:
        yield
    except exc as error:
        raise AssertionError(f"Raised exception {error} when it should not!")
    except Exception as error:
        raise AssertionError(f"An unexpected exception {error} was raised.")
