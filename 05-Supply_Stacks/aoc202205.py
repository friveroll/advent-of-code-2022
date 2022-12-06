"""
    Day 5: Supply Stacks
    Advent of Code 2022
    https://adventofcode.com/2022/day/5
"""
import re
from collections import deque


def parser(filename):
    with open(filename, "r", encoding="utf-8") as reader:
        stacks, procedure = [
            list_.split("\n") for list_ in reader.read().split("\n\n")
        ]
        number_of_stacks = (int(len(stacks[0])) + 1) // 4
        result = {i: [] for i in range(1, number_of_stacks + 1)}
        pattern = re.compile(r"\[([A-Z])\]")

        for stack in stacks:
            positions = [m.start(0) + 1 for m in re.finditer(pattern, stack)]
            for position in positions:
                j = ((position - 1) // 4) + 1
                result[j].append(stack[position])
        list_of_procedures = []
        step_pattern = re.compile(r"move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)")
        for step in procedure:
            list_of_procedures.extend(
                [[int(s) for s in re.findall(step_pattern, step)[0]]]
            )
    return [v for v in result.values()], list_of_procedures


def crate_mover_9000(
    list_of_stacks: list, number_of_items: int, from_stack: int, to_stack: int
) -> list:
    """Return a list with the moves from procedure from part 1"""
    items_to_move = []
    for _ in range(number_of_items):
        items_to_move.append(list_of_stacks[from_stack - 1].pop(0))
    items_to_move.reverse()
    for index, item in enumerate(items_to_move):
        list_of_stacks[to_stack - 1].insert(index, item)
    return list_of_stacks


def crate_mover_9001(
    list_of_stacks: list, number_of_items: int, from_stack: int, to_stack: int
) -> list:
    """Return a list with the moves from procedure from part 2"""
    items_to_move = []
    for _ in range(number_of_items):
        items_to_move.append(list_of_stacks[from_stack - 1].pop(0))
    for index, item in enumerate(items_to_move):
        list_of_stacks[to_stack - 1].insert(index, item)
    return list_of_stacks


def part1(stacks, procedure):
    for step in procedure:
        crate_mover_9000(stacks, *step)
    return ("").join([item[0] for item in stacks])


def part2(stacks, procedure):
    for step in procedure:
        crate_mover_9001(stacks, *step)
    return ("").join([item[0] for item in stacks])


def solve(file):
    return part1(*parser(file)), part2(*parser(file))


if __name__ == "__main__":
    print(solve("input.txt"))
