from itertools import combinations
import numpy as np


def get_factors(num: int, end=float("inf")):
    factors = list()
    for n in range(1, int(np.sqrt(num)) + 1):
        if num % n == 0:
            if n * end >= num:
                factors.append(n)
            if (num // n) * end >= num:
                factors.append(num // n)
    return factors


def find_first_house(total_gifts: int, mult: int, end=float("inf")):
    gifts = 0
    house = 0
    while gifts < total_gifts:
        house += 1
        factors = get_factors(house, end)
        gifts = sum(factors) * mult
    return house


def find_combinations(total_gifts: int) -> list:
    """
    Find all combinations of numbers that are valid distributions of a given amount of gifts :
    - the sum of the numbers must be equal to the amount of gifts
    - every number can only be included once
    - the factors of these numbers must be previously included
    - their least common multiple must be less than the total amount of gifts

    Args:
        total_gifts (int): The total number of gifts.

    Returns:
        list: A list of lists containing valid combinations of numbers.
    """

    numbers = [i for i in range(1, total_gifts)]
    results = []

    def backtrack(remaining, path, start):
        if remaining == 0:
            if np.lcm.reduce(path) < total_gifts:
                results.append(path)
            return
        if remaining < 0:
            return
        for i in range(start, len(numbers)):
            if numbers[i] not in path:
                new_path = path + [numbers[i]]  # Include the number in the path
                factors = get_factors(numbers[i])
                found = True
                j = 0
                while found and j < len(factors) - 1:
                    found = factors[j] in path  # True or False
                    j += 1
                if not found:
                    continue
                backtrack(remaining - numbers[i], path + [numbers[i]], i + 1)

    # Ensure 1 is always included in the combinations
    if 1 <= total_gifts:
        backtrack(total_gifts - 1, [1], 0)

    return results


def find_exact_house(total_gifts: int) -> int:
    """
    Find the first exact house number that should receive the given number of gifts.

    Args:
        total_gifts (int): The total number of gifts.

    Returns:
        int: The first house number that should receive the given number of gifts.
    """
    valid_combinations = find_combinations(total_gifts)
    houses = list()
    if len(valid_combinations) > 1:  # if more than one house receive that amount of gifts
        for comb in valid_combinations:
            houses.append(comb[-1])
        house = min(houses)
    else:
        house = valid_combinations[-1][-1]

    return house


def main():
    print(find_first_house(36000000, 10))
    print(find_first_house(36000000, 11, 50))

    # gifts = 130
    # print(find_exact_house(int(gifts/10)))


if __name__ == "__main__":
    main()