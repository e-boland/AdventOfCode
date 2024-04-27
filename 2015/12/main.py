import json


def part2():
    def flatten(element):

        # if the (outermost) element is a dict :
        if isinstance(element, dict):  # isinstance(object, type) : check if the object's type is type
            if "red" not in element.keys() and "red" not in element.values():  # PART 2 ADDITION
                for key, value in element.items():
                    yield key  # recover key in flattened_values
                    yield from flatten(value)  # calls the function flatten with this dictionary's value as argument

        # if the (outermost) element is a list, a set or a tuple:
        elif isinstance(element, (list, set, tuple)):
            for el in element:
                yield from flatten(el)  # calls the function flatten with the list's item as argument

        # if the argument given to the flatten function isn't a list or a dict anymore :
        else:
            yield element  # recover element in flattened_values

    with open("input.json", "r") as f:
        nested_elements = json.load(f)
    print(nested_elements)

    # Calling the generator function flatten() with the nested_elements as argument:
    flattened_values = list(flatten(nested_elements))  # all yielded elements from flatten() in a list
    print(flattened_values)

    num_sum = 0

    for item in flattened_values:
        if isinstance(item, int):
            num_sum += item

    return num_sum


def main():
    print(part2())


if __name__ == "__main__":
    main()
