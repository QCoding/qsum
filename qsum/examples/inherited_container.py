# pylint: disable=missing-function-docstring,missing-class-docstring
from qsum import Checksum


class CustomDict(dict):
    def sorted_keys(self):
        return sorted(self.keys())


def main():
    my_custom_dict = CustomDict()
    my_custom_dict['b'] = 1
    my_custom_dict['a'] = 2

    print(Checksum(my_custom_dict).hex())


if __name__ == "__main__":
    main()
