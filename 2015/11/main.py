"""
incrementing of one letter until it meets all the conditions (while):
 - no i, o or l => 23 letters :
   always True since I removed those letters from the start
 - three letters following like abc or pqr :
 - two double letters non overlapping like aa or cc :
"""

import string
from time import time  # To know the processing speed of my code.


def part1(password: str = "aaaaaaaa"):
    start = time()  # To know the processing speed of my code

    alphabet = list(string.ascii_lowercase)
    unwanted_letters = {"i", "o", "l"}
    wanted_letters = [letter for letter in alphabet if letter not in unwanted_letters]
    pw = list(password)  # to be hashable

    dic = dict()  # keys are the letters and values are numbers (from 0 to 22)
    i = 0
    for letter in wanted_letters:
        dic[letter] = i
        i += 1
    reverse_dic = {value: letter for letter, value in dic.items()}  # keys are the numbers and values are the letters

    both_conditions = False
    loop = 0

    while not both_conditions:
        condition_1 = False
        condition_2 = False

        #  TEST condition_1:
        i = 1
        found = False
        while i <= 6 and not found:
            if dic[pw[-i - 2]] == dic[pw[-i - 1]] - 1 == dic[pw[-i]] - 2:
                found = True
            i += 1
        if found:
            condition_1 = True

        # TEST condition_2:
        i = 2
        occurrence = 0
        jump = 0
        while i <= 8 and occurrence < 2:
            if dic[pw[-i]] == dic[pw[-i + 1]]:
                occurrence += 1
                jump = 1
            i += 1 + jump
            jump = 0
        if occurrence == 2:
            condition_2 = True

        if loop > 0:  # if the old password meets the conditions it still has to change as we want a new one
            both_conditions = condition_1 and condition_2
        print(f"both conditions : {both_conditions} (C1 = {condition_1}, C2 = {condition_2})")

        if not both_conditions:  # one incrementation
            i = 1  # index
            j = 0  # index adjustor if incremented for the next letter
            stop = False

            while not stop and i <= 8:  # we ensure the password's length won't exceed 8
                new_letter = ""
                if dic.get(pw[-i]) + 1 <= 22:
                    new_letter = reverse_dic.get(dic.get(pw[-i]) + 1)
                    stop = True
                else:
                    new_letter = "a"
                    i += 1  # increment the index by one to go to the next letter for the next iteration
                    j += 1  # for the index : it's the current letter we want to change, not the next one

                pw[-i + j] = new_letter  # incrementing the current letter
                j = 0

        loop += 1

        print(f"end of loop {loop}")
        print("-"*10)

    print(time() - start)

    new_password = "".join(pw)  # convert the list back into a string

    return new_password


def main():
    print(part1("hxbxwxba"))
    print(part1(part1("hxbxwxba")))


if __name__ == "__main__":
    main()
