import csv
import numpy as np

input_data = []

gamma_rate = ""
epsilon_rate = ""

with open("puzzle-input-3.csv") as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        data = list(map(int, list(row[0])))
        input_data.append(data)

    matrix = np.matrix(input_data)
    transpose = np.matrix.transpose(matrix)

    oxygen_matrix = np.array(transpose.copy())
    oxygen_index = 0
    c02_matrix = np.array(transpose.copy())
    c02_index = 0

    # oxygen rating - most common
    while oxygen_matrix.shape[1] > 1:

        print(oxygen_matrix.shape)

        bincount = np.bincount(oxygen_matrix[oxygen_index, :])

        if len(bincount) > 1 and bincount[0] > bincount[1]:
            # more zeros, keep zeros
            oxygen_matrix = np.array(
                oxygen_matrix[:, oxygen_matrix[oxygen_index, :] < 1]
            )
        else:

            oxygen_matrix = np.array(
                oxygen_matrix[:, oxygen_matrix[oxygen_index, :] > 0]
            )
            # more ones, or equal, keep ones

        oxygen_index += 1

    # co2 rating - least common
    while c02_matrix.shape[1] > 1:

        print(c02_matrix.shape)

        bincount = np.bincount(c02_matrix[c02_index, :])

        if len(bincount) > 1 and bincount[0] > bincount[1]:
            # more zeros, keep ones
            c02_matrix = np.array(c02_matrix[:, c02_matrix[c02_index, :] > 0])
        else:
            # more ones, or equal keep zeros
            c02_matrix = np.array(c02_matrix[:, c02_matrix[c02_index, :] < 1])

        c02_index += 1

    print(oxygen_matrix.shape)
    print(c02_matrix.shape)

    oxygen_rate = "".join(list(map(str, list(oxygen_matrix[:, 0]))))
    c02_rate = "".join(list(map(str, list(c02_matrix[:, 0]))))

    oxygen_decimal = int(oxygen_rate, 2)
    c02_decimal = int(c02_rate, 2)

    print(oxygen_decimal)
    print(c02_decimal)

    print(oxygen_decimal * c02_decimal)
