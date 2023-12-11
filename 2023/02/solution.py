from pathlib import Path
import re

def count_colors(line):
    # Define regular expressions for game_id as well as red, blue, and green counts
    game_id_pattern = r'Game (\d+):'
    red_pattern = r'(\d+) red'
    blue_pattern = r'(\d+) blue'
    green_pattern = r'(\d+) green'

    # Initialize counts
    red_count = 0
    blue_count = 0
    green_count = 0

    # Find game_id
    game_id = list(map(int, re.findall(game_id_pattern, line)))[0]

    # Find red, blue, and green counts using regex and converting all the list elements to integers
    red_matches = list(map(int, re.findall(red_pattern, line)))
    blue_matches = list(map(int, re.findall(blue_pattern, line)))
    green_matches = list(map(int, re.findall(green_pattern, line)))

    # Sum counts from matches
    # if red_matches:
    #     red_count = sum(map(int, red_matches))
    # if blue_matches:
    #     blue_count = sum(map(int, blue_matches))
    # if green_matches:
    #     green_count = sum(map(int, green_matches))

    #return game_id, red_count, blue_count, green_count
    return game_id, red_matches, blue_matches, green_matches

def check_if_possible(line, red_lim, blue_lim, green_lim):
    # Check if the game is possible. If it is return the game_id, else return 0.
    game_id, reds, blues, greens = count_colors(line)
    #print(f"Reds: {reds}, Blues")
    if all(red <= red_lim for red in reds) & all(green <= green_lim for green in greens) & all(blue <= blue_lim for blue in blues):
        return game_id
    else:
        return 0

def find_power(line):
    # Get the lists
    game_id, reds, blues, greens = count_colors(line)
    return max(reds)*max(blues)*max(greens)

def main():
    data_folder = Path(".").resolve()
    data = data_folder.joinpath('2023').joinpath('02').joinpath('input.txt')

    possible_game_ids_1 = []
    power_sum = []

    red_lim_1 = 12
    blue_lim_1 = 14
    green_lim_1 = 13
    
    # Open the text file for reading
    with open(data, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            
            pos_id_1 = check_if_possible(line=line, red_lim=red_lim_1, blue_lim=blue_lim_1, green_lim=green_lim_1)
            if pos_id_1 > 0:
                possible_game_ids_1.append(pos_id_1)

            power_sum.append(find_power(line))

    print("Part 1")
    print(f"The sum of all the possible game IDs are {sum(possible_game_ids_1)}")
    print()

    print("Part 2")
    print(f"The sum of all the powers are {sum(power_sum)}")
    print()
            
if __name__ == "__main__":
    main()