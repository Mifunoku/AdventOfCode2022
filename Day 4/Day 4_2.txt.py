import re

my_file = "input.txt"


def is_overlapped(section1_start: int, section1_stop: int, section2_start: int, section2_stop: int):
    if section1_stop < section2_start:
        return 0
    if section1_start > section2_stop:
        return 0
    return 1


def total_score(filename: str) -> int:
    score = 0
    with open(filename) as file:
        for line in file:
            a, b, c, d = map(int, re.split("\W", line[:-1]))
            score += is_overlapped(a, b, c, d)
    return score


print(total_score(my_file))
