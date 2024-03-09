def part1():
    with open('input.txt') as f:
        content = f.readlines()
    total_paper = 0
    total_ribbon = 0
    for line in content:
        l, w, h = [int(n) for n in line.split('x')]  # unpacking from list comprehension
        a, b = sorted([l, w, h])[:2]
        paper = 2 * (l * w + w * h + h * l) + a * b
        ribbon = 2 * (a + b) + l * w * h
        total_paper += paper
        total_ribbon += ribbon
    return total_paper, total_ribbon


def part2():
    return


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
