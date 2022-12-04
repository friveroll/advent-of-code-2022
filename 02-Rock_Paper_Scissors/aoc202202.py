""" Day 2: Rock Paper Scissors
    https://adventofcode.com/2020/day/2  """

import re


def parse(filename):
    """Parse the input file into a list of tuples."""
    out = []
    with open(filename, "r", encoding="utf-8") as reader:
        for line in reader:
            line_result = re.search(r"([ABC])\s([XYZ])", line)
            player1, player2, outcome = "", "", ""
            if line_result.group(1) == "A":
                player1 = "rock"
            elif line_result.group(1) == "B":
                player1 = "paper"
            elif line_result.group(1) == "C":
                player1 = "scissors"
            if line_result.group(2) == "X":
                player2 = "rock"
                outcome = "lose"
            elif line_result.group(2) == "Y":
                player2 = "paper"
                outcome = "draw"
            elif line_result.group(2) == "Z":
                player2 = "scissors"
                outcome = "win"
            out.append((player1, player2, outcome))
    return out


def score_round(data):
    """Score a single round of Rock Paper Scissors."""
    result = 0
    player1, player2 = data[0], data[1]
    if player2 == "rock":
        result += 1
        if player1 == "rock":
            result += 3
        elif player1 == "scissors":
            result += 6
    elif player2 == "paper":
        result += 2
        if player1 == "paper":
            result += 3
        elif player1 == "rock":
            result += 6
    elif player2 == "scissors":
        result += 3
        if player1 == "scissors":
            result += 3
        elif player1 == "paper":
            result += 6
    return result


def part1(data):
    """Solve part 1."""
    return sum(score_round(d) for d in data)


def strategy_2(data):
    """Choice with the strategy guide from data[2]"""
    player1, outcome = data[0], data[2]
    player2 = ""
    if outcome == "win":
        if player1 == "rock":
            player2 = "paper"
        elif player1 == "paper":
            player2 = "scissors"
        elif player1 == "scissors":
            player2 = "rock"
    elif outcome == "lose":
        if player1 == "rock":
            player2 = "scissors"
        elif player1 == "paper":
            player2 = "rock"
        elif player1 == "scissors":
            player2 = "paper"
    elif outcome == "draw":
        player2 = player1
    return player1, player2


def part2(data):
    """Solve part 2."""
    return sum(score_round(strategy_2(d)) for d in data)


def solve(filename):
    """Solve the puzzle."""
    data = parse(filename)
    return part1(data), part2(data)


if __name__ == "__main__":
    print(solve("input.txt"))
