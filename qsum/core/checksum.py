import binascii
import sys

from qsum.core.constants import BYTES_IN_PREFIX
from qsum.data import data_checksum
from qsum.types.logic import checksum_to_type, type_checksum


def checksum(obj):
    """Generate a checksum for a given object based on it's type and contents

    Args:
        obj: object to generate a checksum for

    Returns:
        string representing a checksum of the object

    >>> from qsum import checksum
    >>> c = checksum('a nice word')
    >>> len(c)
    34
    """
    # let's just call this once
    obj_type = type(obj)

    # Combine the type with the data checksum
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

    def hexdigest(self):
        if sys.version_info < (3, 5):
            return binascii.hexlify(self._checksum_bytes).decode()
        else:
            return self._checksum_bytes.hex()

    def __repr__(self):
        """Use the hexdigest as repr is a string so the bytes are actually a less efficient representation"""
        return 'Checksum({})'.format(self.hexdigest())

    def __eq__(self, other):
        """Equality is determined by comparing the raw bytes of the checksum"""
        return self._checksum_bytes == other.checksum_bytes

    def __str__(self):
        """Use the hex digest and get the type name for the nicer representation"""
        # The first BYTES_IN_PREFIX * 2 (since we're going from bytes to hex) are the type prefix
        # we remove this prefix from the hexdigest as we're displaying the human readable version beforehand
        return 'Checksum({}:{})'.format(checksum_to_type(self._checksum_bytes).__name__, self.hexdigest()[BYTES_IN_PREFIX * 2:])
