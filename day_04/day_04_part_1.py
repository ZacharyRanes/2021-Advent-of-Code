"""
Advent of code 2021 day 4 part 1
"""


class BingoBoard:
    """ The Bingo game board as an object"""
    game_board = []
    space_used = []
    for _ in range(5):
        space_used.append([False] * 5)

    def __init__(self, board_input):
        self.game_board = board_input

    def print_board(self):
        for line in self.game_board:
            print(line)
        for line in self.space_used:
            print(line)

    def not_used_spaces_sum(self):
        score = 0
        for i in range(5):
            for j in range(5):
                if self.space_used[i][j] is False:
                    score += self.game_board[i][j]
        return(score)

    def has_won(self):
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

    def number_called(self, number):
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

    game_boards = []
    temp_game_board = []

    for line in input_array[2:]:
        if line != '\n':
            temp_game_board.append(list(map(int, line.split())))
        else:
            board = BingoBoard(temp_game_board)
            game_boards.append(board)
            temp_game_board = []

    for n in array_of_calls:
        for b in game_boards:
            win = b.number_called(n)
            if win:
                b.print_board()
                un_used = b.not_used_spaces_sum()
                print(f"Summed Spaces {un_used}")
                print(f"Last called {n}")
                print(f"Finals score {n * un_used}")
                return


if __name__ == "__main__":
    main()
