import aoc202202 as aoc
import pytest


@pytest.fixture
def example():
    return aoc.parse("example.txt")


def test_format_data(example):
    assert example == [
        ("rock", "paper", "draw"),
        ("paper", "rock", "lose"),
        ("scissors", "scissors", "win"),
    ]


@pytest.mark.parametrize(
    "player1,player2,expected",
    [
        ("rock", "rock", 4),
        ("paper", "rock", 1),
        ("scissors", "rock", 7),
        ("rock", "paper", 8),
        ("paper", "paper", 5),
        ("scissors", "paper", 2),
        ("rock", "scissors", 3),
        ("paper", "scissors", 9),
        ("scissors", "scissors", 6),
    ],
)
def test_score_round(player1, player2, expected):
    assert aoc.score_round((player1, player2)) == expected


def test_score_example(example):
    assert aoc.score_round(example[0]) == 8
    assert aoc.score_round(example[1]) == 1
    assert aoc.score_round(example[2]) == 6


def test_part1(example):
    assert aoc.part1(example) == 15


def test_strategy_2(example):
    assert aoc.strategy_2(example[0]) == ("rock", "rock")
    assert aoc.strategy_2(example[1]) == ("paper", "rock")
    assert aoc.strategy_2(example[2]) == ("scissors", "rock")

def test_part2(example):
    assert aoc.part2(example) == 12
