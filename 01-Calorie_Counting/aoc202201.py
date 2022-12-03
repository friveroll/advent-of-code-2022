""" Day 1: Calorie Counting
    advent of code 2022"""


def parse(filename):
    with open(filename, encoding="utf-8") as fp:
        return [
            [int(number) for number in element.split("\n")]
            for element in fp.read().split("\n\n")
        ]


def part1(data):
    return max(
        [
            sum(element) if isinstance(element, list) else element
            for element in data
        ]
    )


def part2(data):
    return sum(
        sorted(
            [
                sum(element) if isinstance(element, list) else element
                for element in data
            ],
            reverse=True,
        )[:3]
    )


def solve(filename):
    data = parse(filename)
    return part1(data), part2(data)


if __name__ == "__main__":
    print(solve("input.txt"))
