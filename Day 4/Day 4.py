import re

my_file = "input.txt"


def is_fully_overlapped(section1_start: int, section1_stop: int, section2_start: int, section2_stop: int):
    # if section1_start >= section2_start and section1_stop <= section2_stop:
    #     return 1
    # if section2_start >= section1_start and section2_stop <= section1_stop:
    #     return 1
    start_subtraction = section1_start - section2_start
    stop_subtraction = section1_stop - section2_stop
    return start_subtraction * stop_subtraction <= 0


def total_score(filename: str) -> int:
    score = 0
    with open(filename) as file:
        for line in file:
            a, b, c, d = map(int, re.split("\W", line[:-1]))
            score += is_fully_overlapped(a, b, c, d)
    return score


print(total_score(my_file))
