import aoc202204 as aoc
import pytest


@pytest.fixture
def example():
    return aoc.parser("example.txt")


def test_parser(example):
    assert example == [
        ({2, 3, 4}, {6, 7, 8}),
        ({2, 3}, {4, 5}),
        ({5, 6, 7}, {7, 8, 9}),
        ({2, 3, 4, 5, 6, 7, 8}, {3, 4, 5, 6, 7}),
        ({6}, {4, 5, 6}),
        ({2, 3, 4, 5, 6}, {4, 5, 6, 7, 8}),
    ]


@pytest.mark.parametrize(
    "set_a,set_b",
    [({2, 3, 4, 5, 6, 7, 8}, {3, 4, 5, 6, 7}), ({6}, {3, 4, 5, 6})],
)
def test_is_contained_in(set_a, set_b):
    assert aoc.is_contained_in(set_a, set_b)


@pytest.mark.parametrize(
    "set_a,set_b",
    [
        ({5, 6, 7}, {7, 8, 9}),
        ({2, 3, 4, 5, 6, 7, 8}, {3, 4, 5, 6, 7}),
        ({6}, {4, 5, 6}),
        ({2, 3, 4, 5, 6}, {4, 5, 6, 7, 8}),
    ],
)
def test_is_overlapped(set_a, set_b):
    assert aoc.is_overlapped(set_a, set_b)


def test_part1(example):
    assert aoc.part1(example) == 2


def test_part2(example):
    assert aoc.part2(example) == 4


def test_solve(example):
    assert aoc.solve("example.txt") == (2, 4)
