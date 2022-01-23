"""
Advent of code 2021 day 4 part 1
"""

import copy

class BingoBoard:
    """ The Bingo game board as an object"""

    def __init__(self, board_input):
        self.game_board = board_input
        self.space_used = []
        for i in range(5):
            self.space_used.append([])
            for _ in range(5):
                self.space_used[i].append(False)

    def print_board(self) -> None:
        print("--------------------------")
        for line in self.game_board:
            for space in line:
                print(f"| {space:^2} ",end="")
            print("|")
        print("--------------------------")
        for line in self.space_used:
            for space in line:
                print(f"| {space:^2} ", end="")
            print("|")
        print("--------------------------")

    def sum_not_called(self) -> int:
        score = 0
        for i in range(5):
            for j in range(5):
                if self.space_used[i][j] is False:
                    score += self.game_board[i][j]
        return(score)

    def has_won(self) -> bool:
        for line in self.space_used:
            if line == [True, True, True, True, True]:
                return True
        for i in range(5):
            for line in self.space_used:
                if line[i] is not True:
                    break
            else:
                return True
        return False

    def call_number(self, number) -> bool:
        for i in range(5):
            for j in range(5):
                if self.game_board[i][j] == number:
                    self.space_used[i][j] = True
        return self.has_won()


def main():
    """Main Function"""

    input_array = []
    with open('input.txt', 'r', encoding="UTF-8") as input_file:
        input_array = input_file.readlines()

    input_calls = input_array[0].strip()
    array_of_calls = list(map(int, input_calls.split(",")))

    array_of_boards = []
    temp_board = []

    input_array_index = 2
    while input_array_index <= len(input_array):
        for _ in range(5):
            temp_board.append(list(map(int, input_array[input_array_index].split())))
            input_array_index += 1
        input_array_index += 1
        array_of_boards.append(BingoBoard((temp_board)))
        temp_board = []

    for number in array_of_calls:
        for board in array_of_boards:
            win = board.call_number(number)
            if win:
                board.print_board()
                not_called = board.sum_not_called()
                print(f"Summed Spaces {not_called}")
                print(f"Last called {number}")
                print(f"Finals score {number * not_called}")
                return


if __name__ == "__main__":
    main()
