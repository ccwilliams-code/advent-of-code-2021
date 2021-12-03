# Author: Charlie Williams
"""Day 3 of Advent of Code: Dive!"""
from collections import namedtuple
from pprint import pprint


def main():
    input_str = ''

    with open("input.txt") as f:
        input_str = f.read().strip()
    input_tokens = input_str.split("\n")
    # print(input_str)

    total_rows = len(input_tokens);
    column_counts = [0] * len(input_tokens[0])
    for each in input_tokens:
        x = 0
        while x < len(each):
            column_counts[x] += int(each[x])
            x += 1

    pprint(f'total rows: {total_rows}')
    # pprint(column_counts)
    binary_list_result = []
    for each in column_counts:
        if each > total_rows / 2:
            binary_list_result.append(1)
        else:
            binary_list_result.append(0)

    gamma_rate = "".join([str(i) for i in binary_list_result])
    epsilon_rate = "".join([str(1 - i) for i in binary_list_result])
    oxygen = input_tokens.copy()
    co2 = input_tokens.copy()
    x = 0
    while x < len(input_tokens[0]):

        oxydone = False
        co2done = False

        for each in input_tokens:

            if each[x] != gamma_rate[x] and len(oxygen) > 1 and not oxydone:
                # print(f'{each[x] != gamma_rate[x]}')
                print(f'oxyeax={each[x]}{each[x] != gamma_rate[x]}')
                oxygen.remove(each)
                oxydone = True
            if each[x] != epsilon_rate[x] and len(co2) > 1 and not co2done:
                print(f'co2eax={each[x]}{each[x] == epsilon_rate[x]}')
                co2.remove(each)
                co2done = True

            if co2done and oxydone:
                print("\n")
                break

            x += 1

    dgamma_rate = binaryToDecimal("".join([str(i) for i in gamma_rate]))
    depsilon_rate = binaryToDecimal("".join([str(i) for i in epsilon_rate]))

    pprint(len(oxygen))
    pprint(len(co2))


def binaryToDecimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal


if __name__ == "__main__":
    main()
