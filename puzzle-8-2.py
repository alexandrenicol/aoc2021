import numpy as np


puzzle_input = open("puzzle-input-8.txt", "r")
lines = puzzle_input.readlines()

count = 0

ZERO = ["a", "b", "c", "e", "f", "g"]  # 6
ONE = ["c", "f"]  # 2
TWO = ["a", "c", "d", "e", "g"]  # 5
THREE = ["a", "c", "d", "f", "g"]  # 5
FOUR = ["b", "c", "d", "f"]  # 4
FIVE = ["a", "b", "d", "f", "g"]  # 5
SIX = ["a", "b", "d", "e", "f", "g"]  # 6
SEVEN = ["a", "c", "f"]  # 3
EIGHT = ["a", "b", "c", "d", "e", "f", "g"]  # 7
NINE = ["a", "b", "c", "d", "f", "g"]  # 6


def sort_letters(input_string):
    return "".join(sorted(input_string))


output_numbers_list = []

for line in lines:

    values = line.split("|")

    input_values = values[0].strip().split(" ")
    output_values = values[-1].strip().split(" ")

    temp_one = list(filter(lambda x: len(x) == 2, input_values))[0]
    temp_seven = list(filter(lambda x: len(x) == 3, input_values))[0]
    temp_four = list(filter(lambda x: len(x) == 4, input_values))[0]
    temp_eight = list(filter(lambda x: len(x) == 7, input_values))[0]

    two_three_five = list(filter(lambda x: len(x) == 5, input_values))
    zero_six_nine = list(filter(lambda x: len(x) == 6, input_values))

    temp_three = None

    for num in two_three_five:
        if all(item in list(num) for item in list(temp_one)):
            temp_three = num
            break

    combined_three_four = set(temp_three).union(set(temp_four))

    temp_nine = None

    for num in zero_six_nine:
        if all(item in list(num) for item in list(combined_three_four)):
            temp_nine = num

    e = list(set(temp_eight).difference(set(temp_nine)))[0]

    temp_two = None

    for num in two_three_five:
        if all(item in list(num) for item in list(e)):
            temp_two = num
            break

    temp_five = None

    for num in two_three_five:
        if num not in [temp_two, temp_three]:
            temp_five = num
            break

    zero_six = [e for e in zero_six_nine if e not in [temp_nine]]

    temp_six = None
    for num in zero_six:
        if all(item in list(num) for item in list(temp_five)):
            temp_six = num
            break

    temp_zero = [e for e in zero_six if e not in [temp_six]][0]

    zero = sort_letters(temp_zero)
    one = sort_letters(temp_one)
    two = sort_letters(temp_two)
    three = sort_letters(temp_three)
    four = sort_letters(temp_four)
    five = sort_letters(temp_five)
    six = sort_letters(temp_six)
    seven = sort_letters(temp_seven)
    eight = sort_letters(temp_eight)
    nine = sort_letters(temp_nine)

    print(zero)
    print(one)
    print(two)
    print(three)
    print(four)
    print(five)
    print(six)
    print(seven)
    print(eight)
    print(nine)

    numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

    # ----

    output_numbers = ""

    for output_value in output_values:
        output_value_sorted = sort_letters(output_value)
        output_numbers += str(numbers.index(output_value_sorted))

    print(int(output_numbers))

    output_numbers_list.append(int(output_numbers))


print(sum(output_numbers_list))
