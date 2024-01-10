from pathlib import Path
import re   
import numpy as np


    
def scratchcard_checker(card):
    
    # Card number
    card_number = int(card.split(': ')[0].split(' ')[-1])
    
    # Remove the leading text ("Card #:")
    cleaned_str = card.split(': ')[1]
    
    # Split the cleaned string using '|' as the delimiter
    parts = cleaned_str.split(' | ')

    # Use list comprehensions to parse the numbers and remove empty strings
    winning_numbers = [int(num) for num in parts[0].split() if num.strip()]
    your_numbers = [int(num) for num in parts[1].split() if num.strip()]

    # Calculate scratchcard value
    card_value = 0
    card_matches = 0
    for num in your_numbers:
        if num in winning_numbers:
            card_matches += 1 # used in part 2
            if card_value == 0: # used in part 1
                card_value = 1
            else:
                card_value *= 2

    return card_number, card_value, card_matches
    


def main():
    data_folder = Path(".").resolve()
    data = data_folder.joinpath('2023').joinpath('04').joinpath('input.txt')
    print(data)

    file = open(data, 'r')
    
    # Find the number of lines in the input file
    cards = file.readlines()
    no_of_cards = len(cards)

    # Create an array to hold the current number of copies for each card
    copy_status = np.full(no_of_cards,1).astype(np.int32)
    
    # Iterate through each line in the file
    total_points = 0
    for card in cards:
        card_number, card_points, card_matches = scratchcard_checker(card)
        print(card_number)
        print(card_matches)
        if card_points > 0:
            total_points += card_points
            
            # Initiate a vector of the same length as no_of_cards with zeroes
            new_copies = np.zeros(no_of_cards).astype(np.int32)            
            # If the number of copies to be received exceeds the no_of_cards we stop at the last card
            if(card_number+card_matches >= no_of_cards):
                new_copies[card_number:] = new_copies[card_number:] + copy_status[card_number-1]
            else:
                new_copies[card_number:card_number+card_matches] = new_copies[card_number:card_number+card_matches] + copy_status[card_number-1]
            
            copy_status += new_copies
            del(new_copies)
        del(card_number, card_points)
        
        print(copy_status)

    file.close()       

    print("Part 1")
    print(f"The sum of all the scratchcard points are {total_points}")
    print()


    print("Part 2")
    print(f"The number of scratchcards in the end is {sum(copy_status)}")
    print()

   
            
if __name__ == "__main__":
    main()
