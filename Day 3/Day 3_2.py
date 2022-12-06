my_file = "input.txt"


def rucksack_score(rucksack_1: str, rucksack_2: str, rucksack_3: str) -> int:
    inner = set(rucksack_1) & set(rucksack_2) & set(rucksack_3)
    score = 0
    for letter in inner:
        number = ord(letter)
        if number < 94:
            score += number - 38
        else:
            score += number - 96
    return score


def total_score(filename: str) -> int:
    score = 0
    with open(filename) as file:
        while line := file.readline():
            score += rucksack_score(line.strip(), file.readline().strip(), file.readline().strip())
    return score


print(total_score(my_file))
