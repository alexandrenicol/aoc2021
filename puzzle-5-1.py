import numpy as np

puzzle_input = open("puzzle-input-5.txt", "r")
wind_lines = puzzle_input.readlines()

ocean_floor = [[0 for i in range(0, 1000)] for i in range(0, 1000)]
# ocean_floor = [[0 for i in range(0, 10)] for i in range(0, 10)]


for line in wind_lines:
    data = line.split(" -> ")
    input = data[0]
    output = data[1]

    input_xy = list(map(int, input.split(",")))
    output_xy = list(map(int, output.split(",")))

    if (input_xy[0] == output_xy[0]) or (input_xy[1] == output_xy[1]):
        # horizontal or vertical wind ?

        min_x = min(input_xy[0], output_xy[0])
        max_x = max(input_xy[0], output_xy[0])
        min_y = min(input_xy[1], output_xy[1])
        max_y = max(input_xy[1], output_xy[1])

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                ocean_floor[x][y] += 1

    else:
        # diagonal lines
        step_x = 1 if input_xy[0] < output_xy[0] else -1
        step_y = 1 if input_xy[1] < output_xy[1] else -1
        r_x = range(input_xy[0], output_xy[0] + step_x, step_x)
        r_y = range(input_xy[1], output_xy[1] + step_y, step_y)
        for i in range(len(r_x)):
            ocean_floor[r_x[i]][r_y[i]] += 1

print(np.count_nonzero(np.array(ocean_floor) > 1))
