from pathlib import Path
import re

numbers_dict = {
    
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}

def find_calibration_value(instrs):
    # Strip all non-numeric characters
    digits = re.sub(r"\D", "", instrs)
    calibration_value = int(digits[0] + digits[-1])
    
    return calibration_value

def translate_string_digits(instrs):
    # Define dictionary for all insertions.
    # I need to keep the text on both sides of the digit in case there are overlapping string numbers on either sides
    numbers_dict = {
        'one' : 'one1one',
        'two' : 'two2two',
        'three' : 'three3three',
        'four' : 'four4four',
        'five' : 'five5five',
        'six' : 'six6six',
        'seven' : 'seven7seven',
        'eight' : 'eight8eight',
        'nine' : 'nine9nine'
    }

    
    # Replace character strings with integers
    for key in numbers_dict.keys():
        instrs = instrs.lower().replace(key, numbers_dict[key])
    
    return instrs

def main():
    data_folder = Path(".").resolve()
    data = data_folder.joinpath('01').joinpath('input.txt')
    
    # Initialize lists to hold all the calibration values
    calibration_values_1 = []
    calibration_values_2 = []

    # Open the text file for reading
    with open(data, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            
            # Find the current lines calibration values for part 1
            cv_1 = find_calibration_value(line)
            
            # Find the current lines calibration values for part 2
            # Start by translating sub-strings to digits
            cv_2 = find_calibration_value(translate_string_digits(line))
            
            # Append current lines calibration values to their respective lists
            calibration_values_1.append(cv_1)
            calibration_values_2.append(cv_2)

            # print(line)
            # print(translate_string_digits(line))
            # print(find_calibration_value(translate_string_digits(line)))
            # print()
            # print()
            # print()


    print("Part 1")
    print(f"The sum of all the calibration values are {sum(calibration_values_1)}")
    print()

    print("Part 2")
    print(f"The sum of all the calibration values are {sum(calibration_values_2)}")
    print()


if __name__ == "__main__":
    main()