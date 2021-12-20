import numpy as np

puzzle_input = open("puzzle-input-9.txt", "r")
lines = puzzle_input.readlines()

count = 0

rows = []

risk_levels = []

for line in lines:
    column = list(map(int, list(str(line.strip()))))
    rows.append(column)

low_points = []


def get_nearby_basin_points(point, basin_index):
    x = point[0]
    y = point[1]

    nearby_points = []

    basin_points = basin_points_list[basin_index]

    point_value = rows[x][y]

    if x > 0:
        value = rows[x - 1][y]
        if value < 9 and [x - 1, y] not in basin_points:
            nearby_points.append([x - 1, y])

    if y > 0:
        value = rows[x][y - 1]
        if value < 9 and [x, y - 1] not in basin_points:
            nearby_points.append([x, y - 1])

    if y < len(rows[x]) - 1:
        value = rows[x][y + 1]
        if value < 9 and [x, y + 1] not in basin_points:
            nearby_points.append([x, y + 1])

    if x < len(rows) - 1:
        value = rows[x + 1][y]
        if value < 9 and [x + 1, y] not in basin_points:
            nearby_points.append([x + 1, y])

    for nearby_point in nearby_points:
        basin_points_list[basin_index].append(nearby_point)

    for nearby_point in nearby_points:
        get_nearby_basin_points(nearby_point, basin_index)


# get low points
for i in range(len(rows)):
    column = rows[i]
    for j in range(len(column)):
        value = rows[i][j]

        comparison_values = []

        if i > 0:
            top_value = rows[i - 1][j]
            comparison_values.append(top_value)

        if j > 0:
            left_value = rows[i][j - 1]
            comparison_values.append(left_value)

        if j < len(column) - 1:
            right_value = rows[i][j + 1]
            comparison_values.append(right_value)

        if i < len(rows) - 1:
            bottom_value = rows[i + 1][j]
            comparison_values.append(bottom_value)

        if all(x > value for x in comparison_values):
            # low point
            risk_levels.append(value + 1)

            low_points.append([i, j])


basin_sizes = []
basin_points_list = []


# get low points' basin points
for basin_index in range(len(low_points)):

    point = low_points[basin_index]
    basin_points_list.append([])
    basin_points_list[basin_index].append(point)

    get_nearby_basin_points(point, basin_index)

    basin_points = basin_points_list[basin_index]

    basin_sizes.append(len(basin_points))


# get the three largest basins
arr = np.array(basin_sizes)
arr_sorted = -np.sort(-arr, axis=0)
top_three = arr_sorted[:3]


print(top_three)


print("answer:")

print(top_three[0] * top_three[1] * top_three[2])
