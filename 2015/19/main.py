import re


def get_molecule() -> str:
    with open("input.txt") as f:
        molecule = f.read()
    return molecule


def get_replacements() -> dict:
    with open("replacements.txt") as f:
        content = f.readlines()
    replacements = dict()
    for line in content:
        elements = re.findall(r"\w+", line)
        if elements[0] in replacements.keys():
            replacements[elements[0]].append(elements[1])
            new_value = replacements[elements[0]]
        else:
            new_value = [elements[1]]
        replacements[elements[0]] = new_value
    return replacements


def molecule_replacements(molecule: str, replacements: dict):
    all_single_replacements = set()
    for element, possible_replacements in replacements.items():
        for replacement in possible_replacements:
            i = 0
            found = True
            while found:
                n = molecule.find(element, i)  # find element starting from index i
                if n == -1:  # if not found
                    found = False
                else:
                    new_molecule = molecule[:n] + replacement + molecule[n + len(element):]
                    all_single_replacements.add(new_molecule)
                    i = n + len(element)  # index starts after already found elements to get the next one
    return len(all_single_replacements)


def reverse_replacement(molecule: str, replacements: dict):
    # get reversed dict :
    reverse_replacements = dict()
    for key, elements in replacements.items():
        for element in elements:
            reverse_replacements[element] = key

    steps = 0
    while molecule != 'e':
        for element in reverse_replacements.keys():
            i = 0
            found = True
            while found and i < len(molecule):
                n = molecule.find(element, i)  # find element starting from index i
                if n == -1:  # if not found
                    found = False
                else:  # if found
                    if molecule not in replacements["e"]:
                        if reverse_replacements[element] != "e":
                            new_molecule = molecule[:n] + reverse_replacements[element] + molecule[n + len(element):]
                            molecule = new_molecule
                            steps += 1
                            i = n + len(reverse_replacements[element])  # index starts after already changed elements
                        else:
                            i = n + len(element)
                    else:
                        molecule = reverse_replacements[element]
                        steps += 1
    return steps


def main():
    molecule: str = get_molecule()
    replacements: dict = get_replacements()
    print(molecule_replacements("HOH", {"H": ["HO", "OH"], "O": ["HH"]}))
    print(molecule_replacements("HOHOHO", {"H": ["HO", "OH"], "O": ["HH"]}))
    print(molecule_replacements(molecule, replacements))
    print(reverse_replacement("HOH", {"H": ["HO", "OH"], "O": ["HH"], "e": ["H", "O"]}))
    print(reverse_replacement("HOHOHO", {"H": ["HO", "OH"], "O": ["HH"], "e": ["H", "O"]}))
    print(reverse_replacement(molecule, replacements))


if __name__ == "__main__":
    main()
