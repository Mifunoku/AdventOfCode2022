
my_file, marker_length = "input.txt", 14
# my_file, marker_length = "input_test.txt", 4

def marker_position(filename: str, marker_length: int = 4) -> int:
    with open(filename) as file:
        message = file.readline()
    marker, message = message[:marker_length], message[marker_length:]
    for index, char in enumerate(message):
        if len(set(marker)) == marker_length:
            return marker_length+index
        marker = marker[1:]+char
    return len(message)+marker_length

print(marker_position(my_file, marker_length))
