def organize_data(lines):
    drawn_nums = [int(draw_num.strip()) for draw_num in lines[0].split(",")]
    
    cards = []
    num_cards = 0
    # create a 2d list for each bingo card
    for i in range(1, len(lines)):
        if lines[i] == '\n':
            cards.append([])
            num_cards += 1
        else:
            row = []
            for val in lines[i].split(' '):
                if val.strip() != '':
                    row.append(int(val.strip()))
            cards[num_cards - 1].append(row)
    
    return drawn_nums, cards


def mark_cards(drawn_num, cards):
    # mark the drawn numbers as True to keep track of them
    for i, card in enumerate(cards):
        for j, row in enumerate(card):
            for k, val in enumerate(row):
                if val == drawn_num:
                    cards[i][j][k] = True


def get_winning_card_index(cards):
    # check if any cards have won
    for i, card in enumerate(cards):
        # check rows
        for row in card:
            if all(val is True for val in row):
                return i
        # check columns
        for j in range(len(card[0])):
            column = [row[j] for row in card]
            if all(val is True for val in column):
                return i
    return None



def main():
    data = open("day04/input.txt", "r")
    lines = [line for line in data]
    drawn_nums, cards = organize_data(lines)

    winning_card_index = None
    winning_drawn_num = 0
    
    for drawn_num in drawn_nums:
        mark_cards(drawn_num, cards)
        winning_card_index = get_winning_card_index(cards)
        if winning_card_index is not None:
            winning_drawn_num = drawn_num
            break
    
    winning_card = cards[winning_card_index]
    unmarked_nums_sum = 0
    # get the sum of unmarked numbers for the winning card
    for row in winning_card:
        for val in row:
            if type(val) != bool:
                unmarked_nums_sum += val

    print(winning_drawn_num * unmarked_nums_sum)


if __name__ == "__main__":
    main()