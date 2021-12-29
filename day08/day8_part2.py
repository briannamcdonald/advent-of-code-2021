def organize_data(lines):
    # organize into a list containing lists of digits and outputs where each digit is represented by a set of characters
    digits = []
    outputs = []
    for line in lines:
        digit_section, output_section = line.split(" | ")
        digit_list = digit_section.strip().split(" ")
        output_list = output_section.strip().split(" ")
        digits.append([{char for char in digit} for digit in digit_list])
        outputs.append([{char for char in output} for output in output_list])

    return digits, outputs


def get_shared_segments(digit1, digit2):
    # get a list of segments that are in both digits
    shared_segments = []
    for val in digit1:
        if val in digit2:
            shared_segments.append(val)
    return shared_segments


def main():
    data = open("day08/input.txt", "r")
    lines = [line for line in data]
    digits_list, outputs_list = organize_data(lines)

    output_sum = 0
    for i in range(len(digits_list)):
        digits = digits_list[i]
        outputs = outputs_list[i]

        # we can get 1, 7, 4, and 8 since they have unique lengths
        for digit in digits:
            if len(digit) == 2:
                one = digit
            elif len(digit) == 3:
                seven = digit
            elif len(digit) == 4:
                four = digit
            elif len(digit) == 7:
                eight = digit
        digits.remove(one)
        digits.remove(seven)
        digits.remove(four)
        digits.remove(eight)

        # we can find 2, 5, and 6 since they share only one segment with 1
        options = []
        for digit in digits:
            shared_segments = get_shared_segments(one, digit)
            if len(shared_segments) == 1:
                options.append(digit)
        # 6 shares one segment with 1 and has length six
        for option in options:
            if len(option) == 6:
                six = {char for char in option}
                options.remove(option)
        # 5 shares the same segment as 6 and 2 is unique
        six_shared_segment = get_shared_segments(one, six)[0]
        if six_shared_segment in options[0]:
            five = {char for char in options[0]}
            two = {char for char in options[1]}
        else:
            five = {char for char in options[1]}
            two = {char for char in options[0]}
        digits.remove(two)
        digits.remove(five)
        digits.remove(six)

        # 3 is the only digit of length five left
        for digit in digits:
            if len(digit) == 5:
                three = digit
        digits.remove(three)

        # 9 shares four digits with 4
        for digit in digits:
            if len(get_shared_segments(digit, four)) == 4:
                nine = digit
        digits.remove(nine)

        # 0 is the last digit left
        zero = digits[0]

        # get the output value and add it to the sum
        found_digits = [zero, one, two, three, four, five, six, seven, eight, nine]
        output_val = ""
        for output_digit in outputs:
            output_val += str(found_digits.index(output_digit))
        output_sum += int(output_val)

    print(output_sum)


if __name__ == "__main__":
    main()
