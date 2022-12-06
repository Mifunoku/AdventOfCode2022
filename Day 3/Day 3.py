my_file = "input.txt"


def rucksack_score(rucksack: str) -> int:
    half = len(rucksack) // 2
    first_compartment = list(rucksack[:half])
    second_compartment = list(rucksack[half:])
    inner = set(first_compartment) & set(second_compartment)

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
        for line in file:
            score += rucksack_score(line.strip())
    return score


print(total_score(my_file))
