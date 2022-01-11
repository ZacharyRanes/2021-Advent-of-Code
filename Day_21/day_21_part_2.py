def Board_Move(position, moves):
    BOARD_SPACES = 10
    position = ((position + moves) % BOARD_SPACES)

    # If position becomes BOARD_SPACES it must be on BOARD_SPACES
    if position == 0:
        position = BOARD_SPACES

    return position


def main():

    NUM_TURNS = 3
    WIN_SCORE = 21

    input_array = []
    with open('input', 'r', encoding="UTF-8") as input_file:
        input_array = input_file.readlines()

    p1_position = int(input_array[0][-2])
    p2_position = int(input_array[1][-2])

    p1_wins = 0
    p2_wins = 0

    # ques do not work something specail

    print("P1 Wins: %d" % p1_wins)
    print("P2 Wins: %d" % p2_wins)


if __name__ == "__main__":
    main()
