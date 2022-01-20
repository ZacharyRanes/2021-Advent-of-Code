"""
Advent of code 2021 day 6 Both parts
"""


def main():
    """Main Function"""

    input_array = []
    with open('input', 'r', encoding="UTF-8") as input_file:
        input_array = input_file.readlines()

    starting_fish = list(map(int, input_array[0].split(",")))

    # DAYS_PAST = 80  # Part 1
    DAYS_PAST = 256  # Part 2

    # index = days till making new spawn
    fish_states = [0] * 9
    for n in starting_fish:
        fish_states[n] += 1

    for _ in range(DAYS_PAST):
        for fish_respan_days, fish_count in enumerate(fish_states):
            if fish_respan_days == 0:
                respan_count = fish_count
            else:
                fish_states[fish_respan_days - 1] = fish_count
        fish_states[6] += respan_count
        fish_states[8] = respan_count

    print(sum(fish_states))


if __name__ == "__main__":
    main()
