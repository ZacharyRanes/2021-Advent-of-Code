"""
TASK: Advent of code 2021 day 10 part 1

AUTHOR: Zachary Ranes
"""

OPENING_SYMBOLS = ("(","[","{","<")
CLOSING_SYMBOLS = (")","]","}",">")

MATCHING_OPENINGS_FOR_CLOSINGS = {
    ")":"(",
    "]":"[",
    "}":"{",
    ">":"<"
}

SCORE_FOR_ERROR_BY_CLOSING = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137
}


def main():
    """Main Function"""

    with open('input', 'r', encoding="UTF-8") as input_file:
        input_array = input_file.readlines()

    errors_score = 0
    stack = []

    for line in input_array:
        stack.clear()
        for line_character in line:
            if line_character in OPENING_SYMBOLS:
                stack.append(line_character)
            elif line_character in CLOSING_SYMBOLS:
                if stack[-1] != MATCHING_OPENINGS_FOR_CLOSINGS[line_character]:
                    errors_score += SCORE_FOR_ERROR_BY_CLOSING[line_character]
                    break
                else:
                    stack.pop()

    print(errors_score)

if __name__ == "__main__":
    main()
