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
    oxygen_list = matrix.copy()
    co_list = matrix.copy()

    # Oxygen//Most Common
    for each in matrix:
        oxygen_list = eliminate_incorrect(oxygen_list, c, calc_most_common_bit(count_bits(get_col(oxygen_list, c))))
        if len(oxygen_list) == 1:
            break
        c += 1

    c = 0
    for each in matrix:
        co_list = eliminate_incorrect(co_list, c, calc_least_common_bit(count_bits(get_col(co_list, c))))
        if len(co_list) == 1:
            break
        c += 1

    pprint(oxygen_list)
    pprint(co_list)

    oxygen_rating = int(get_binary_from_bitlist(oxygen_list[0]), 2)
    co2_rating = int(get_binary_from_bitlist(co_list[0]), 2)

    print(oxygen_rating * co2_rating)


def eliminate_incorrect(alist: list, position_to_check: int, correct_value: int) -> list:
    results = []
    for each in alist:
        if each[position_to_check] == correct_value:
            results.append(each)
    return results


def count_bits(list_of_bits: list) -> list[int]:
    results = [0, 0]
    for each in list_of_bits:
        results[each] += 1
    return results


def get_col(matrix: list[list], col_number) -> list:
    results = []
    for row in matrix:
        results.append(row[col_number])
    return results


def calc_most_common_bit(zero_one_freq_list) -> int:
    """Given a list containing the frequency of zeroes and ones
    return whether zeroes or ones were more common"""
    if zero_one_freq_list[0] > zero_one_freq_list[1]:
        return 0
    elif zero_one_freq_list[0] < zero_one_freq_list[1]:
        return 1
    else:
        print("EQUAL ALERT")
        return 1


def calc_least_common_bit(zero_one_freq_list):
    """Given a list containing the frequency of zeroes and ones
    return whether zeroes or ones were less common"""
    if zero_one_freq_list[0] > zero_one_freq_list[1]:
        return 1
    elif zero_one_freq_list[0] < zero_one_freq_list[1]:
        return 0
    else:
        print("EQUAL ALERT")
        return 0


def get_binary_from_bitlist(bitlist):
    return "".join([str(x) for x in bitlist])


if __name__ == "__main__":
    main()

# 3950397 is too high
