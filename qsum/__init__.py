# import useful core modules to the top level package
from qsum.core import exceptions
# certain constants will be commonly used
from qsum.core.cache import qsum_version
from qsum.core.constants import DependsOn
# import the most common core functions to the top level package
from qsum.core.logic import checksum, checksum_hex, Checksum, is_supported_type
# it should always be easy to run tests, which are shipped with the qsum package
from qsum.util._tester import test

__version__ = qsum_version()
