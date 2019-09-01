class QSumException(Exception):
    pass


class QSumInvalidDataTypeException(QSumException):
    pass


class QSumInvalidTypeException(QSumException):
    pass


class QSumInvalidPrefixException(QSumException):
    pass


class QSumStaticLookupMissException(QSumException):
    """Based on the type value was expected to have a static checksum but it failed to"""
    pass
