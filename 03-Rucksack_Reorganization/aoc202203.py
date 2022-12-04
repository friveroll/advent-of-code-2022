""" Day 3: Rucksack Reorganization
   https://adventofcode.com/2020/day/3  """

import string


def parse(filename):
    """Parse the input file into a list of tuples."""
    return [
        line.strip()
        for line in open(filename, "r", encoding="utf-8").readlines()
    ]


def split_items(data):
    """Split the items into two lists."""
    out = []
    for item in data:
        out.append((item[: len(item) // 2], item[len(item) // 2 :]))
    return out


def group_by_3(data):
    """Group the data by 3."""
    return list(zip(*(iter(data),) * 3))


def get_unique_letter(data):
    """Return the unique letters in a string."""
    return "".join(set(data[0]).intersection(data[1]))


def common_between_3(data):
    """Return the common letters between 3 strings."""
    return "".join(set(data[0]).intersection(data[1], data[2]))


def get_priority(letter):
    """Return the priority of a letter."""
    return string.ascii_letters.index(letter) + 1


def part1(data):
    """Return the solution to part 1."""
    data = split_items(data)
    unique_letters = [get_unique_letter(item) for item in data]
    return sum([get_priority(letter) for letter in unique_letters])


def part2(data):
    """Return the solution to part 2."""
    data = group_by_3(data)
    unique_letters = [common_between_3(item) for item in data]
    return sum([get_priority(letter) for letter in unique_letters])


def solve():
    """Solve the puzzle."""
    data = parse("input.txt")
    return part1(data), part2(data)


if __name__ == "__main__":
    print(solve())
