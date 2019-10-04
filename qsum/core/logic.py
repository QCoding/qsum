import functools
import operator
from functools import reduce

from qsum.core.constants import BYTES_IN_PREFIX, CONTAINER_TYPES, MAPPABLE_CONTAINER_TYPES, DEFAULT_HASH_ALGO, \
    UNORDERED_CONTAINER_TYPES
from qsum.core.exceptions import QSumUnhandledContainerType
from qsum.data import data_checksum
from qsum.types.type_logic import checksum_to_type, type_to_prefix
from qsum.types.type_map import TYPE_TO_PREFIX


def checksum(obj, hash_algo=DEFAULT_HASH_ALGO) -> bytes:
    """Generate a checksum for a given object based on it's type and contents

    Args:
        obj: object to generate a checksum of
        hash_algo: the hash algorithm to use to convert the bytes to a message digest

    Returns:
        checksum bytes representing the object's type and a message digest of the data

    >>> from qsum import checksum
    >>> checksum('a nice word').hex()
    '000177bdb96414925834c784c7497b14ca73a7ecead6d0542a5666bcb0598813bf9d'
    >>> checksum(('a', 'nice', 'word')).hex()
    '010086eb00a39e1bd72ae55e30fc9638b12803a495b0e45f54fba9438d60e3310e9a'
    >>> checksum({'a': 1, 'nice': 2, 'word': 3}).hex()
    '0103ed71fada8381439167d30ca1310e87af60e8f41e1fa320e0f626775f5b8cd908'
    """
    obj_type = type(obj)
    return _checksum(obj, obj_type, obj_type, hash_algo)


def _checksum(obj, obj_type, checksum_type, hash_algo) -> bytes:
    """Checksum the given obj, assuming it's of obj_type and return a checksum of type checksum_type

    Args:
        obj: object to checksum
        obj_type: the type of logic to use for checksumming the data
        checksum_type:
            the type to use for the checksum prefix, useful when the process of checksumming one object involves
            transforming the data to another type but we want to return the original object type
        hash_algo: the hash algorithm to use to convert the bytes to a message digest

    Returns:
        checksum bytes

    """
    # Handle containers with multiple objects that need to be individual checksummed and then combined
    if obj_type in CONTAINER_TYPES:
        if obj_type in MAPPABLE_CONTAINER_TYPES:
            checksum_func_with_args = functools.partial(checksum, hash_algo=hash_algo)
            if obj_type in UNORDERED_CONTAINER_TYPES:
                # compute the checksums and sort the checksums as we don't trust native python sorting across types
                checksum_bytes = reduce(operator.add, sorted(map(checksum_func_with_args, obj)), bytearray())
            else:
                # compute the checksums of the elements of the mappable collection and build up a byte array
                # we are capturing the type and data checksums of all of the elements here
                # container types that hit this logic should have a predicable iteration order
                checksum_bytes = reduce(operator.add, map(checksum_func_with_args, obj), bytearray())

            # let's use the container type for the type_checksum but tell the data_checksum to use the bytes logic
            return type_to_prefix(checksum_type) + data_checksum(checksum_bytes, bytes, hash_algo)

        if obj_type == dict:
            # obj.items() returns dict_items which appear list like but in fact we don't want to trust the stability
            # of the order of the items, so let's treat it like an unordered set (no need to actually make it a set,
            # in fact that may cause issues if the values aren't hashable, i.e. dict of dicts) and use the sort of the
            # checksums as our method for stabilizing the overall checksum of the object
            # for python 3.7 this means that even though dicts are ordered, we will ignore that order, this is a design
            # decision and may need to be re-visited/potentially have an option to pick the methodology
            return _checksum(obj.items(), set, obj_type, hash_algo=hash_algo)

        raise QSumUnhandledContainerType("{} has no checksumming implementation available".format(obj_type))

    # For a simple object combine the type with the data checksum
    return type_to_prefix(checksum_type) + data_checksum(obj, obj_type, hash_algo)


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
    def type(self) -> type:
        """type of the checksum"""
        return checksum_to_type(self._checksum_bytes)

    @property
    def checksum_bytes(self) -> bytes:
        """The raw bytes of the checksum"""
        return self._checksum_bytes

    def hex(self) -> str:
        """The hex representation of the checksum"""
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


def is_supported_type(the_type: type) -> bool:
    """
    Determine if the given type is supported by checking against the prefix map
    Args:
        the_type: type to check

    Returns:
        Whether the given type is checksummable
    """
    return the_type in TYPE_TO_PREFIX
