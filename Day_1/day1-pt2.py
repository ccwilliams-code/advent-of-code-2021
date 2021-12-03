# Author: Charlie Williams
"""Day 1 Part 2 of Advent of Code: Sonar Sweep"""
from pprint import pprint
from typing import List


def main():
    sums, data = [], []
    # Read the data
    with open("input.txt") as f:
        for each in f.readlines():
            data.append(int(each.strip()))

    x = 0
    while x < len(data) - 2:
        sums.append(data[x] + data[x + 1] + data[x + 2])
        x += 1

    print(count_increases(sums))


def count_increases(numbers: List) -> int:
    """count the number of times an increase occurs between elements in an array"""
    x = 1
    increases = 0
    while x < len(numbers):
        print(f"{numbers[x]} >? {numbers[x - 1]}")
        if numbers[x] > numbers[x - 1]:
            increases += 1
        x += 1
    return increases


if __name__ == "__main__":
    main()
