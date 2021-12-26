def get_num_of_1s_and_0s(vals):
    # store how many times each value appears in a dictionary
    count_dict = dict()
    for val in vals:
        if val in count_dict.keys():
            count_dict[val] += 1
        else:
            count_dict[val] = 1

    return count_dict


def get_most_common_val(count_dict):
    if count_dict['0'] > count_dict['1']:
        return '0'
    return '1'


def get_least_common_val(count_dict):
    if count_dict['0'] <= count_dict['1']:
        return '0'
    return '1'


def main():
    data = open("day03/input.txt", "r")
    lines = [line.strip() for line in data]

    potential_oxygen_generator_ratings = lines.copy()
    potential_co2_scrubber_ratings = lines.copy()

    bin_string_length = len(lines[0])
    for i in range(bin_string_length):
        if len(potential_oxygen_generator_ratings) == 1 and len(potential_co2_scrubber_ratings) == 1: break
        
        if len(potential_oxygen_generator_ratings) > 1:
            vals = [bin_string[i] for bin_string in potential_oxygen_generator_ratings]
            count_dict = get_num_of_1s_and_0s(vals)
            potential_oxygen_generator_ratings = [rating for rating in potential_oxygen_generator_ratings if rating[i] == get_most_common_val(count_dict)]
        if len(potential_co2_scrubber_ratings) > 1:
            vals = [bin_string[i] for bin_string in potential_co2_scrubber_ratings]
            count_dict = get_num_of_1s_and_0s(vals)
            potential_co2_scrubber_ratings = [rating for rating in potential_co2_scrubber_ratings if rating[i] == get_least_common_val(count_dict)]

    print(int(potential_oxygen_generator_ratings[0], 2) * int(potential_co2_scrubber_ratings[0], 2))


if __name__ == "__main__":
    main()