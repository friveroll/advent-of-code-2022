import re


def parser(filename):
    with open(filename, "r", encoding="utf-8") as reader:
        out = []
        for line in reader:
            a, b, c, d = map(int, re.findall(r"\d+", line))
            out.append(
                (
                    set(range(a, b + 1)),
                    set(range(c, d + 1)),
                )
            )
    return out


def is_contained_in(a, b):
    return a.issubset(b) or a.issuperset(b)


def is_overlapped(a, b):
    return len(a.intersection(b)) > 0 or len(b.intersection(a)) > 0


def part1(data):
    out = 0
    for item in data:
        if is_contained_in(item[0], item[1]) or is_contained_in(
            item[1], item[0]
        ):
            out += 1
    return out


def part2(data):
    out = 0
    for item in data:
        if is_overlapped(item[0], item[1]):
            out += 1
    return out


def solve(filename):
    data = parser(filename)
    return part1(data), part2(data)


if __name__ == "__main__":
    print(solve("input.txt"))
