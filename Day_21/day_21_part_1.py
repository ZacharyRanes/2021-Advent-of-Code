def Board_Move(position, moves):
    BOARD_SPACES = 10
    position = ((position + moves) % BOARD_SPACES)

    # If position becomes BOARD_SPACES it must be on BOARD_SPACES
    if position == 0:
        position = BOARD_SPACES

    return position


def main():

    NUM_TURNS = 3
    WIN_SCORE = 1000

    input_array = []

    with open('input', 'r', encoding="UTF-8") as input_file:
        input_array = input_file.readlines()

    p1_position = int(input_array[0][-2])
    p2_position = int(input_array[1][-2])

    p1_score = 0
    p2_score = 0

    p1_turn = True
    p2_turn = False
    turn_count = 0

    game_won = False
    dice_rolled = 0

    while not game_won:
        for i in range(1, 101):
            dice_rolled += 1

            if p1_turn:
                turn_count += 1
                p1_position = Board_Move(p1_position, i)

            if p2_turn:
                turn_count += 1
                p2_position = Board_Move(p2_position, i)

            if turn_count >= NUM_TURNS:
                if p1_turn:
                    p1_score += p1_position
                if p2_turn:
                    p2_score += p2_position
                p1_turn = not p1_turn
                p2_turn = not p2_turn
                turn_count = 0

            if p1_score >= WIN_SCORE:
                print("P1 Wins")
                game_won = True
                break

            if p2_score >= WIN_SCORE:
                print("P2 Wins")
                game_won = True
                break

    print("Dice Rolled: %d" % dice_rolled)
    print("P1 Score: %d" % p1_score)
    print("P2 Score: %d" % p2_score)


if __name__ == "__main__":
    main()
