from __future__ import annotations
import typing

my_file = "input.txt"


class RPSGame:
    name: str
    value: int

    def __init__(self, name: str):
        if name in ("A", "X", "Rock"):
            self.name = "Rock"
            self.value = 1

        if name in ("B", "Y", "Paper"):
            self.name = "Paper"
            self.value = 2

        if name in ("C", "Z", "Scissors"):
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


def fight_score(opponent: str, you: str) -> int:
    opponent = RPSGame(opponent)
    you = RPSGame(you)
    if opponent > you:
        return you.value
    elif opponent == you:
        return 3 + you.value
    return 6 + you.value


def total_score(filename: str) -> int:
    score = 0
    with open(filename) as file:
        for line in file:
            opponent, you = line.split()
            score += fight_score(opponent, you)
    return score


print(total_score(my_file))
