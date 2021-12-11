import numpy as np


puzzle_input = open("puzzle-input-7.txt", "r")
lines = puzzle_input.readlines()


# fish_register = [0,0,0,0,0,0,0,0,0]

for line in lines:
    crab_positions = np.array(list(map(int, line.split(","))))

print(crab_positions)

print(np.median(crab_positions))

alignment_point = int(np.median(crab_positions))

total_distance = 0

for crab_position in crab_positions:
    distance = abs(crab_position - alignment_point)
    total_distance += distance


print(total_distance)

