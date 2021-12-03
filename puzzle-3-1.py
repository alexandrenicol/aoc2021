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

    for i in range(0, transpose.shape[0]):
        bincount = np.bincount(transpose[i, :].A1)

        if bincount[0] > bincount[1]:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    print(gamma_rate)
    print(epsilon_rate)

    gamma_decimal = int(gamma_rate, 2)
    epsilon_decimal = int(epsilon_rate, 2)

    print(gamma_decimal)
    print(epsilon_decimal)

    print(gamma_decimal * epsilon_decimal)
