from re import findall
from time import time  # To know the processing speed of my code.


def part1():
    start = time()  # To know the processing speed of my code
    lights = [[] for _ in range(1000)]
    x = 0
    y = 0
    while x < 1000:
        while y < 1000:
            lights[x].append((x, y))    # Actually, the index in the list is the same as the positions (x, y)
            y += 1
        y = 0
        x += 1

    with open("input.txt") as f:
        instructions = f.readlines()  # list where each element is a lign of instructions

    lights_setting = dict()
    for row in lights:
        for coord in row:
            lights_setting[coord] = False  # False = turned off et True = turned on

    for line in instructions:
        x_a, y_a, x_b, y_b = findall(r'\d+', line)  # extracts the numbers from a string
        xa, ya, xb, yb = int(x_a), int(y_a), int(x_b), int(y_b)
        x = xa
        y = ya

        if line.startswith("turn on"):
            while x <= xb:
                while y <= yb:
                    lights_setting[(x, y)] = True
                    y += 1
                y = ya
                x += 1

        elif line.startswith("turn off"):
            while x <= xb:
                while y <= yb:
                    lights_setting[(x, y)] = False
                    y += 1
                y = ya
                x += 1

        elif line.startswith("toggle"):
            while x <= xb:
                while y <= yb:
                    if not lights_setting[(x, y)]:
                        lights_setting[(x, y)] = True
                    else:
                        lights_setting[(x, y)] = False
                    y += 1
                y = ya
                x += 1

    lit = 0
    for value in lights_setting.values():
        if value:
            lit += 1

    print(time() - start)
    return lit


def part1_pilpil():
    start = time()  # To know the processing speed of my code
    n = 1000
    lights = [[0] * n for _ in range(n)]  # The index actually corresponds to the position (x,y) so the list can
    # contain the state of the light (0 = off, 1 = on) instead of the position. Here they're all off ([0]). So the
    # dictionary won't be needed to associate the positions to a state.

    with open("input.txt") as f:
        instructions = f.readlines()

    for line in instructions:
        x_a, y_a, x_b, y_b = findall(r'\d+', line)
        xa, ya, xb, yb = int(x_a), int(y_a), int(x_b), int(y_b)

        if line.startswith("toggle"):
            for i in range(xa, xb + 1):
                for j in range(ya, yb + 1):
                    lights[i][j] = 0 if lights[i][j] else 1
        else:
            value = 1 if line.startswith("turn on") else 0
            for i in range(xa, xb + 1):
                for j in range(ya, yb + 1):
                    lights[i][j] = value

    lit = sum(sum(line) for line in lights)
    print(time() - start)
    return lit


def part2():
    start = time()  # To know the processing speed of my code
    n = 1000
    lights = [[0] * n for _ in range(n)]

    with open("input.txt") as f:
        instructions = f.readlines()  # list where each element is a lign of instructions

    for line in instructions:
        x_a, y_a, x_b, y_b = findall(r'\d+', line)
        xa, ya, xb, yb = int(x_a), int(y_a), int(x_b), int(y_b)

        for x in range(xa, xb + 1):
            for y in range(ya, yb + 1):
                if line.startswith("turn on"):
                    lights[x][y] += 1
                elif line.startswith("toggle"):
                    lights[x][y] += 2
                elif line.startswith("turn off"):
                    lights[x][y] = max(lights[x][y] - 1, 0)

    count = 0
    for row in lights:
        for element in row:
            count += element

    print(time() - start)  # To know the processing speed of my code

    return count


def main():
    print(part2())
    print(part1_pilpil())


if __name__ == "__main__":
    main()
