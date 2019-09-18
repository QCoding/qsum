# qsum: 
Intuitive and extendable checksumming for python objects

<table>
<tr>
  <td>Build Status</td>
  <td>
    <a href="https://travis-ci.org/QCoding/qsum">
    <img src="https://travis-ci.org/QCoding/qsum.svg?branch=master" alt="travis build status" />
    </a>
</tr>
<tr>
 <td>Coverage</td>
  <td>
    <a href="https://codecov.io/gh/QCoding/qsum">
    <img src="https://codecov.io/github/QCoding/qsum/coverage.svg?branch=master" alt="coverage" />
    </a>
  </td>
</tr>
</table>

## Goals
* Provide a high level checksumming toolkit for python with builtin support for common types
* Provide a framework for implementing customized checksumming logic
* Produce high quality checksums with extraordinarily low collision rates
* Build a toolkit for using and manipulating checksums
* Test it all and provide support for python 3.4, 3.5, 3.6, and 3.7

## Relationship to `__hash__`
* Respect the same contract as `__hash__` with regards to: 'The only required property is that objects which compare equal have the same hash value'
* Do not salt hash values and maintain as much stability in checksums as possible throughout python sessions, python versions, and versions of this package
* PYTHONHASHSEED should have no effect on checksums
* Provide significantly longer checksums than `__hash__` which 'is typically 8 bytes on 64-bit builds and 4 bytes on 32-bit builds'
* Represent all checksums as bytes but provide toolkits to view more human readable formats like hexdigests
* Permit the calculation of checksums on mutable objects

## Checksum Design
* The first two bytes of every checksum representing the type with functionality provided to extract it
* The rest of the checksum in a digest of the byte representation of the data

## References
[Wikipedia Checksum](https://en.wikipedia.org/wiki/Checksum)

[Python Hashlib](https://docs.python.org/3/library/hashlib.html)

[Python `__hash__`](https://docs.python.org/3/reference/datamodel.html#object.__hash__)
