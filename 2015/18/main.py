from copy import deepcopy
from functools import reduce
import numpy as np


def get_grid_from_str(str_input: str):
    side_len = int(np.sqrt(len(str_input)))  # length of the grid's sides
    grid = [list(str_input[i:i + side_len]) for i in range(0, len(str_input), side_len)]
    return grid


def get_grid_from_file(file_name: str):
    with open(file_name) as f:
        grid_lines = f.readlines()
    grid = [list(line.replace("\n", "")) for line in grid_lines]
    return grid


def change_corners(grid: list):
    grid[0][0] = '#'
    grid[0][-1] = '#'
    grid[-1][0] = '#'
    grid[-1][-1] = '#'
    return grid


def count_neighbours(x: int, y: int, grid):
    x_n = [x - 1, x, x + 1]
    y_n = [y - 1, y, y + 1]
    count = 0
    for i in range(len(x_n)):
        for j in range(len(y_n)):
            if i != 1 or j != 1:
                neighbour = grid[x_n[i]][y_n[j]] if x_n[i] in range(0,len(grid)) and y_n[j] in range(0, len(grid[i])) else "."
                if neighbour == "#":
                    count += 1
    return count


def change_lights(grid: list, part: int):
    if part == 2:
        grid = change_corners(grid)

    new_grid = deepcopy(grid)

    x = 0
    while x < len(grid):  # iterate each line
        y = 0

        while y < len(grid[x]):  # iterate each line's element (= each light)
            this_light = grid[x][y]
            neighbours_on = count_neighbours(x, y, grid)

            if this_light == '#':  # if ON
                if part == 2:  # PART 2 :
                    if x in (0, len(grid) - 1) and y in (0, len(grid[x]) - 1):  # if corner
                        new_grid[x][y] = '#'
                    elif neighbours_on in (2, 3):
                        new_grid[x][y] = '#'
                    else:
                        new_grid[x][y] = '.'
                else:  # PART 1 :
                    if neighbours_on in (2, 3):
                        new_grid[x][y] = '#'
                    else:
                        new_grid[x][y] = '.'

            else:  # if OFF
                if neighbours_on == 3:
                    new_grid[x][y] = '#'
                else:
                    new_grid[x][y] = '.'
            y += 1
        x += 1

    return new_grid


def count_final_lights(grid: list, steps: int, part: int):
    final_lights = reduce(lambda x, f: f(x, part), [change_lights] * steps, grid)

    count = 0
    for row in final_lights:
        for light in row:
            count += 1 if light == '#' else 0
    return count


def main():
    print(count_final_lights(get_grid_from_str(".#.#.#...##.#....#..#...#.#..#####.."), 4, 1))
    print(count_final_lights(get_grid_from_file("input.txt"), 100, 1))

    print(count_final_lights(get_grid_from_str(".#.#.#...##.#....#..#...#.#..#####.."), 5, 2))
    print(count_final_lights(get_grid_from_file("input.txt"), 100, 2))


if __name__ == "__main__":
    main()
