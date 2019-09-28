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
