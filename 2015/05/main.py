
def part1():
    with open("input.txt") as f:
        strings = f.readlines()
    i = 0
    vowels = "aeiou"
    banned = ["ab", "cd", "pq", "xy"]

    for string in strings:
        condition1 = False
        condition2 = False
        condition3 = False

        n = 0
        for letter in string:
            if letter in vowels:
                n += 1
        if n >= 3:
            condition1 = True

        """
        found = False
        for element in banned:
            if element in string:
                found = True
        if not found:
            condition2 = True
        """

        found = False
        index = 0
        while index < len(banned) and not found:
            if banned[index] in string:
                found = True
            index += 1
        if not found:
            condition2 = True

        previous_letter = ""
        for letter in string:
            if letter == previous_letter:
                condition3 = True
            previous_letter = letter

        all_conditions = condition1 and condition2 and condition3
        if all_conditions:
            i += 1

    return i


def part2():
    with open("input.txt") as f:
        strings = f.readlines()
    i = 0

    for string in strings:
        condition1 = False
        condition2 = False

        duos = dict()
        key_check = []
        value_check = []

        previous_letter = ""
        index = 0
        for letter in string:
            if previous_letter:
                duo = previous_letter + letter
                duos[index] = duo
                index += 1
            previous_letter = letter
        for key, value in duos.items(): # while ?
            key_check.append(key)
            if value not in value_check or (value in value_check and duos[key] == duos[key-1]):
                value_check.append(value)
        if len(value_check) != len(key_check): # pas nécessaire, = si value pas append
            condition1 = True

        previous_letter = ""
        pre_previous_letter = ""

        for letter in string:   # à transformer en while
            if letter == pre_previous_letter:
                condition2 = True
            pre_previous_letter = previous_letter
            previous_letter = letter

        all_conditions = condition1 and condition2
        if all_conditions:
            i += 1

    return i



def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()