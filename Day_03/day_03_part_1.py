"""
Advent of code 2021 day 3 part 1
"""


def main():
    """Main Function"""

    input_array = []
    with open('input', 'r', encoding="UTF-8") as input_file:
        input_array = input_file.readlines()

    frequency = [[0] * 12, [0] * 12]

    for row in input_array:
        for i, c in enumerate(row):
            if c == "0":
                frequency[0][i] += 1
            if c == "1":
                frequency[1][i] += 1

    gamma_string = ""
    for i in range(12):
        if frequency[0][i] > frequency[1][i]:
            gamma_string += "0"
        if frequency[0][i] < frequency[1][i]:
            gamma_string += "1"

    gamma = int(gamma_string, 2)

    epsilon_string = ""
    for i in range(12):
        if frequency[0][i] < frequency[1][i]:
            epsilon_string += "0"
        if frequency[0][i] > frequency[1][i]:
            epsilon_string += "1"

    epsilon = int(epsilon_string, 2)

    print(gamma)
    print(epsilon)

    print(gamma*epsilon)


if __name__ == "__main__":
    main()
