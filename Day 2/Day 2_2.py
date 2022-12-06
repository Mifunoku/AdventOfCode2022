from __future__ import annotations
import typing

my_file = "input.txt"


class RPSGame:
    name: str
    value: int

    def __init__(self, name: str):
        if name in ("A", "Rock"):
            self.name = "Rock"
            self.value = 1

        if name in ("B", "Paper"):
            self.name = "Paper"
            self.value = 2

        if name in ("C", "Scissors"):
            self.name = "Scissors"
            self.value = 3

    def __eq__(self, other: RPSGame):
        return self.name == other.name

    def __gt__(self, other: RPSGame):
        if self.name == "Rock" and other.name == "Scissors":
            return True
        if self.name == "Paper" and other.name == "Rock":
            return True
        if self.name == "Scissors" and other.name == "Paper":
            return True
        return False


def fight_score(opponent: str, result: str) -> int:
    order = ['Rock', 'Paper', 'Scissors']
    opponent = RPSGame(opponent)
    if result == 'X':  # lose
        index = (order.index(opponent.name) - 1) % 3
        you = RPSGame(order[index])
        return 0 + you.value
    elif result == 'Z':  # win
        index = (order.index(opponent.name) + 1) % 3
        you = RPSGame(order[index])
        return 6 + you.value
    return 3 + opponent.value  # draw


def total_score(filename: str) -> int:
    score = 0
    with open(filename) as file:
        for line in file:
            opponent, you = line.split()
            score += fight_score(opponent, you)
    return score


print(total_score(my_file))
