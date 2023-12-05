from pathlib import Path
import re

def main():
    data_folder = Path(".").resolve()
    data = data_folder.joinpath('02').joinpath('input.txt')
    output = data_folder.joinpath('02').joinpath('output.txt')
    
    # Open the text file for reading
    with open(data, 'r') as file,  open(output, 'w') as output_file:
        # Iterate through each line in the file
        for line in file:
            print(line)
            sliced = line[1:line.find('"', 1)] # find the second occurence of " and slice the string. I know the first " is at position 0
            output_file.write(sliced + '\n')  # Write the extracted string to the output file

if __name__ == "__main__":
    main()