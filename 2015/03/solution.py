from pathlib import Path


# (0,0) er første posisjon med gave. Så endres det avhengig av neste karakter i strengen. 
# lagre hver posisjon som en tuple i en liste for hvert flytt
# telle antall unike posisjoner til slutt

def find_house_locations(instrs):
    # Initialize list with start location to store all house locations (as tuples)
    house_locations = [(0,0)]
    
    # Iterate through the list of directions
    for char in instrs:
        last_location = house_locations[-1]

        # Modify the last location tuple with the new instructions
        if char == '<':
            new_location = (last_location[0] - 1, last_location[1])
        elif char == '>':
            new_location = (last_location[0] + 1, last_location[1])
        elif char == '^':
            new_location = (last_location[0], last_location[1] + 1)
        elif char == 'v':
            new_location = (last_location[0], last_location[1] - 1)

        # Add the new location to the list of houses        
        house_locations.append(new_location)
        
    return house_locations

def count_unique_house_locations(house_locations):
    # Convert the list of tuples to a set to remove duplicates
    unique_house_locations = set(house_locations)

    # Count the distinct house locations tuples
    distinct_houses = len(unique_house_locations)
    
    return distinct_houses

    
def find_santa_and_robo_houses(instrs):
    # Split the input into odd and even instructions. The odd ones go to Santa and the even go to Robo-Santa
    santa_instrs = instrs[::2]  # Characters at even positions
    robo_instrs = instrs[1::2]  # Characters at odd positions
    
    # Find house locations for Santa and Robo-Santa separately
    santa_house_locations = find_house_locations(santa_instrs)
    robo_house_locations = find_house_locations(robo_instrs)

    # Combine the house locations of Santa and Robo-Santa
    combined_house_locations = santa_house_locations + robo_house_locations

    return combined_house_locations

def main():
    data_folder = Path(".").resolve()
    data = data_folder.joinpath("04","input.txt").read_text()
    
    print("Part 1")
    print(f"The instructions says Santa needs to visit {count_unique_house_locations(find_house_locations(data))} distinct houses.") # The instructions says Santa needs to visit 2572 distinct houses.
    print()

    print("Part 2")
    print(f"The instructions says Santa and Robo-Santa need to visit {count_unique_house_locations(find_santa_and_robo_houses(data))} distinct houses.") # The instructions says Santa and Robo-Santa need to visit 2572 distinct houses.
    print()
    


if __name__ == "__main__":
    main()