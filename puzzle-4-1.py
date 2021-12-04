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

winning_table = None
bingo_numbers_out = []

for i in range(len(bingo_numbers)):

    if winning_table is not None:
        break

    bingo_numbers_out = bingo_numbers[: i + 1]

    for bingo_table in bingo_tables:

        np_bingo_table = np.array(bingo_table)

        if winning_table is not None:
            break

        # check rows
        for row_index in range(np_bingo_table.shape[0]):

            if winning_table is not None:
                break

            row_numbers = list(np_bingo_table[row_index, :])

            if all(elem in bingo_numbers_out for elem in row_numbers):
                # BINGO!
                print("BINGO")
                winning_table = np_bingo_table.copy()
                # pass

        # check columns
        for column_index in range(np_bingo_table.shape[1]):

            if winning_table is not None:
                break

            column_numbers = list(np_bingo_table[:, column_index])

            if all(elem in bingo_numbers_out for elem in column_numbers):
                # BINGO!
                print("BINGO")
                winning_table = np_bingo_table.copy()
                # pass

## bingo
print(bingo_numbers_out)
print(winning_table)

# last number called
last_number_called = bingo_numbers_out[-1]

## get sum of all unmarked numbers

winning_table_number = list(winning_table.flatten())

print(winning_table_number)
wining_table_number_not_called = [
    x for x in winning_table_number if x not in bingo_numbers_out
]
print(wining_table_number_not_called)
print(sum(wining_table_number_not_called))
print(last_number_called)

print(sum(wining_table_number_not_called) * last_number_called)
