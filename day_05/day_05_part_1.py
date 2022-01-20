"""
Advent of code 2021 day 5 part 1
"""


def line_math(input_array):
    """
    input array of arrays with x1,y1,x2,y2
    """

    line_diagram = []
    for _ in range(1000):
        line_diagram.append([0] * 1000)

    for line in input_array:
        x1 = line[0]
        y1 = line[1]
        x2 = line[2]
        y2 = line[3]

        if x1 == x2:
            if y1 <= y2:
                for i in range(y1, y2+1):
                    line_diagram[x1][i] += 1
            else:
                for i in range(y2, y1+1):
                    line_diagram[x1][i] += 1
        elif y1 == y2:
            if x1 <= x2:
                for i in range(x1, x2+1):
                    line_diagram[i][y2] += 1
            else:
                for i in range(x2, x1+1):
                    line_diagram[i][y2] += 1

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

    danger_areas = 0
    for line in output_array:
        for n in line:
            if n >= 2:
                danger_areas += 1

    print(danger_areas)

    # 977000 too high


if __name__ == "__main__":
    main()
