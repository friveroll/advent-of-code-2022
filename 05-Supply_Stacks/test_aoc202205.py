"""
    Tests for
    Day 5: Supply Stacks
    Advent of Code 2022
    https://adventofcode.com/2022/day/5
"""
import aoc202205 as aoc
import pytest


@pytest.fixture
def example():
    return aoc.parser("example.txt")


@pytest.fixture
def input():
    return aoc.parser("input.txt")


def test_parser(example):
    assert example == (
        [["N", "Z"], ["D", "C", "M"], ["P"]],
        [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]],
    )


def test_move_stacks():
    assert aoc.move_stacks([["A"], ["B", "C"], ["D", "E", "F"]], 2, 2, 1) == [
        ["C", "B", "A"],
        [],
        ["D", "E", "F"],
    ]


def test_move_stacks():
    assert aoc.move_stacks(
        [["A"], ["B", "C"], ["D", "E", "F"]], 2, 2, 1, is_reversed=False
    ) == [
        ["B", "C", "A"],
        [],
        ["D", "E", "F"],
    ]


def test_part1_example(example):
    assert aoc.part1(*example) == "CMZ"


def test_part1_input(input):
    assert aoc.part1(*input) == "TLNGFGMFN"
