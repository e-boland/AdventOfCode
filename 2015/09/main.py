from itertools import permutations


def part1():
    with open("input.txt") as f:
        content = f.readlines()

    city_pairs = dict()
    all_cities = set()

    for line in content:
        city_1, _, city_2, _, path_dist = line.split()

        all_cities.add(city_1)
        all_cities.add(city_2)

        if city_1 not in city_pairs.keys():
            city_pairs[city_1] = {city_2: int(path_dist)}
        elif city_2 not in city_pairs[city_1].keys():
            city_pairs[city_1][city_2] = int(path_dist)

        if city_2 not in city_pairs.keys():
            city_pairs[city_2] = {city_1: int(path_dist)}
        elif city_1 not in city_pairs[city_2].keys():
            city_pairs[city_2][city_1] = int(path_dist)

    cities = list(all_cities)  # a list with all the different cities (n)
    all_paths = list(permutations(cities))  # all the different paths possible for the n cities (!n)

    best_dist = 0
    longest_dist = 0

    for path in all_paths:
        path_dist = 0

        for i in range(len(path) - 1):  # the cumulative distance between all the cities for this path
            path_dist += city_pairs[path[i]][path[i + 1]]  # the distance between city_i and city_i+1

        if best_dist == 0 or path_dist < best_dist:
            best_dist = path_dist

        if path_dist > longest_dist:
            longest_dist = path_dist

    return best_dist, longest_dist


def main():
    print(part1())


if __name__ == "__main__":
    main()
