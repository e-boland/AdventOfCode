
def part1():
    with open('input.txt') as f:
        content = f.read()
    position = [0, 0]
    all_positions = set()
    for char in content:
        if char == '^':
            position[0] += 1
        elif char == 'v':
            position[0] -= 1
        elif char == '>':
            position[1] += 1
        elif char == '<':
            position[1] -= 1
        all_positions.add(tuple(position))
    return len(all_positions)


def part2():
    with open('input.txt') as f:
        content = f.read()
    position_santa = [0, 0]
    position_robot = [0, 0]
    all_positions = set()
    for char in content[::2]:
        if char == '^':
            position_santa[0] += 1
        elif char == 'v':
            position_santa[0] -= 1
        elif char == '>':
            position_santa[1] += 1
        elif char == '<':
            position_santa[1] -= 1
        all_positions.add(tuple(position_santa))
    for char in content[1::2]:
        if char == '^':
            position_robot[0] += 1
        elif char == 'v':
            position_robot[0] -= 1
        elif char == '>':
            position_robot[1] += 1
        elif char == '<':
            position_robot[1] -= 1
        all_positions.add(tuple(position_robot))
    return len(all_positions)


def part2_pilpil():
    with open('input.txt') as f:
        content = f.read()
    positions = [[0, 0], [0, 0]]
    all_positions = set()
    for index, char in enumerate(content):
        current = index % 2  # = 0 if even index (santa) and = 1 if odd index (robot)
        if char == '^':
            positions[current][0] += 1
        elif char == 'v':
            positions[current][0] -= 1
        elif char == '>':
            positions[current][1] += 1
        elif char == '<':
            positions[current][1] -= 1
        all_positions.add(tuple(positions[current]))
    return len(all_positions)


def main():
    print(part1())
    print(part2())
    print(part2_pilpil())


if __name__ == '__main__':
    main()
