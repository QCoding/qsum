import operator
from functools import reduce

from qsum.core.constants import BYTES_IN_PREFIX, CONTAINER_TYPES, MAPPABLE_CONTAINER_TYPES
from qsum.data import data_checksum
from qsum.types.logic import checksum_to_type, type_checksum


def checksum(obj):
    """Generate a checksum for a given object based on it's type and contents

    Args:
        obj: object to generate a checksum for

    Returns:
        string representing a checksum of the object

    >>> from qsum import checksum
    >>> checksum('a nice word').hex()
    '000177bdb96414925834c784c7497b14ca73a7ecead6d0542a5666bcb0598813bf9d'
    >>> checksum(('a', 'nice', 'word')).hex()
    '010086eb00a39e1bd72ae55e30fc9638b12803a495b0e45f54fba9438d60e3310e9a'
    """
    # let's just call this once
    obj_type = type(obj)

    if obj_type in CONTAINER_TYPES:
        if obj_type in MAPPABLE_CONTAINER_TYPES:
            # compute the checksums of the elements of the mappable collection and build up a byte array
            # we are capturing the type and data checksums of all of the elements here
            checksum_bytes = reduce(operator.add, map(checksum, obj), bytearray())

            # let's use the container type for the type_checksum but tell the data_checksum to use the bytes logic
            return type_checksum(obj_type) + data_checksum(checksum_bytes, bytes)
    else:
        # For a simple object combine the type with the data checksum
        return type_checksum(obj_type) + data_checksum(obj, obj_type)


class Checksum:
    """Class for working with checksums

    All manipulations of checksums should utilize this class
    """

    @classmethod
    def checksum(cls, obj):
        """Generate the checksum and wrap in a Checksum object"""
        return Checksum(checksum(obj))

    def __init__(self, checksum_bytes):
        self._checksum_bytes = checksum_bytes

    @property
    def type(self):
        return checksum_to_type(self._checksum_bytes)

    @property
    def checksum_bytes(self):
        return self._checksum_bytes

    def hex(self):
        return self._checksum_bytes.hex()

    def __repr__(self):
        """Use the hexdigest as repr is a string so the bytes are actually a less efficient representation"""
        return 'Checksum({})'.format(self.hex())

    def __eq__(self, other):
        """Equality is determined by comparing the raw bytes of the checksum"""
        return self._checksum_bytes == other.checksum_bytes

    def __str__(self):
        """Use the hex digest and get the type name for the nicer representation"""
        # The first BYTES_IN_PREFIX * 2 (since we're going from bytes to hex) are the type prefix
        # we remove this prefix from the hexdigest as we're displaying the human readable version beforehand
        return 'Checksum({}:{})'.format(checksum_to_type(self._checksum_bytes).__name__,
                                        self.hex()[BYTES_IN_PREFIX * 2:])
