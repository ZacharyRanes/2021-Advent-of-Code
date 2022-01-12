def main():

    input_array = []
    with open('input', 'r', encoding="UTF-8") as input_file:
        input_array = input_file.readlines()

    # [x][y] x will be 0 for 0s and 1 for 1s
    # [x][y] y the col of the input
    distribution = [[0] * 12, [0] * 12]

    for row in input_array:
        for i, char in enumerate(row):
            if char != '\n':
                if int(char) == 0:
                    distribution[0][i] += 1
                if int(char) == 1:
                    distribution[1][i] += 1

    print(distribution)


    #print("Answer: %d" % ())


if __name__ == "__main__":
    main()