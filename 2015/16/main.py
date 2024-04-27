import re


def parse_sues(all_sues: [str]):
    sue_dict = dict()

    for sue in all_sues:
        match = re.match(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)", sue)
        if match:
            sue_number = int(match.group(1))
            this_sue = [match.group(i) for i in range(2, 7, 2)]  # from 2 to 7, 1 out of 2
            values = [int(match.group(i)) for i in range(3, 8, 2)]  # from 3 to 8, 1 out of 2
            sue_dict[sue_number] = dict(zip(this_sue, values))
    return sue_dict


def part1():
    right_sue = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0,
                 "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

    with open("input.txt") as f:
        all_sues = f.readlines()

    sue_dict = parse_sues(all_sues)
    sue_match = list(range(1, len(all_sues) + 1))

    while len(sue_match) > 1:
        sue_number = sue_match.pop(0)
        this_sue = sue_dict[sue_number]
        match = True
        attributes = list(right_sue.keys())
        i = 0
        while match and i < len(attributes):
            attribute = attributes[i]
            value = right_sue.get(attribute)
            current = this_sue.get(attribute)
            i += 1
            if current is None:
                continue
            if attribute in ["cats", "trees"]:
                if current <= value:
                    match = False
            elif attribute in ["pomeranians", "goldfish"]:
                if current >= value:
                    match = False
            elif current != value:
                match = False
        if match:
            sue_match.append(sue_number)
    return sue_match


def main():
    print(part1())


if __name__ == "__main__":
    main()
