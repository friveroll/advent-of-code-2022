"""
    Day 6: Tuning Trouble
    Advent of Code 2022
    https://adventofcode.com/2022/day/6
"""


def find_start_of_packet(datastream, packet_size):
    last_n_chars = []
    for index, char in enumerate(datastream):
        last_n_chars.append(char)
        if len(last_n_chars) > packet_size:
            last_n_chars.pop(0)
        if len(set(last_n_chars)) == packet_size:
            return index + 1
    return -1


def part1(data):
    return find_start_of_packet(data, 4)


def part2(data):
    return find_start_of_packet(data, 14)


def solve():
    with open("input.txt", "r", encoding="utf-8") as reader:
        data = reader.read().strip()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    solve()
