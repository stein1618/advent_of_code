from pathlib import Path
import re

# assume all strings are nice
# remove if not enough vowels
# remove if no doubles
# remove if contains naughty strings


def is_nice_string_part_1(s):
    # Check if the string contains at least three vowels (aeiou)
    if len(re.findall(r'[aeiou]', s)) < 3:
        return False

    # Check if the string contains at least one letter that appears twice in a row
    if not re.search(r'(.)\1', s):
        return False

    # Check if the string does not contain the forbidden substrings
    if re.search(r'ab|cd|pq|xy', s):
        return False

    # If all conditions are met, the string is nice
    return True

def is_nice_string_part_2(s):
    # Check for a pair of any two letters that appears at least twice in the string without overlapping.
    # We use a regular expression with capturing groups to find such pairs.
    pair_pattern = re.compile(r'(..).*\1')
    
    # Check for a letter that repeats with exactly one letter between them.
    repeat_pattern = re.compile(r'(.).\1')
    
    # Check if both conditions are met for the given string.
    if pair_pattern.search(s) and repeat_pattern.search(s):
        return True
    else:
        return False





def main():
    
    # Read the input strings
    data_folder = Path(".").resolve()
    data = data_folder.joinpath('05','input.txt')
    with open(data, 'r') as file:
        lines = file.readlines()

    nice_count_1 = 0
    nice_count_2 = 0

    # Check each input string
    for line in lines:
        if is_nice_string_part_1(line.strip()):
            nice_count_1 += 1
        if is_nice_string_part_2(line.strip()):
            nice_count_2 += 1

    print("Number of nice strings with part 1 instrucitons:", nice_count_1)
    print("Number of nice strings with part 2 instrucitons:", nice_count_2)


    
    print("Part 1")
    print(f"There are {nice_count_1} nice strings following the 1st set of instructions.")
    print()

    print("Part 2")
    print(f"There are {nice_count_2} nice strings following the 2nd set of instructions.")
    print()

  


if __name__ == "__main__":
    main()