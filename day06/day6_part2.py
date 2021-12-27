def organize_data(lines):
    lanternfish = [int(fish.strip()) for fish in lines[0].split(",")]
    lanternfish_counter = [0]*9

    for fish in lanternfish:
        lanternfish_counter[fish] += 1

    return lanternfish_counter


def main():
    data = open("day06/input.txt", "r")
    lines = [line for line in data]
    lanternfish_counter = organize_data(lines)
    
    NUM_OF_DAYS = 256
    ADULT_CYCLE_VAL = 6
    CHILD_CYCLE_VAL = 8
    for _ in range(NUM_OF_DAYS):
        num_new_fish = lanternfish_counter[0]
        lanternfish_counter = lanternfish_counter[1:] + lanternfish_counter[:1]
        lanternfish_counter[CHILD_CYCLE_VAL] = num_new_fish
        lanternfish_counter[ADULT_CYCLE_VAL] += num_new_fish
    
    print(sum(lanternfish_counter))


if __name__ == "__main__":
    main()