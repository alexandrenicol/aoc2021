import numpy as np

puzzle_input = open("puzzle-input-4.txt", "r")
puzzle_lines = puzzle_input.readlines()

count = 0

bingo_numbers = []
bingo_tables = []
bingo_table = []

## preparing bingo game

for line in puzzle_lines:
    if count == 0:
        bingo_numbers = list(map(int, line.split(",")))
        count += 1
        continue

    if len(line) < 2:
        if len(bingo_table) > 0:
            bingo_tables.append(bingo_table)
        bingo_table = []
        continue

    bingo_table.append(
        list(map(int, filter(lambda item: len(item) > 0, line.split(" "))))
    )

# last bingo table
bingo_tables.append(np.array(bingo_table))


## game on


BINGO_TABLES_COUNT = len(bingo_tables)
winning_tables = [False for iter in range(BINGO_TABLES_COUNT)]

bingo_numbers_out = []

last_winning_number = -1
last_winning_table = -1

for i in range(len(bingo_numbers)):

    if winning_tables.count(True) == BINGO_TABLES_COUNT:
        break

    bingo_numbers_out = bingo_numbers[: i + 1]

    for j in range(len(bingo_tables)):

        bingo_table = bingo_tables[j]

        np_bingo_table = np.array(bingo_table)

        is_winning_table = winning_tables[j]

        if is_winning_table == True:
            continue

        # check rows
        for row_index in range(np_bingo_table.shape[0]):

            if is_winning_table == True:
                break

            row_numbers = list(np_bingo_table[row_index, :])

            if all(elem in bingo_numbers_out for elem in row_numbers):
                # BINGO!
                print("BINGO")
                winning_tables[j] = True
                is_winning_table = True
                last_winning_number = bingo_numbers[i]
                last_winning_table = j

        if is_winning_table == True:
            continue

        # check columns
        for column_index in range(np_bingo_table.shape[1]):

            if is_winning_table == True:
                break

            column_numbers = list(np_bingo_table[:, column_index])

            if all(elem in bingo_numbers_out for elem in column_numbers):
                # BINGO!
                print("BINGO")
                winning_tables[j] = True
                is_winning_table = True
                last_winning_number = bingo_numbers[i]
                last_winning_table = j

## bingo

print(last_winning_number)
print(bingo_tables[last_winning_table])

winning_table = np.array(bingo_tables[last_winning_table])

## get sum of all unmarked numbers

winning_table_number = list(winning_table.flatten())

wining_table_number_not_called = [
    x for x in winning_table_number if x not in bingo_numbers_out
]

print(sum(wining_table_number_not_called) * last_winning_number)
