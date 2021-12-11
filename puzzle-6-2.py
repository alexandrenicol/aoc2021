from typing import List

puzzle_input = open("puzzle-input-6.txt", "r")
lines = puzzle_input.readlines()


fish_register = [0,0,0,0,0,0,0,0,0]

for line in lines:
    input_data = list(map(int, line.split(",")))

    for initial_fish_timer in input_data:
        fish_register[initial_fish_timer] += 1

print(f"Initial state: {fish_register}")

for i in range (256):
    fishes_at_zero = fish_register.pop(0)
    fish_register.append(fishes_at_zero)
    fish_register[6] = fish_register[6] + fishes_at_zero

    print(f"After {i+1} day(s): {fish_register}")

print(sum(fish_register))

