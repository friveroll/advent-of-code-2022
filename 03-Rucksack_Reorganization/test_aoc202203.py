import aoc202203 as aoc
import pytest


def test_parse():
    assert aoc.parse("example.txt") == [
        ("vJrwpWtwJgWr", "hcsFMMfFFhFp"),
        ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"),
        ("PmmdzqPrV", "vPwwTWBwg"),
        ("wMqvLMZHhHMvwLH", "jbvcjnnSBnvTQFn"),
        ("ttgJtRGJ", "QctTZtZT"),
        ("CrZsJsPPZsGz", "wwsLwLmpwMDw"),
    ]


@pytest.fixture
def example():
    return aoc.parse("example.txt")


def test_get_unique_letter(example):
    assert aoc.get_unique_letter(example[0]) == "p"
    assert aoc.get_unique_letter(example[1]) == "L"
    assert aoc.get_unique_letter(example[2]) == "P"
    assert aoc.get_unique_letter(example[3]) == "v"
    assert aoc.get_unique_letter(example[4]) == "t"
    assert aoc.get_unique_letter(example[5]) == "s"


def test_get_priority():
    assert aoc.get_priority("p") == 16
    assert aoc.get_priority("L") == 38
    assert aoc.get_priority("P") == 42
    assert aoc.get_priority("v") == 22
    assert aoc.get_priority("t") == 20
    assert aoc.get_priority("s") == 19


def test_part1(example):
    assert aoc.part1(example) == 157
