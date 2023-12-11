from pathlib import Path
import re

def find_numbers_with_symbols(grid, symbols):
    # Define characters to ignore. If it's a different character it's a symbol
    #symbols_to_check = ['*', '#', '+', '$']
    symbols_to_check = symbols

    # Initialize a list to store numbers with nearby symbols
    numbers_with_symbols = []

    # Iterate through each row in the grid
    for row_no, row in enumerate(grid):
        col_no = 0
        while col_no < len(row):
            if row[col_no].isdigit():
                # Find the starting and ending column for the number
                col_no_min = col_no
                col_no_max = col_no
                while col_no_max + 1 < len(row) and row[col_no_max + 1].isdigit():
                    col_no_max += 1

                # Check the nearby box for symbols
                nearby_symbols = []
                symbol_position = []
                for r in range(max(0, row_no - 1), min(len(grid), row_no + 2)):
                    for c in range(max(0, col_no_min - 1), min(len(row), col_no_max + 2)):
                        if grid[r][c] in symbols_to_check:
                            nearby_symbols.append(grid[r][c])
                            symbol_position.append((r,c))

                if nearby_symbols:
                    # Extract the multi-digit number
                    #number_str = row[col_no:col_no_max + 1]
                    number_str = ''.join(row[col_no:col_no_max + 1])
                    number = int(number_str)
                    numbers_with_symbols.append((number, nearby_symbols, symbol_position))

                # Update the column pointer
                col_no = col_no_max + 1
            else:
                # Skip non-digit characters
                col_no += 1

    return numbers_with_symbols
    

def main():
    data_folder = Path(".").resolve()
    data = data_folder.joinpath('2023').joinpath('03').joinpath('input.txt')

    grid = []

    with open(data, 'r') as file:

        text = file.read()
        grid = [list(line.strip()) for line in text.split('\n')]

        # Remove periods, digits [0-9], and newline characters from the text
        cleaned_text = ''.join(char for char in text if not char.isdigit() and char != '.' and char != '\n')

        # Find unique remaining symbols
        unique_symbols = list(set(cleaned_text))

        
    # Call the function to find numbers with nearby symbols
    result = find_numbers_with_symbols(grid, unique_symbols)
    sum_of_part_numbers = 0

    print(result)

    # # Print the result
    # for number, symbols in result:
    #     print(f"Number {number} has nearby symbols: {', '.join(symbols)}")
    #     sum_of_part_numbers += number


    # print("Part 1")
    # print(f"The sum of all the part numbers are {sum_of_part_numbers}")
    # print()

   
            
if __name__ == "__main__":
    main()

#  Jeg lurte på om vi skulle spille litt mer på magefølelse-temaet?
# Jeg kan printe ut noen kort med logoen vår med en QR-kode bakpå. Det blir et lotteri hvor man i ren tekstform får beskjed om hva man har vunnet:
# - klem fra Stein
# - planke fra Lise Maren
# -

 # print("Part 2")
    # print(f"The sum of all the powers are {sum(power_sum)}")
    # print()