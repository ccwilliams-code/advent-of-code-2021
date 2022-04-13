# Author: Charlie Williams

"""Draw a line in a matrix given the start and end coords. Calc the number of intersections"""
import numpy as np
from functools import total_ordering
from pprint import pprint
import numpy

from aoc_utils import read_input


def main():
    coords = []
    matrix = numpy.empty((1000, 1000))
    # Initialize 1000x1000 matrix with 0s
    matrix.fill(0)
    data = read_input('input.txt')

    strcoords = list(map(lambda s: s.split(" -> "), data))

    for row in strcoords:
        for each in row:
            coords.append(eval(each))
        # pprint(coords)

    # for i in range(2, 4, 2):
    for i in range(0, len(coords), 2):
        # [::-1] reverses the order of the coords, because matrix operation is expecting rc, not xy
        draw_line(matrix, coords[i][::-1], coords[i + 1][::-1])
    # When you sum 2 lists, you join them together, so this sum(matrix, list) works.
    # It joins each sub list to the target list
    print(len(sum([[int(i) for i in line if int(i) > 1] for line in matrix], [])))

    print(matrix.astype(np.int))


def draw_line(matrix, start: tuple, end: tuple):
    if start[0] == end[0]:
        # Horizontal Case

        if start[1] > end[1]:
            matrix[start[0], end[1]:start[1] + 1] += 1
        else:
            matrix[start[0], start[1]:end[1] + 1] += 1

    elif start[1] == end[1]:
        # Vertical Case
        if start[0] > end[0]:
            matrix[end[0]:start[0] + 1, start[1]] += 1
        else:
            matrix[start[0]:end[0] + 1, start[1]] += 1
    else:  # Diagonal case
        print(f'{start}--{end}')
        r_range = list(range(start[0], end[0] + 1)) if start[0] < end[0] else list(
            reversed(range(end[0], start[0] + 1)))
        c_range = list(range(start[1], end[1] + 1)) if start[1] < end[1] else list(
            reversed(range(end[1], start[1] + 1)))
        print(list(zip(r_range, c_range)))
        for each in list(zip(r_range, c_range)):
            matrix[each[0]][each[1]] += 1

        # if start[0] > end[0]:
        #     if start[1] < end[1]:
        #         matrix[start[0]:end[0], start[1]:end[1]] += 1
        #     else:
        #         matrix[start[0]:end[0], end[1]:start[1]] += 1
        # else:
        #     if start[1] < end[1]:
        #
        #         matrix[end[0]:start[0], start[1]:end[1]] += 1
        #     else:
        #         print(f"{end[0]}:{start[0]}, {start[1]}:{end[1]}")
        #         print(matrix[end[0]:start[0], end[1]:start[1]])
        #         print(matrix[end[1]: start[1]], matrix[end[0]:start[0]])
        #         matrix[end[0]:start[0], end[1]:start[1]] += 1


if __name__ == "__main__":
    main()
