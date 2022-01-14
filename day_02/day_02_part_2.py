def main():
    input_array = []

    with open('input', 'r', encoding="UTF-8") as input_file:
        input_array = input_file.readlines()

    depth = 0
    horizontal = 0
    aim = 0

    for row in input_array:
        if row[0] == "f":
            horizontal += int(row[-2])
            depth += (int(row[-2]) * aim)
        elif row[0] == "d":
            aim += int(row[-2])
        elif row[0] == "u":
            aim -= int(row[-2])

    print("depth: %d" % depth)
    print("horizontal %d" % horizontal)
    print("Answer: %d" % (depth * horizontal))


if __name__ == "__main__":
    main()
