def main():
    data = open("day06/input.txt", "r")
    lines = [line for line in data]
    lanternfish = [int(fish.strip()) for fish in lines[0].split(",")]
    
    NUM_OF_DAYS = 80
    ADULT_CYCLE_VAL = 6
    CHILD_CYCLE_VAL = 8
    for _ in range(NUM_OF_DAYS):
        for i in range(len(lanternfish)):
            if lanternfish[i] >= 1:
                lanternfish[i] -= 1
            else:
                lanternfish[i] = ADULT_CYCLE_VAL
                lanternfish.append(CHILD_CYCLE_VAL)
    
    print(len(lanternfish))


if __name__ == "__main__":
    main()