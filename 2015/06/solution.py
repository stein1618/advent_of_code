from pathlib import Path
import numpy as np

# Define a function to turn on the lights within a rectangle
def turn_on_rectangle(lower_left, upper_right, light_panel):
    light_panel[lower_left[0]:upper_right[0] + 1, lower_left[1]:upper_right[1] + 1] = True
    return light_panel

# Define a function to turn off the lights within a rectangle
def turn_off_rectangle(lower_left, upper_right, light_panel):
    light_panel[lower_left[0]:upper_right[0] + 1, lower_left[1]:upper_right[1] + 1] = False
    return light_panel

# Define a function to toggle the lights within a rectangle
def toggle_rectangle(lower_left, upper_right, light_panel):
    light_panel[lower_left[0]:upper_right[0] + 1, lower_left[1]:upper_right[1] + 1] = ~light_panel[lower_left[0]:upper_right[0] + 1, lower_left[1]:upper_right[1] + 1]
    return light_panel

# Define a function to turn on the lights within a rectangle
def increase_rectangle(lower_left, upper_right, light_panel):
    light_panel[lower_left[0]:upper_right[0] + 1, lower_left[1]:upper_right[1] + 1] += 1
    return light_panel

# Define a function to turn off the lights within a rectangle
def decrease_rectangle(lower_left, upper_right, light_panel):
    light_panel[lower_left[0]:upper_right[0] + 1, lower_left[1]:upper_right[1] + 1] -= 1
    # Ensure brightness values are not below zero
    light_panel[light_panel < 0] = 0
    return light_panel

# Define a function to toggle the lights within a rectangle
def double_increase_rectangle(lower_left, upper_right, light_panel):
    light_panel[lower_left[0]:upper_right[0] + 1, lower_left[1]:upper_right[1] + 1] += 2
    return light_panel


def parse_instruction(instruction):

    parts = instruction.split()
    action = parts[0]
    start_x, start_y = map(int, parts[-3].split(','))
    end_x, end_y = map(int, parts[-1].split(','))
    return action, (start_x, start_y), (end_x, end_y)

def execute_instruction(instruction, light_panel, part):
    action, lower_left, upper_right = parse_instruction(instruction)
    if part == 1:
        if action == "turn":
            if "on" in instruction:
                turn_on_rectangle(lower_left, upper_right, light_panel)
            else:
                turn_off_rectangle(lower_left, upper_right, light_panel)
        elif action == "toggle":
            toggle_rectangle(lower_left, upper_right, light_panel)
    else:
        if action == "turn":
            if "on" in instruction:
                increase_rectangle(lower_left, upper_right, light_panel)
            else:
                decrease_rectangle(lower_left, upper_right, light_panel)
        elif action == "toggle":
            double_increase_rectangle(lower_left, upper_right, light_panel)
    
    return light_panel


def main():
    
    data_folder = Path(".").resolve()
    data = data_folder.joinpath('06','input.txt')

    # Create a 1000x1000 NumPy array of booleans initialized to False (lights off)
    light_panel_1 = np.zeros((1000, 1000), dtype=bool)
    # Create a 1000x1000 NumPy array of zeros (lights off)
    light_panel_2 = np.zeros((1000, 1000), dtype=int)
        
    # Open the text file for reading
    with open(data, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            light_panel_1 = execute_instruction(line, light_panel_1, 1)
            light_panel_2 = execute_instruction(line, light_panel_2, 2)

    # Calculate the number of lights in the "on" position in Part 1
    num_lights_on = np.count_nonzero(light_panel_1)
    # Calculate the total brightness in Part 2
    total_brightness = np.sum(light_panel_2)

    print("Part 1")
    print(f"There are {num_lights_on} lights on after all instructions have been executed.")
    print()

    print("Part 2")
    print(f"The total_brightness of the panel is {total_brightness}.")
    print()

 


if __name__ == "__main__":
    main()

# from pathlib import Path
# import numpy as np
# import re

# data_folder = Path(".").resolve()
# reg = re.compile(r"(toggle|turn on|turn off) (\d+,\d+) through (\d+,\d+)")
# class Lights:

#     def __init__(self,data):
#         self.grid_size = (1000,1000)
#         self.grid = np.zeros(self.grid_size,dtype=int)
        
#         self.instrs = []
#         for line in data.split('\n'):
#             m = reg.match(line)
#             if m is None:
#                 raise RuntimeError()
#             status = m.group(1)
#             start = [int(d) for d in m.group(2).split(',')]
#             end = [int(d)+1 for d in m.group(3).split(',')]
#             self.instrs.append([status,(start[1],end[1]),(start[0],end[0])])

#     def follow_instructions(self):
#         for instr in self.instrs:
#             y = instr[1]
#             x = instr[2]
#             if instr[0] == 'toggle':
#                 self.grid[y[0]:y[1],x[0]:x[1]] =  1-self.grid[y[0]:y[1],x[0]:x[1]]
#             elif instr[0] == 'turn on':
#                 self.grid[y[0]:y[1],x[0]:x[1]] = 1
#             else:
#                 self.grid[y[0]:y[1],x[0]:x[1]] = 0

#     def follow_instructions_brightness(self):
#         for instr in self.instrs:
#             y = instr[1]
#             x = instr[2]
#             if instr[0] == 'toggle':
#                 self.grid[y[0]:y[1],x[0]:x[1]] += 2
#             elif instr[0] == 'turn on':
#                 self.grid[y[0]:y[1],x[0]:x[1]] += 1
#             else:
#                 self.grid[y[0]:y[1],x[0]:x[1]] -= 1
#                 self.grid[self.grid < 0] = 0
    
#     def total_brightness(self):
#         return np.sum(self.grid)


# def main():
#     data = data_folder.joinpath('06','input.txt').read_text()
#     print("Part 1")
#     l = Lights(data)
#     l.follow_instructions()
#     print(f"{l.total_brightness()} lights are on after following the instructions")
#     print()
    
#     print("Part 2")
#     l = Lights(data)
#     l.follow_instructions_brightness()
#     print(f"The total brightness is {l.total_brightness()} after following the instructions")


# if __name__ == "__main__":
#     main()