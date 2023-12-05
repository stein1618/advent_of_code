from pathlib import Path






def find_area(boxes):
    # Initialize variables to store the total area and the additional area from the smallest surfaces
    total_area = 0

    # Iterate through the list of boxes
    for box in boxes:
        length, width, height = box
        dimensions = [length, width, height]
        dimensions.sort()  # Sort the dimensions in ascending order
        
        # Calculate the area of the smallest surface (product of the two shortest sides)
        smallest_surface_area = dimensions[0] * dimensions[1]
        
        # Add the area of the smallest surface to the total area
        total_area += 2 * (length * width + width * height + height * length) + smallest_surface_area

    return total_area

def find_length(boxes):
    # Initialize variables to store the total area and the additional area from the smallest surfaces
    total_length = 0

    # Iterate through the list of boxes
    for box in boxes:
        length, width, height = box
        dimensions = [length, width, height]
        dimensions.sort()  # Sort the dimensions in ascending order
        
        # Calculate the area of the smallest perimeter
        smallest_perimeter = 2*dimensions[0] + 2*dimensions[1]

        # Calculate the volume of the cube for the bow ribbon length need
        bow = length*width*height
        
        # Add the area of the smallest surface to the total area
        total_length += smallest_perimeter + bow

    return total_length
    
def main():
    data_folder = Path(".").resolve()
    data = data_folder.joinpath('input.txt')
    
    # Initialize a list to store the box dimensions as tuples (l, w, h)
    boxes = []

    # Open the text file for reading
    with open(data, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into parts based on 'x' separator and convert them to integers
            parts = line.strip().split('x')
            l, w, h = map(int, parts)
            
            # Append the dimensions as a tuple to the list
            boxes.append((l, w, h))


    print("Part 1")
    print(f"The instructions says the elves need {find_area(boxes)} square feet of wrapping paper.")
    print()

    print("Part 2")
    print(f"The instructions says the elves need {find_length(boxes)} feet of ribbon.")
    


if __name__ == "__main__":
    main()