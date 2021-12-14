import numpy as np


puzzle_input = open("puzzle-input-8.txt", "r")
lines = puzzle_input.readlines()

count = 0

for line in lines:
    output_values = line.split("|")[-1].strip().split(" ")

    for output_value in output_values:
        if len(output_value) in  [2,3,4,7]:
            count += 1

print(count)
