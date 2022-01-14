"""
Advent of code 2021 day 3 part 2
"""


def frequency(array_of_binaries_as_string, frequency_bit, most_common=True):
    """INPUT: array that holds 12bit numbers stored as strings
              which of the 12bits to look at as index starting at 0
              weather or not to be basing on most or least frequent
       LOGIC: looks at each number and selects the numbers that has the
              most/least common assurances of the 1 or 0 at the given position
       OUTPUT: a sub array of the given array that passes the check
    """

    frequency_array = [[], []]

    for row in array_of_binaries_as_string:
        if row[frequency_bit] == "0":
            frequency_array[0].append(row.strip())
        if row[frequency_bit] == "1":
            frequency_array[1].append(row.strip())

    if most_common:
        if len(frequency_array[0]) <= len(frequency_array[1]):
            return frequency_array[1]
        return frequency_array[0]
    # most_common == false
    if len(frequency_array[0]) <= len(frequency_array[1]):
        return frequency_array[0]
    return frequency_array[1]


def main():
    """Main Function"""

    input_array = []
    with open('input', 'r', encoding="UTF-8") as input_file:
        input_array = input_file.readlines()

    # print(frequency(input_array, 0))
    oxygen_array = input_array
    for i in range(12):
        oxygen_array = frequency(oxygen_array, i)
        if len(oxygen_array) == 1:
            break

    co2_array = input_array
    for i in range(12):
        co2_array = frequency(co2_array, i, False)
        if len(co2_array) == 1:
            break

    oxygen = int(oxygen_array[0], 2)
    co2 = int(co2_array[0], 2)

    print(co2 * oxygen)


if __name__ == "__main__":
    main()
