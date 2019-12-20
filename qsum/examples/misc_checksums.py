# pylint: disable=missing-function-docstring
"""Just a bunch of misc python objects to checksum"""

import random

from qsum import Checksum


def foo_function():
    pass


def foo_function2():
    """A nice function"""


def main():
    obj = {
        'a': list(range(1, 100)),
        1: random.random(),
        (5, 7): {0.1, 0.2, 0.3},
        1.5: frozenset({1, 2, 3}),
        'd': (foo_function, foo_function2),  # tuple of functions, getting fun ha?
        'random': random,  # yes the entire module,
    }
    check = Checksum(obj)
    print(check.hex())  # this will change between python versions since we're checksumming the random module


if __name__ == "__main__":
    main()
