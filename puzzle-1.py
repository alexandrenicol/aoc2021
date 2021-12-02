import csv

input_data = []

output_data = []

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
        if i == 0:
            output_data.append([input_data[i], "NA"])
            na_count += 1
        else:
            previous_data = input_data[i - 1]
            current_data = input_data[i]

            if int(current_data) > int(previous_data):
                output_data.append([input_data[i], "increase"])
                increase_count += 1
            elif int(current_data) < int(previous_data):
                output_data.append([input_data[i], "decrease"])
                decrease_count += 1
            else:
                output_data.append([input_data[i], "stable"])
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
