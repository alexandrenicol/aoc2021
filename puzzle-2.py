import csv

input_data = []

output_data = []


def get_depth(index, raw_data):
    range_min = index - 2
    range_max = index + 1

    range_raw_data = raw_data[range_min:range_max]
    range_data = map(int, range_raw_data)

    return sum(range_data)


with open("puzzle-input-1.csv") as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        input_data.append(row[0])

    print(len(input_data))

    increase_count = 0
    decrease_count = 0
    na_count = 0
    stable_count = 0

    for i in range(len(input_data)):
        if i < 2:
            pass
        elif i == 2:

            depth = get_depth(i, input_data)

            output_data.append([depth, "NA"])
            na_count += 1
        else:
            previous_depth = get_depth(i - 1, input_data)
            current_depth = get_depth(i, input_data)

            if current_depth > previous_depth:
                output_data.append([current_depth, "increase"])
                increase_count += 1
            elif current_depth < previous_depth:
                output_data.append([current_depth, "decrease"])
                decrease_count += 1
            else:
                output_data.append([current_depth, "stable"])
                stable_count += 1

    print(len(output_data))
    print("increase_count")
    print(increase_count)
    print("decrease_count")
    print(decrease_count)
    print("na_count")
    print(na_count)
    print("stable_count")
    print(stable_count)
