"""Performance test that has been instrumental in collection optimizations"""

import cProfile

from qsum import checksum


def main():
    """main method"""
    long_list = list(range(0, 100000))
    print(checksum(long_list).hex())


if __name__ == "__main__":
    cProfile.run('main()')
