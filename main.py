"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(dict.fromkeys(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    sort_order = "asc"
    if len(sys.argv) in (3, 4):
        filename = sys.argv[1]

        duplicate_option = sys.argv[2].lower()
        if duplicate_option not in ["yes", "no"]:
            print("The second argument must be 'yes' or 'no'")
            sys.exit(1)
        remove_duplicates = duplicate_option == "yes"

        if len(sys.argv) == 4:
            sort_order = sys.argv[3].lower()
            if sort_order not in ("asc", "desc"):
                print("The third argument must be 'asc' or 'desc'")
                sys.exit(1)
    else:
        print("The first argument must specify the input file")
        print("The second argument specifies whether to remove duplicates")
        print("The third argument (optional) specifies the order: asc or desc")
        sys.exit(1)

    print(f"Words will be read from file {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"File {filename} does not exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list, ascending=(sort_order == "asc")))