def part1():
    dic = {'(': 1, ')': -1}
    with open('input.txt') as f:
        content = f.read()
    result = 0
    for char in content:
        result += dic.get(char, 0)
    return result


def part2():
    dic = {'(': 1, ')': -1}
    with open('input.txt') as f:
        content = f.read()
    result = 0
    i = 0
    while result != -1 and i < len(content):
        result += dic.get(content[i], 0)
        i += 1
    return i


def part2_pilpil():
    dic = {'(': 1, ')': -1}
    with open('input.txt') as f:
        content = f.read()
    result = 0
    for index, char in enumerate(content):
        result += dic.get(char, 0)
        if result == -1:
            return index + 1
    return 0


def main():
    print(part1())
    print(part2())
    print(part2_pilpil())


if __name__ == '__main__':
    main()
