import numpy as np


puzzle_input = open("puzzle-input-7.txt", "r")
lines = puzzle_input.readlines()


# fish_register = [0,0,0,0,0,0,0,0,0]

for line in lines:
    crab_positions = np.array(list(map(int, line.split(","))))

# print(crab_positions)

print(np.median(crab_positions))
print(np.average(crab_positions))

min_point = int(np.min(crab_positions))
max_point = int(np.max(crab_positions))

print(min_point)
print(max_point)


# alignment_point = np.average(crab_positions)

min_total_fuel = 999999999999999999999999999999999999

alignment_point = 0

for i in range(min_point, max_point+1):
    total_fuel = 0

    for crab_position in crab_positions:
        # fuel = sigma from 1 to distance of

        distance = abs(crab_position - i)
        # fuel = np.arange(1, distance + 1)
        # total_fuel += sum(fuel)

        # alternative after a bit of math brain power mode on, much much faster
        total_fuel += (distance ** 2 + distance) / 2 #

    if (total_fuel < min_total_fuel):
        alignment_point = i
        min_total_fuel = total_fuel

print("---")
print(alignment_point)
print(min_total_fuel)

