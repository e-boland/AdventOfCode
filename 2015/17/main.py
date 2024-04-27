from itertools import combinations
import numpy as np


def get_input():
    with open("input.txt") as f:
        content = f.readlines()
        clean_content = list()
        for num in content:
            clean_num = int(num.replace("\n", ""))
            clean_content.append(clean_num)
    return clean_content


def part1(combi, volume):
    combi.sort(reverse=True)  # sorting input in descending order
    all_combinations = [list(combo) for r in range(1, len(combi) + 1) for combo in combinations(combi, r)]

    valid_combinations = 0
    for combi in all_combinations:
        result = 0
        i = 0
        while result <= volume and i < len(combi):
            result += combi[i]
            i += 1
        if result == volume:
            valid_combinations += 1

    return valid_combinations


def part2(combi, volume):

    valid_combinations = list()
    r = 1
    while not valid_combinations and r < len(combi):
        for combo in combinations(combi, r):
            if np.sum(combo) == volume:
                valid_combinations.append(combo)
        r += 1

    return len(valid_combinations)


def main():
    # print(part1([20, 5, 10, 15, 5], 25))
    # print(part1(get_input(), 150))
    print(part2([20, 5, 10, 15, 5], 25))
    print(part2(get_input(), 150))


if __name__ == "__main__":
    main()


"""
    OLD PART 2 :
    all_combinations = list()
    for r in range(1, len(combi)):  # r in range (1 - 5)
        comb_this_len = list()
        for combo in combinations(combi, r):  # r is the wanted length of the combination
            comb_this_len.append(combo)
        all_combinations.append(comb_this_len)

    valid_combinations = 0
    i = 0
    while not valid_combinations and i < len(all_combinations):
        j = 0
        while j < len(all_combinations[i]):
            if np.sum(all_combinations[i][j]) == volume:
                valid_combinations += 1
            j += 1
        i += 1

    return valid_combinations
"""