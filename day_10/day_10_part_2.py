"""
TASK: Advent of code 2021 day 10 part 2

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

SCORE_FOR_TYPE = {
    "(":1,
    "[":2,
    "{":3,
    "<":4
}


def main():
    """Main Function"""

    with open('input', 'r', encoding="UTF-8") as input_file:
        input_array = input_file.readlines()

    stack = []
    scores_array = []
    scores_array_index = -1

    for line in input_array:
        stack.clear()
        for line_character in line:
            if line_character in OPENING_SYMBOLS:
                stack.append(line_character)
            elif line_character in CLOSING_SYMBOLS:
                if stack[-1] != MATCHING_OPENINGS_FOR_CLOSINGS[line_character]:
                    break
                else:
                    stack.pop()
        else:
            scores_array.append(0)
            scores_array_index += 1
            stack_size = len(stack)
            for _ in range(stack_size):
                element = stack.pop()
                scores_array[scores_array_index] *= 5
                scores_array[scores_array_index] += SCORE_FOR_TYPE[element]

    scores_array.sort()
    mid_index = round(len(scores_array)/2)
    print(scores_array[mid_index])


if __name__ == "__main__":
    main()
