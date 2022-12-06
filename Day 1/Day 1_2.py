import queue

my_file = "input.txt"
number_of_top_calories = 3


def find_elves_order(filename: str) -> queue.PriorityQueue:
    elves_ordered = queue.PriorityQueue()
    elf_number = 1
    calories = 0
    with open(filename) as file:
        for line in file:
            if line := line.strip():
                calories += int(line)
            else:
                elves_ordered.put((-calories, elf_number))  # priority sorts in ascending order, so we change the sign
                elf_number += 1
                calories = 0
    return elves_ordered


def get_sum_of_top_calories(filename:str, top: int) -> int:
    order = find_elves_order(filename)
    sum_of_top_calories = 0
    for _ in range(top):
        sum_of_top_calories += order.get()[0]
    return -sum_of_top_calories  # changing the sign to get proper value


print(get_sum_of_top_calories(my_file, 3))
