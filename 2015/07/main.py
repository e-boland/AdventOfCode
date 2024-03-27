"""
Each number from 0 to 65535 correspond to a combination of 16-bits (either 0 or 1)
For example : 0 would be 0000 0000 0000 0000, 1 would be 0000 0000 0000 0001,
              2 would be 0000 0000 0000 0010, 3 would be 0000 0000 0000 0011,
              4 would be 0000 0000 0000 0100, 5 would be 0000 0000 0000 0101, etc.
Each wire has an identifier (some lowercase letters) and can carry a signal that is one of those 65535 numbers.

A signal is provided to each wire by a gate, another wire, or some specific value.
Each wire can only get a signal from one source, but can provide its signal to multiple destinations.
A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together:
x AND y -> z means to connect (wire x) and (wire y) to an [AND gate], and then connect its output to (wire z).

For example:
   - 123 -> x means that the signal 123 is provided to wire x.
   - x AND y -> z means that the {bitwise AND} of wire x and wire y is provided to wire z.
   - p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
   - NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

{bitwise AND} : takes two equal-length binary representations and performs the logical AND operation on
each pair of the corresponding bits. For example 1010 AND 1011 => 1010.

{bitwise OR} : 1010 OR 1011 => 1011

{left-shift by 1} : 0010 (2) => 0100 (4)
Left-shift by n is tha same as multiplying (or divide if it's a right-shift) by 2^n the corresponding number.

{bitwise complement} : NOT 1011  => 0100

To convert a number in 16-bits : f'{number:16b}' (for example : f'{4:16b}' => 0000 0000 0000 0100
"""


from numpy import uint16
from tqdm import tqdm


def part1(n=0):

    with open("input.txt") as f:
        instructions = f.readlines()

    wire_signal = dict()    # keys = wire's name ; values = signal in 16-bits
    with tqdm() as pbar:
        while "a" not in wire_signal.keys():

            for line in instructions:
                elements = line.split()  # list of the elements in line

                # 'xxx' '->' 'b'
                if len(elements) == 3 and elements[2] not in wire_signal.keys():   # if 'b' not in dict keys
                    if elements[0].isdigit():
                        if n and elements[2] == 'b':
                            wire_signal[elements[2]] = uint16(n)
                        else:
                            wire_signal[elements[2]] = uint16(elements[0])  # {"b": 'xxx in 16-bits'}
                    elif elements[0] in wire_signal.keys():
                        wire_signal[elements[2]] = wire_signal.get(elements[0])

                # 'NOT' 'b' '->' 'c'
                if len(elements) == 4 and elements[1] in wire_signal.keys():  # if 'b' in dict keys
                    new_signal = ~wire_signal.get(elements[1])  # NOT xxx in 16-bits
                    wire_signal[elements[3]] = new_signal  # {"c" : 'not xxx in 16-bits'}

                # 'a' 'INSTRUCTION' 'b' '->' 'c'
                if len(elements) == 5:
                    if elements[0].isdigit():
                        a = int(elements[0])
                    else:
                        a = wire_signal.get(elements[0])
                        if a is None:
                            continue  # Ends the current iteration of the closest loop
                    if elements[2].isdigit():
                        b = int(elements[2])
                    else:
                        b = wire_signal.get(elements[2])
                        if b is None:
                            continue

                    if elements[1] == "LSHIFT":
                        output = a << b
                        wire_signal[elements[4]] = output  # {'c' = output in 16-bits}
                    elif elements[1] == "RSHIFT":
                        output = a >> b
                        wire_signal[elements[4]] = output
                    elif elements[1] == "AND":
                        output = a & b
                        wire_signal[elements[4]] = output
                    elif elements[1] == "OR":
                        output = a | b
                        wire_signal[elements[4]] = output

                pbar.update()

    return int(wire_signal['a'])


def main():
    print(part1(part1()))


if __name__ == '__main__':
    main()
