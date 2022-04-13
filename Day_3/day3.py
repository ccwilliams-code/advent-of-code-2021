from pprint import pprint

from aoc_utils import read_input


def main():
    data = read_input('input.txt')
    matrix = [[int(y) for y in x] for x in data]
    gamma_rate_list = []
    epsilon_rate_list = []

    print("=========MATRIX DATA=========")
    pprint(matrix)
    print("=========MATRIX DATA=========")

    c = 0
    while c < len(matrix[0]):
        gamma_rate_list.append(calc_most_common_bit(count_bits(get_col(matrix, c))))
        epsilon_rate_list.append(calc_least_common_bit(count_bits(get_col(matrix, c))))
        c += 1

    gamma_rate_binary = get_binary_from_bitlist(gamma_rate_list)
    epsilon_rate_binary = get_binary_from_bitlist(epsilon_rate_list)
    print(f'Gamma   :\t{gamma_rate_binary}')
    print(f'Epsilon :\t{epsilon_rate_binary}')

    print(int(gamma_rate_binary, 2) * int(epsilon_rate_binary, 2))


def count_bits(list_of_bits: list) -> list[int]:
    results = [0, 0]
    for each in list_of_bits:
        results[each] += 1
    print(results)
    return results


def get_col(matrix: list[list], col_number) -> list:
    results = []
    for row in matrix:
        results.append(row[col_number])
    return results


def calc_most_common_bit(zero_one_freq_list):
    """Given a list containing the frequency of zeroes and ones
    return whether zeroes or ones were more common"""
    if zero_one_freq_list[0] > zero_one_freq_list[1]:
        return 0
    else:
        return 1


def calc_least_common_bit(zero_one_freq_list):
    """Given a list containing the frequency of zeroes and ones
    return whether zeroes or ones were less common"""
    if zero_one_freq_list[0] > zero_one_freq_list[1]:
        return 1
    else:
        return 0


def get_binary_from_bitlist(bitlist):
    return "".join([str(x) for x in bitlist])


if __name__ == "__main__":
    main()
