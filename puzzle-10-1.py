puzzle_input = open("puzzle-input-10.txt", "r")
lines = puzzle_input.readlines()


opening_brackets = ["[", "(", "{", "<"]
closing_brackets = ["]", ")", "}", ">"]

corrupt_brackets = []

scores = {"]": 57, "}": 1197, ")": 3, ">": 25137}


def brackets_match(open_bracket, close_bracket):
    if open_bracket == "[" and close_bracket == "]":
        return True
    if open_bracket == "(" and close_bracket == ")":
        return True
    if open_bracket == "{" and close_bracket == "}":
        return True
    if open_bracket == "<" and close_bracket == ">":
        return True
    return False


for line in lines:
    nLine = list(str(line.strip()))
    # print(nLine)

    opening_bracket_list = []

    for bracket in nLine:
        if bracket in opening_brackets:
            opening_bracket_list.append(bracket)

        if bracket in closing_brackets:
            last_open_bracket = opening_bracket_list[-1]

            if brackets_match(last_open_bracket, bracket):
                opening_bracket_list.pop()
            else:
                # corrupt
                print("corrupt brackets")
                corrupt_brackets.append(bracket)
                break

print(corrupt_brackets)

final_score = 0
for bracket in corrupt_brackets:
    final_score += scores[bracket]

print(final_score)
