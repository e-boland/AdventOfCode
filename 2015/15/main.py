import re


def spoons_distributions(total_spoons, number_of_properties, distribution=[]):
    distributions = []
    if number_of_properties == 1:
        distribution.append(total_spoons)
        distributions.append(distribution.copy())
        distribution.pop()
    else:
        for spoons in range(1, total_spoons - number_of_properties + 2):
            distribution.append(spoons)
            distributions.extend(spoons_distributions(total_spoons - spoons, number_of_properties - 1, distribution))
            distribution.pop()
    return distributions


def part1():
    with open("input.txt") as f:
        ingredients = f.readlines()

    all_stats = list()

    for ingredient in ingredients:
        stats = re.findall(r"-?\d+", ingredient)  # a list with all the ingredient's stats
        for i in range(len(stats)):  # converting into integers
            stats[i] = int(stats[i])
        all_stats.append(stats)  # a list with each ingredient's stats

    # generating a list with all the possible spoons distributions:
    all_distributions = spoons_distributions(100, 4)
    best_result = 0
    best_distribution = []

    for distribution in all_distributions:

        # multiplying each ingredient's stats by its given spoons:
        mult = [[] for idx in range(len(all_stats))]
        for i in range(len(all_stats)):
            for j in range(len(distribution)+1):  # len(distribution) = 4 but there are 5 stats, so we need 5 (len +1)
                mult[i] += [distribution[i] * all_stats[i][j]]

        # sum of each ingredient's stat for each type of stat:
        all_sum = []
        for i in range(5):
            stat_sum = max(0, (mult[0][i] + mult[1][i] + mult[2][i] + mult[3][i]))  # if < 0 => =0
            all_sum.append(stat_sum)

        calories = all_sum[4]
        if calories == 500:
            # multiplying the resulting stats with each other:
            result = all_sum[0] * all_sum[1] * all_sum[2] * all_sum[3]  # result of this distribution

            if result > best_result:
                best_result = result
                best_distribution = distribution

    return best_result, best_distribution


def main():
    print(part1())


if __name__ == "__main__":
    main()
