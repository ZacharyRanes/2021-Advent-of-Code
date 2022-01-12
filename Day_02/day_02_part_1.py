def main():
    input_array = []

    with open('input', 'r', encoding="UTF-8") as input_file:
        input_array = input_file.readlines()

    depth = 0
    horizontal = 0

    for i in range(0, len(input_array)):
        if input_array[i][0] == "f":
            horizontal += int(input_array[i][-2])
        elif input_array[i][0] == "d":
            depth += int(input_array[i][-2])
        elif input_array[i][0] == "u":
            depth -= int(input_array[i][-2])

    print("depth: %d" % depth)
    print("horizontal %d" % horizontal)
    print("Answer: %d" % (depth * horizontal))


if __name__ == "__main__":
    main()
