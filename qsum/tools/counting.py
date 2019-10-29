import typing
from collections import defaultdict

from qsum.types.type_logic import checksum_to_type


def count_types(checksums: typing.Iterable) -> defaultdict:
    """For the given checksums collection count the number of times each type occurs

    Args:
        checksums:

    Returns:
    >>> from qsum import checksum
    >>> counts = count_types(list(map(checksum, [1,2,3,'a','b','c','d', 5.5, 6.6])))
    >>> counts[int], counts[str], counts[float]
    (3, 4, 2)
    """
    # default all types to 0
    type_by_count = defaultdict(int)
    checksums_iter = iter(checksums)
    for checksum_value in checksums_iter:
        type_by_count[checksum_to_type(checksum_value)] += 1

    return type_by_count
