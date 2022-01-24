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

    segment_1 = ""
    segment_2 = ""
    segment_3 = ""
    segment_4 = ""
    segment_5 = ""
    segment_6 = ""
    segment_7 = ""

    segment_3_or_6 = []
    segment_2_or_4 = []
    segment_5_or_7 = []

    # find 1 encoding and posable segments
    for signal in code:
        if len(signal) == 2:
            for segment in signal:
                segment_3_or_6.append(segment)
            encoding["".join(sorted(signal))] = 1
            code.remove(signal)
            break
    # find 4 encoding and posable segments
    for signal in code:
        if len(signal) == 4:
            for segment in signal:
                if segment not in segment_3_or_6:
                    segment_2_or_4.append(segment)
            encoding["".join(sorted(signal))] = 4
            code.remove(signal)
            break
    # find 7 encoding and one segment
    for signal in code:
        if len(signal) == 3:
            for segment in signal:
                if segment not in segment_3_or_6:
                    segment_1 = segment
            encoding["".join(sorted(signal))] = 7
            code.remove(signal)
            break
    # find 8 encoding and posable segments
    for signal in code:
        if len(signal) == 7:
            for segment in signal:
                if segment not in segment_3_or_6 \
                and segment not in segment_2_or_4 \
                and segment != segment_1:
                    segment_5_or_7.append(segment)
            encoding["".join(sorted(signal))] = 8
            code.remove(signal)
            break
    # find 9 encoding
    for signal in code:
        if len(signal) == 6:
            if segment_5_or_7[0] in signal and segment_5_or_7[1] not in signal:
                encoding["".join(sorted(signal))] = 9
                segment_5 = segment_5_or_7[1]
                segment_7 = segment_5_or_7[0]
                code.remove(signal)
                break
            if segment_5_or_7[1] in signal and segment_5_or_7[0] not in signal:
                encoding["".join(sorted(signal))] = 9
                segment_5 = segment_5_or_7[0]
                segment_7 = segment_5_or_7[1]
                code.remove(signal)
                break
    # find 0 encoding
    for signal in code:
        if len(signal) == 6:
            if segment_2_or_4[0] in signal and segment_2_or_4[1] not in signal:
                encoding["".join(sorted(signal))] = 0
                segment_2 = segment_2_or_4[0]
                segment_4 = segment_2_or_4[1]
                code.remove(signal)
                break
            if segment_2_or_4[1] in signal and segment_2_or_4[0] not in signal:
                encoding["".join(sorted(signal))] = 0
                segment_2 = segment_2_or_4[1]
                segment_4 = segment_2_or_4[0]
                code.remove(signal)
                break
    # find 6 encoding
    for signal in code:
        if len(signal) == 6:
            if segment_3_or_6[0] in signal and segment_3_or_6[1] not in signal:
                encoding["".join(sorted(signal))] = 6
                segment_3 = segment_3_or_6[1]
                segment_6 = segment_3_or_6[0]
                code.remove(signal)
                break
            if segment_3_or_6[1] in signal and segment_3_or_6[0] not in signal:
                encoding["".join(sorted(signal))] = 6
                segment_3 = segment_3_or_6[0]
                segment_6 = segment_3_or_6[1]
                code.remove(signal)
                break
    # with all segments know find that last three
    for signal in code:
        if segment_1 in signal\
        and segment_3 in signal\
        and segment_4 in signal\
        and segment_5 in signal\
        and segment_7 in signal:
            encoding["".join(sorted(signal))] = 2
        if segment_1 in signal\
        and segment_3 in signal\
        and segment_4 in signal\
        and segment_6 in signal\
        and segment_7 in signal:
            encoding["".join(sorted(signal))] = 3
        if segment_1 in signal\
        and segment_2 in signal\
        and segment_4 in signal\
        and segment_6 in signal\
        and segment_7 in signal:
            encoding["".join(sorted(signal))] = 5


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
        working_output_string = ""
        for encoded_number in output_encoded:
            sorted_encoded_number = "".join(sorted(encoded_number))
            working_output_string += str(decoding_dictionary[sorted_encoded_number])
        sum_all_outputs += int(working_output_string)

    print(sum_all_outputs)


if __name__ == "__main__":
    main()
