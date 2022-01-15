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

    game_boards = [[]]
    game_board_index = 0

    for line in input_array[2:]:
        if line != '\n':
            game_boards[game_board_index].append(list(map(int, line.split())))
        else:
            game_board_index += 1
            game_boards.append([])

    print(game_boards)


if __name__ == "__main__":
    main()
