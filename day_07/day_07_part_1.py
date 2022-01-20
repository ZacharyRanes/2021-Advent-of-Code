"""
Advent of code 2021 day 7 part 1
"""


def main():
    """Main Function"""

    input_array = []
    with open('input', 'r', encoding="UTF-8") as input_file:
        input_array = input_file.readlines()

    horizontal_positions = list(map(int, input_array[0].split(",")))

    print(horizontal_positions)


if __name__ == "__main__":
    main()
