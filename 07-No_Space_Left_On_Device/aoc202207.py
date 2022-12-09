"""
    Day 7: No Space Left On Device
    Advent of Code 2022
    https://adventofcode.com/2022/day/7
"""
from collections import Counter
from pathlib import Path


def parse(filename):
    data = Path(filename).read_text()
    cwd = Path()
    dirs = Counter()
    for line in data.splitlines():
        match line.split():
            case ["$", "cd", name]:
                cwd = cwd.joinpath(name).resolve()
            case [s, name] if s.isdigit():
                for p in [cwd, *cwd.parents]:
                    dirs[p] += int(s)
    return dirs


def part1(data):
    return sum(v for v in data.values() if v <= 100_000)


def part2(data):
    rmbytes = data[Path("/")] - 70_000_000 + 30_000_000
    return min(v for v in data.values() if v >= rmbytes)


def solve(filename):
    data = parse(filename)
    return part1(data), part2(data)


if __name__ == "__main__":
    print(solve("input.txt"))
