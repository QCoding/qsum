# pylint: disable=import-outside-toplevel
"""
Entrypoint for testing from the top-level namespace
# pattern is from https://github.com/pandas-dev/pandas/blob/master/pandas/util/_tester.py
"""
import os
import sys

import typing

PKG = os.path.dirname(os.path.dirname(__file__))

DEFAULT_ARGS = ["--cov-report=term-missing", "--cov=qsum", "-n=auto", "--mypy", "--pylint"]


def test(use_default_args: bool = True, extra_args: typing.Union[str, list] = None) -> None:
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
    cmd = DEFAULT_ARGS if use_default_args else []
    if extra_args:
        if not isinstance(extra_args, list):
            extra_args = [extra_args]
        cmd = extra_args
    cmd += [PKG]
    print("running: pytest {}".format(" ".join(cmd)))
    sys.exit(pytest.main(cmd))


__all__ = ["test"]
