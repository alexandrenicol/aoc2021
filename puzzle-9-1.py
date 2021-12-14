puzzle_input = open("puzzle-input-9.txt", "r")
lines = puzzle_input.readlines()

count = 0

rows = []

risk_levels = []

for line in lines:
    column = list(map(int, list(str(line.strip()))))
    rows.append(column)

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

            # current_basin_number = []


print(sum(risk_levels))
