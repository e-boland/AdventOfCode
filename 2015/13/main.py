"""
For each possible pair, I have to calculate the resultant of both happiness.
For example, if Alice loses 2 happiness sitting next to Bob and Bob gains 93 happiness sitting next to Alice :
The pair Alice-David = 91.

'name' '_' 'gain/lose' 'number' '_' '_' '_' '_' '_' '_' 'name''.'
Alice would lose 2 happiness units by sitting next to Bob.
merged => sort => turn into a string

Ex: (A,  B,  C,  D)  = order : len = 4, A = order[i], B = order[i+1] ... with i in range(len(order))
=> (AB, BC, CD, DA)  = pairs of this order :
i = 0 => AB = order[i] + order[i+1] if i+1 <len(order) else order[i] + order[0]  => i+=1
=> (AB, BC, CD, AD)  = keys for these pairs : tuple(sorted([order[i]] + [order[i+1]]))
"""

from itertools import permutations


def part1():
    with open('input.txt') as f:
        content = f.readlines()  # list with each line as an element

    dic = dict()  # keys = pairs of people, values = total of happiness for both sitting together
    all_names = set()
    # To add myself (part2) :
    my_name = "Me"
    all_names.add(my_name)

    for line in content:
        name_1, _, sign, num, _, _, _, _, _, _, name_2 = ((line.replace('.', '')).strip()).split(' ')
        all_names.add(name_1)
        all_names.add(name_2)
        new_key = tuple(sorted([name_1] + [name_2]))  # key = tuple (name1, name2 in alphabetical order)
        num_value = int(num) if sign == "gain" else -int(num)  # positive num if "gain", negative num if "lose"
        if new_key in dic.keys():
            dic[new_key] = int(dic.get(new_key)) + num_value  # new key's value = old value + current value
        else:
            dic[new_key] = num_value  # key's value = current value if not yet in dict

        # Adding myself (part2):
        my_key_1 = tuple(sorted([my_name] + [name_1]))
        if my_key_1 not in dic.keys():
            dic[my_key_1] = 0
        my_key_2 = tuple(sorted([my_name] + [name_2]))
        if my_key_2 not in dic.keys():
            dic[my_key_2] = 0

    names = list(all_names)
    all_orders = list(permutations(names))  # every list's item is a different order
    best_order = 0

    for order in all_orders:  # Ex : order = (A, C, B, D)
        order_value = 0  # will be the total value for the current order

        for index in range(len(order) - 1):  # len(A, C, B, D) = 4 => i : 0-4 with 4 out of index
            next_index = index + 1 if index != len(order) - 1 else 0
            pair = tuple(sorted([order[index]] + [order[next_index]]))  # = (A, C), (B, C) or (B,D) which are dic keys
            order_value += dic.get(pair)  # adding the current pair's value to the order's value

        if order_value > best_order:
            best_order = order_value

    return best_order


def main():
    print(part1())


if __name__ == "__main__":
    main()
