""" test for Day 1: Calorie Counting
    advent of code 2022"""

import aoc202201 as aoc
import pytest


@pytest.fixture
def example():
    return aoc.parse("example.txt")


def test_parse(example):
    assert example == [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
    ]


def test_part1(example):
    assert aoc.part1(example) == 24000


def test_part2(example):
    assert aoc.part2(example) == 45000
