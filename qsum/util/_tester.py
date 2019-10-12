# pylint: disable=import-outside-toplevel
"""
Entrypoint for testing from the top-level namespace
# pattern is from https://github.com/pandas-dev/pandas/blob/master/pandas/util/_tester.py
"""
import os
import sys

PKG = os.path.dirname(os.path.dirname(__file__))


def test(extra_args=None) -> None:
    """
    Run the test suite for qsum
    Args:
        extra_args: additional args to pass to pytest

    Returns: None
    """
    try:
        import pytest
    except ImportError:
        raise ImportError("Need pytest to run tests")
    cmd = []  # type: list
    if extra_args:
        if not isinstance(extra_args, list):
            extra_args = [extra_args]
        cmd = extra_args
    cmd += [PKG]
    print("running: pytest {}".format(" ".join(cmd)))
    sys.exit(pytest.main(cmd))


__all__ = ["test"]
