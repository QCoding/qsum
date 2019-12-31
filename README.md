# qsum: Python checksumming toolkit
Intuitive and extendable checksumming for python objects

<table>
<tr>
  <td>Latest Release</td>
  <td>
    <a href="https://anaconda.org/qcoding/qsum">
    <img src="https://anaconda.org/qcoding/qsum/badges/version.svg?update=1" alt="Anaconda Cloud"/>
    </a>
  </td>
</tr>
<tr>
  <td>Build Status</td>
  <td>
    <a href="https://travis-ci.com/QCoding/qsum">
    <img src="https://travis-ci.com/QCoding/qsum.svg?branch=master" alt="travis build status" />
    </a>
  </td>
</tr>
<tr>
 <td>Coverage</td>
  <td>
    <a href="https://codecov.io/gh/QCoding/qsum">
    <img src="https://codecov.io/github/QCoding/qsum/coverage.svg?branch=master" alt="coverage" />
    </a>
  </td>
</tr>
<tr>
<td>License</td>
<td>
  <a href="https://opensource.org/licenses/MIT">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="license" />
  </a>
</td>
</tr>
<tr>
<td>Downloads</td>
<td>
  <a href="https://anaconda.org/qcoding/qsum">
  <img src="https://anaconda.org/qcoding/qsum/badges/downloads.svg" alt="downloads" />
  </a>
</td>
</tr>
<tr>
<td>Platforms</td>
<td>
  <a href="https://anaconda.org/qcoding/qsum">
  <img src="https://anaconda.org/qcoding/qsum/badges/platforms.svg" alt="noarch" />
  </a>
</td>
</tr>
</table>


## Goals
* Provide a checksumming toolkit for python with out of the box support for common types
* Architect a framework for implementing customized checksumming logic
* Produce high quality checksums with extraordinarily low collision rates
* Build a toolkit for using and manipulating checksums
* Test it all with 100% coverage and support python 3.5, 3.6, 3.7 and 3.8

## Where to get it
Source code is available on github: https://github.com/QCoding

Install with conda:
```
# add the QCoding Channel
conda config --append channels QCoding
# install the latest version of QSum
conda install qsum
```

## How to use it
```
# Functional Interface
from qsum import checksum
checksum('abc')

# Class Interface
from qsum import Checksum
Checksum('abc').checksum_bytes
```

## Design
* QSUM CHECKSUM = TYPE PREFIX + DATA CHECKSUM 
    * The first two bytes of every checksum represent the type and will be referred to as the 'type prefix'
    * The rest of the checksum in a digest of the byte representation of the object and will be refered to as the 'data checksum'

### Relationship to `__hash__`
* Respect the same contract as `__hash__` with regards to: 'The only required property is that objects which compare equal have the same hash value'
* Do not salt hash values (unless requested) and maintain as stability in checksums throughout python sessions, python versions, and versions of this package
* PYTHONHASHSEED should have no effect on checksums
* Provide significantly longer checksums than `__hash__` which 'is typically 8 bytes on 64-bit builds and 4 bytes on 32-bit builds'
* Represent all checksums as bytes but provide a toolkit to view more human readable formats like hexdigests
* Base checksums on object contents and permit the calculation of checksums on mutable objects

### Adding Salt
* By default the environment is not included in the checksum but individual package versions can be included if the package name is added via the depends_on argument
* To include the entire python environment in the checksum:
    ```
    from qsum import checksum, DependsOn
    checksum('abc', depends_on=DependsOn.PythonEnv)
    ```

## Type Support
* The great majority of [Built-in Types](https://docs.python.org/3.7/library/stdtypes.html) including collections are checksummable
    * _int, float, str, bytes, tuple, list, dict, set, etc._
* Common types have registered type prefixes which can be used to recover the type from the checksum

###  Custom Containers
* Custom container classes that inherit from common python containers _(E.g. tuple, list, set, dict)_ are checksummable
* The class name is not recoverable from the type prefix but will be added as salt to the data checksum to prevent collisions

### Functions and Modules
* Functions are checksummed based on a combination of their source code, attributes and module location
* Modules are checksummed simply based on the hash of their source code

### Files
* When passed an open file handle qsum will include all the bytes of the file in the checksum calculation

## References
[Wikipedia Checksum](https://en.wikipedia.org/wiki/Checksum)

[Python Hashlib](https://docs.python.org/3/library/hashlib.html)

[Python `__hash__`](https://docs.python.org/3/reference/datamodel.html#object.__hash__)

[What Happens When You Mess With Hashing In Python](https://www.asmeurer.com/blog/posts/what-happens-when-you-mess-with-hashing-in-python/)
