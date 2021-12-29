def organize_data(lines):
    digits = []
    outputs = []
    for line in lines:
        digit, output = line.split(" | ")
        digits.append(digit.strip().split(" "))
        outputs.append(output.strip().split(" "))

    return digits, outputs


def main():
    data = open("day08/input.txt", "r")
    lines = [line for line in data]
    _, outputs = organize_data(lines)

    counter = 0
    for output in outputs:
        for value in output:
            if len(value) == 2 or len(value) == 3 or len(value) == 4 or len(value) == 7:
                counter += 1

    print(counter)


if __name__ == "__main__":
    main()
