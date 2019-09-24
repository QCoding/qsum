import operator
from functools import reduce

from qsum.core.constants import BYTES_IN_PREFIX, CONTAINER_TYPES, MAPPABLE_CONTAINER_TYPES
from qsum.data import data_checksum
from qsum.types.logic import checksum_to_type, type_checksum


def checksum(obj) -> bytes:
    """Generate a checksum for a given object based on it's type and contents

    Args:
        obj: object to generate a checksum for

    Returns:
        checksum bytes

    >>> from qsum import checksum
    >>> checksum('a nice word').hex()
    '000177bdb96414925834c784c7497b14ca73a7ecead6d0542a5666bcb0598813bf9d'
    >>> checksum(('a', 'nice', 'word')).hex()
    '010086eb00a39e1bd72ae55e30fc9638b12803a495b0e45f54fba9438d60e3310e9a'
    """
    obj_type = type(obj)
    return _checksum(obj, obj_type, obj_type)


def _checksum(obj, obj_type, checksum_type) ->bytes:
    """Checksum the given object of the given type

    Args:
        obj: object to checksum
        obj_type: the type of logic to use for checksumming the data
        checksum_type:
            the type to use for the checksum prefix, useful when the process of checksumming one object involves
             transforming the data to another type but we want to return the original object type

    Returns:
        checksum bytes

    """
    # Handle containers with multiple objects that need to be individual checksummed and then combined
    if obj_type in CONTAINER_TYPES:
        if obj_type in MAPPABLE_CONTAINER_TYPES:
            # compute the checksums of the elements of the mappable collection and build up a byte array
            # we are capturing the type and data checksums of all of the elements here
            checksum_bytes = reduce(operator.add, map(checksum, obj), bytearray())

            # let's use the container type for the type_checksum but tell the data_checksum to use the bytes logic
            return type_checksum(checksum_type) + data_checksum(checksum_bytes, bytes)

        if obj_type == dict:
            # for dictionaries we need to stable sort the keys then get the values in that order
            # when sorting the k,v tuples sorted should only be considering the k since no two keys should be equal
            # if that is not the case then the odd behavior of sorting on the value will occur
            # sorted(obj.items()) returns a list of tuples, which we already how to checksum
            # obj_type=dict for the prefix, but we're pass list to the data_checksum as we've extracted list like data
            return _checksum(sorted(obj.items()), list, obj_type)
    else:
        # For a simple object combine the type with the data checksum
        return type_checksum(checksum_type) + data_checksum(obj, obj_type)


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
