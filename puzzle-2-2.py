import csv

# input_data = []

output_data = []


# def get_depth(index, raw_data):
#     range_min = index - 2
#     range_max = index + 1

#     range_raw_data = raw_data[range_min:range_max]
#     range_data = map(int, range_raw_data)

#     return sum(range_data)


with open("puzzle-input-2.csv") as csvfile:
    input_data = csv.reader(csvfile, delimiter=" ")

    horizontal_count = 0
    aim_count = 0
    depth_count = 0

    for row in input_data:
        if row[0] == "forward":
            horizontal_count += int(row[1])

            depth_count = depth_count + (aim_count * int(row[1]))
        elif row[0] == "down":
            aim_count += int(row[1])
        elif row[0] == "up":
            aim_count -= int(row[1])
        else:
            pass

    print("horizontal_count")
    print(horizontal_count)
    print("aim_count")
    print(aim_count)
    print("depth_count")
    print(depth_count)
    print("total")
    print(horizontal_count * depth_count)
