# pylint: disable=missing-function-docstring,missing-class-docstring
from qsum import Checksum


def main():
    with_versions = Checksum("abc", depends_on=('wheel', 'setuptools'))
    print(with_versions.hex())


if __name__ == "__main__":
    main()
