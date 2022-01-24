"""
TASK: Advent of code 2021 day 8 part 2

AUTHOR: Zachary Ranes
"""


def decode(code:list) -> dict:
    """
    Takes a list of singals patterns
    returns a dict that holds key encoding value the int digit is repsresents
    """
    encoding = {}

    segment_1_sure = ""
    segment_2 = []
    segment_3_sure = ""
    segment_3 = []
    segment_4 = []
    segment_5 = []
    segment_6_sure = ""
    segment_6 = []
    segment_7 = []

    # find 1 encoding and posable segments
    for n in code:
        if len(n) == 2:
            encoding["".join(sorted(n))] = 1
            for segment in n:
                segment_3.append(segment)
                segment_6.append(segment)
            code.remove(n)
            break
    # find 4 encoding and posable segments
    for n in code:
        if len(n) == 4:
            for segment in n:
                if segment not in segment_3 and segment not in segment_6:
                    segment_2.append(segment)
                    segment_4.append(segment)
            encoding["".join(sorted(n))] = 4
            code.remove(n)
            break
    # find 7 encoding and one segment
    for n in code:
        if len(n) == 3:
            for segment in n:
                if segment not in segment_3 and segment not in segment_6:
                    segment_1_sure = segment
            encoding["".join(sorted(n))] = 7
            code.remove(n)
            break
    # find 8 encoding and posable segments
    for n in code:
        if len(n) == 7:
            encoding["".join(sorted(n))] = 8
            for segment in n:
                if segment not in segment_1_sure \
                and segment not in segment_2 \
                and segment not in segment_3 \
                and segment not in segment_4 \
                and segment not in segment_6:
                    segment_5.append(segment)
                    segment_7.append(segment)
            code.remove(n)
            break
    # find 9 encoding
    for n in code:
        if len(n) == 6:
            not_it = False
            for segment in n:
                if segment in segment_5:
                    if not not_it:
                        break
                    else:
                        not_it = True
                encoding["".join(sorted(n))] = 9
                code.remove(n)
                break
    #find 0 encoding
    for n in code:
        if len(n) == 6:
            not_it = False
            for segment in n:
                if segment in segment_4:
                    if not not_it:
                        break
                    else:
                        not_it = True
                encoding["".join(sorted(n))] = 0
                code.remove(n)
                break
    #find 6 encoding
    for n in code:
        if len(n) == 6:
            not_it = False
            for segment in n:
                if segment in segment_3:
                    if not not_it:
                        break
                    else:
                        not_it = True
                encoding["".join(sorted(n))] = 6
                if segment_3[0] in n:
                    segment_3_sure = segment_3[1]
                    segment_6_sure = segment_3[0]
                else:
                    segment_3_sure = segment_3[0]
                    segment_6_sure = segment_3[1]
                code.remove(n)
                break

    for n in code:
        if segment_3_sure not in n \
        and segment_6_sure in n:
            encoding["".join(sorted(n))] = 5
        if segment_3_sure in n \
        and segment_6_sure in n:
            encoding["".join(sorted(n))] = 3
        if segment_3_sure in n \
        and segment_6_sure not in n:
            encoding["".join(sorted(n))] = 2

    return encoding


def main():
    """Main Function"""

    with open('input', 'r', encoding="UTF-8") as input_file:
        input_array = input_file.readlines()

    modded_input = []
    for line in input_array:
        modded_input.append(line.split())

    sum_all_outputs = 0
    for line in modded_input:
        line_coding = line[0:10]
        decoding_dictionary = decode(line_coding)
        output_encoded = line[-4:]
        for encoded_number in output_encoded:
            sorted_encoded_number = "".join(sorted(encoded_number))
            sum_all_outputs += decoding_dictionary[sorted_encoded_number]

    print(sum_all_outputs)
    # 3778 too low

if __name__ == "__main__":
    main()
