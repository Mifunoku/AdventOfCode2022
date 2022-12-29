import re
import numpy as np

my_file = "input.txt"
# my_file = "input_test.txt"

def moving(filename: str) -> str:
    cargo = []
    temp = []
    mode = 'cargo'
    with open(filename) as file:
        for line in file:
            if line != '\n':
                if mode == 'cargo':
                    for index, value in enumerate(line):
                        if (index-1)%4 == 0:
                            if value == ' ':
                                value = 0
                            temp.append(value)
                    cargo.append(temp)
                    temp = []
                if mode == 'moves':
                    tokens = np.array(re.split("\W", line))
                    no_crates, stack_from, stack_to = map(int, tokens[[1,3,5]])
                    cargo[stack_to-1].extend(cargo[stack_from-1][-no_crates:])
                    cargo[stack_from - 1] = cargo[stack_from - 1][:-no_crates]
            else:
                if mode == 'cargo':
                    cargo.pop()
                    cargo = list(map(list, zip(*(cargo[::-1]))))
                    cargo = [list(filter(lambda item: item != 0, stack)) for stack in cargo]
                mode = 'moves'
    print(cargo)
    message = [stack.pop() for stack in cargo]
    return ''.join(message)

print(moving(my_file))
