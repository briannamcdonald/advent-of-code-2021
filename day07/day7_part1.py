def main():
    data = open("day07/input.txt", "r")
    lines = [line for line in data]
    crabs = [int(fish.strip()) for fish in lines[0].split(",")]

    median_val = sorted(crabs)[len(crabs) // 2]
    fuel_sum = 0
    for crab in crabs:
        fuel_sum += abs(crab - median_val)

    print(fuel_sum)


if __name__ == "__main__":
    main()
