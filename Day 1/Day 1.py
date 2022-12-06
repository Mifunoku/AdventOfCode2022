import queue

my_file = "input.txt"


def find_elf(filename: str) -> int:
    elf_number = 1
    calories = 0
    max_calories = 0
    with open(filename) as file:
        for line in file:
            if line := line.strip():
                calories += int(line)
            else:
                if max_calories < calories:
                    elf_carrying_number = elf_number
                    max_calories = calories
                elf_number += 1
                calories = 0
    return elf_carrying_number, max_calories


print(find_elf(my_file))
