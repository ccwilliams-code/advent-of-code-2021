# Author: Charlie Williams
"""Day 2 of Advent of Code: Dive!"""
from collections import namedtuple
from pprint import pprint

Instruction = namedtuple('Instruction', 'command value')


def main():
    instructions: list[Instruction] = []
    pos = (0, 0, 0)

    with open("input.txt") as f:
        for each in f.readlines():
            pos = handleInstruction(Instruction(each.split(" ")[0], int(each.split(" ")[1].strip())), pos)

    print(pos[0] * pos[1])


def handleInstruction(inst: Instruction, pos: tuple):
    x, y, a = pos
    match inst.command:
        case "forward":
            x += inst.value
            y += inst.value * a
        case "down":
            a += inst.value
        case "up":
            a -= inst.value
    return x, y, a


if __name__ == "__main__":
    main()
