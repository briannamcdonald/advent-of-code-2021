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


def get_winning_card_indexes(cards):
    winning_indexes = set()
    # check if any cards have won
    for i, card in enumerate(cards):
        # check rows
        for row in card:
            if all(val is True for val in row):
                winning_indexes.add(i)
        # check columns
        for j in range(len(card[0])):
            column = [row[j] for row in card]
            if all(val is True for val in column):
                winning_indexes.add(i)

    if len(winning_indexes) > 0:
        return winning_indexes
    return None



def main():
    data = open("day04/input.txt", "r")
    lines = [line for line in data]
    drawn_nums, cards = organize_data(lines)

    winning_card_indexes = None
    winning_drawn_num = 0

    # remove winning cards from the list of cards until there is one left
    for drawn_num in drawn_nums:
        mark_cards(drawn_num, cards)
        winning_card_indexes = get_winning_card_indexes(cards)
        if winning_card_indexes is not None:
            winning_card_indexes = sorted(list(winning_card_indexes), reverse=True)
            if len(cards) > 1:
                for index in winning_card_indexes:
                    del cards[index]
            elif len(cards) == 1:
                winning_drawn_num = drawn_num
                break
    
    winning_card = cards[winning_card_indexes[0]]
    unmarked_nums_sum = 0
    # get the sum of unmarked numbers for the winning card
    for row in winning_card:
        for val in row:
            if type(val) != bool:
                unmarked_nums_sum += val

    print(winning_drawn_num * unmarked_nums_sum)
    

if __name__ == "__main__":
    main()