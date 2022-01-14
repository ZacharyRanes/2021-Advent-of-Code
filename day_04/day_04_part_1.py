"""
Advent of code 2021 day 4 part 1
"""


def main():
    """Main Function"""

    input_array = []
    with open('input.txt', 'r', encoding="UTF-8") as input_file:
        input_array = input_file.readlines()

    input_calls = input_array[0].strip()
    array_of_calls = list(map(int, input_calls.split(",")))

    

if __name__ == "__main__":
    main()
