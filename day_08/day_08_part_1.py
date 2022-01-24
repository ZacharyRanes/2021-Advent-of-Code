"""
TASK: Advent of code 2021 day 8 part 1

AUTHOR: Zachary Ranes
"""


def main():
    """Main Function"""

    with open('input', 'r', encoding="UTF-8") as input_file:
        input_array = input_file.readlines()

    modded_input = []
    for line in input_array:
        modded_input.append(line.split())

    count = 0
    for line in modded_input:
        for i in range(-4,0):
            if len(line[i]) in (2,4,3,7):
                count += 1

    print(count)


if __name__ == "__main__":
    main()
