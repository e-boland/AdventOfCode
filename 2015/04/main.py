from hashlib import md5


def part1(code="yzbqklnj", n=5):
    found = False
    i = 0
    while not found:
        test = code + str(i)
        if ((md5(test.encode())).hexdigest()).startswith("0"*n):
            return i
        i += 1


def main():
    print(part1())
    print(part1(n=6))


if __name__ == '__main__':
    main()

