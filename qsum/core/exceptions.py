class QSumException(Exception):
    """Base exception class for QSum"""


class QSumInvalidDataTypeException(QSumException):
    """Indicates an invalid data type was hit"""


class QSumInvalidTypeException(QSumException):
    """Indicates an invalid type was hit"""


class QSumInvalidPrefixException(QSumException):
    """Indicates an invalid type prefix was hit"""


class QSumStaticLookupMissException(QSumException):
    """Based on the type value was expected to have a static checksum but it failed to"""


class QSumUnhandledContainerType(QSumException):
    """An un-supported container type has been used"""


class QSumInvalidChecksum(QSumException):
    """Where a checksum like object was expected an invalid object was given"""


class QSumInvalidDependsOn(QSumException):
    """Invalid type of value passed to depends on"""


class QSumInvalidBytesDataType(QSumException):
    """Invalid type of bytes data, must be bytes, bytearray
    or a valid generator that produces bytes or bytearray values"""


class QSumUnknownVersionDependency(QSumException):
    """QSum version is being added via DependsOn but the package version can not be resolved,
    this may happen if you are running qsum locally and not via a conda installation"""
