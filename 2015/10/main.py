"""
TEST : starting_num = 1, process = 5 :
    11  first process : OK
    21  second process : OK
    1211  third process : OK
    111221  forth process : OK
    312211  fifth process : OK
    13112221 sixth process : OK
"""


def part1(starting_num: int = 1, process: int = 1):
    num = str(starting_num)  # starting num

    for _ in range(process):  # number of process
        new_num = ""
        i = 0  # char index in num

        while i < len(num)-1:  # while every char of ths num aren't checked
            n = 1  # number of successive occurrences for one char

            while i+n < len(num) and num[i] == num[i + n]:  # while current char is the same as the n next chars
                n += 1

            new_num += str(n) + num[i]
            i += n  # go to next char after i+n (for the next iteration)

        if i == len(num)-1:  # if last num is a single occurrence (otherwise it would be i == len(num))
            new_num += "1" + num[i]

        num = new_num  # taking the new num for next process iteration

    return len(num)


def main():
    print(part1(3113322113, 50))


if __name__ == "__main__":
    main()
