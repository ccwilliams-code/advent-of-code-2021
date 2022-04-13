# Author: Charlie Williams

"""Simulate a LOT of Lanternfish"""
from pprint import pprint

from aoc_utils import read_input


def main():
    data = read_input('input.txt')
    days_to_simulate = 256
    data = data[0].split(',')
    sea: dict = dict.fromkeys(range(9), 0)
    for each in data:
        sea[int(each)] += 1

    for day in range(18):
        for key in sea:
            sea[key]

    pprint(sea)


if __name__ == "__main__":
    main()
