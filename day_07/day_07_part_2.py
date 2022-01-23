"""
TASK: Advent of code 2021 day 7 part 2

AUTHOR: Zachary Ranes

NOTE: Bruit force try all end postions for how much fuel they would take to get to
      This one is very slow with bruit force... but it did find the right answer

TODO: figure out how to do this one without bruit force
"""


def fuel_used(starting_postions:list, end_postion:int) -> int:
    """
    takes a list of postions and a point all postions should move to
    returns the number of moves for all postions to get to end position
    now with new fuel cost
    """
    moves_used = 0
    for position in starting_postions:
        cost = 1
        for _ in range(1,abs(position - end_postion)+1):
            moves_used += cost
            cost += 1
    return moves_used


def main():
    """Main Function"""

    input_array = []
    with open('input', 'r', encoding="UTF-8") as input_file:
        input_array = input_file.readlines()

    array_horizontal_positions = list(map(int, input_array[0].split(",")))

    set_horizontal_positions = set(array_horizontal_positions)

    fuel_needed = fuel_used(array_horizontal_positions, 0)

    for horizontal_position in set_horizontal_positions:
        temp = fuel_used(array_horizontal_positions, horizontal_position)
        if temp < fuel_needed:
            fuel_needed = temp

    print(fuel_needed)


if __name__ == "__main__":
    main()
