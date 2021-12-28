def main():
    data = open("day07/input.txt", "r")
    lines = [line for line in data]
    crabs = [int(fish.strip()) for fish in lines[0].split(",")]

    mean_val = round(sum(crabs) / len(crabs))
    fuel_sum = 0
    for crab in crabs:
        n = abs(crab - mean_val)
        fuel_sum += (n * (n + 1)) / 2

    print(int(fuel_sum))


if __name__ == "__main__":
    main()
