"""
Advent of code 2021 day 5 part 1
"""


def line_math(input_array):
    """
    input array of arrays with x1,y2,x2,y2
    """

    line_diagram = [[0]*10] * 10

    for a in input_array:
        x1 = a[0]
        x2 = a[2]
        y1 = a[1]
        y2 = a[3]

        if x1 == x2:
            pass
        if y1 == y2:
            pass

    return line_diagram


def main():
    """Main Function"""

    input_array = []
    with open('input.txt', 'r', encoding="UTF-8") as input_file:
        input_array = input_file.readlines()

    modded_input = []
    for line in input_array:
        editing_array = line.split()
        useful_array = (list(map(int, editing_array[0].split(",")))) \
            + (list(map(int, editing_array[2].split(","))))
        modded_input.append(useful_array)

    output_array = line_math(modded_input)

    for line in output_array:
        print(line)


if __name__ == "__main__":
    main()
