
def part1():
    with open("input.txt") as f:
        lines = f.read().splitlines()  # list with each line as an element

    all_removed = 0  # number of characters removed to convert current string (code) to a value string
    all_added = 0  # number of characters added to convert current string (value) to a code string

    for line in lines:
        last_char = ""
        pre_char = ""
        removed_char = 0
        added_char = 0
        spe = False
        pre_active_slash = False  # - rouge

        for char in line:

            if pre_char == 'x' and spe:
                spe = False
                if (char.isdigit() or char in 'abcdef') and (last_char.isdigit() or last_char in 'abcdef'):
                    removed_char += 3

            if char in ['"', '\\']:
                added_char += 1

            if last_char == '\\' and not pre_active_slash:  # + vert et - rouge
                pre_active_slash = True  # - vert
                if char == '\\':
                    removed_char += 1
                elif char == '"':
                    removed_char += 1
                elif char == 'x':
                    spe = True
            else:
                pre_active_slash = False  # - rouge

            pre_char = last_char
            last_char = char

        removed_char += 2  # to deduct the starting and ending ""
        added_char += 2  # to add new starting and ending ""

        all_removed += removed_char
        all_added += added_char

        # print(f"{line}, {code}, {value}, {code_count}, {all_removed}")

    return all_removed, all_added


def main():
    print(part1())


if __name__ == "__main__":
    main()

