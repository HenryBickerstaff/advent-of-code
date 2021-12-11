import re
import heapq
import math
import itertools
import time
import numpy as np
from scipy import ndimage
from collections import Counter, defaultdict as dd
from functools import reduce

with open('input.txt', 'r') as f:
    arr = [x.strip('\n') for x in f.readlines()]

input_list = []
for line in arr:
    chars = []
    chars[:] = line
    input_list.append(chars)

input_array = np.array(input_list)

def part1() -> list:
    """
    Loops through each row and takes the position of each element that is lower than both it's neighbors. This list of 
        potentials can then be looped through to check the elements "above" or "below" it.

    Returns:
        risk(list) - List of at risk positions with added 1.
        
    """
    risk = []
    potential = {}

    for i, row in enumerate(input_array):
        for j, pos in enumerate(row):
            if j > 0 and j < len(row) - 1 and pos < row[j - 1] and pos < row[j + 1]:
                if i in potential.keys():
                    potential[i].append(j)
                else:
                    potential[i] = [j]
            elif j == 0 and pos < row[j + 1] or j == len(row) - 1 and pos < row[j - 1]:
                if i in potential.keys():
                    potential[i].append(j)
                else:
                    potential[i] = [j]

    for k, v in potential.items():
        for index in v:
            current = input_array[k][index]
            if k > 0 and k < 99:
                above = input_array[int(k) - 1][index]
                below = input_array[int(k) + 1][index]

                if current < above and current < below:
                    risk.append(int(current) + 1)
                    print(current, above, below)

            elif k == 0:
                below = input_array[int(k) + 1][index]
                if current < below:
                    risk.append(int(current) + 1)
            elif k == 99:
                above = input_array[int(k) - 1][index]
                if current < above:
                    risk.append(int(current) + 1)

    return risk

def part2() -> int: 
    """
    Takes a numpy array, converts all values to either 1s or 0s (as we don't care about actual values, only 9s or non-9s), then
        labels the array using scipy ndimage, giving us the features of the array, in this case the clumps of 0s. This
        array can then be flattened and the number of each value occurence totaled. We then take the 3 largest and multiply
        them.

    Returns:
        total(int) - Total of the 3 largest basins multiplied together.
    """
    for i, row in enumerate(input_array):
        for j, pos in enumerate(row):
            if pos == '9':
                input_array[i][j] = 1
            else:
                input_array[i][j] = 0

    label, total_basins = ndimage.label(input_array == '0')
    size = np.bincount(label.ravel())
    sorted_sizes = sorted(size[1:], reverse=True)
    total = sorted_sizes[0] * sorted_sizes[1] * sorted_sizes[2]
    return total

print(sum(part1()))
print(part2())

