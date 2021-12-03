import re
import heapq
import math
import itertools
import time
from collections import Counter, defaultdict as dd
from functools import reduce

with open('input.txt', 'r') as f:
    arr = [x.strip('\n') for x in f.readlines()]

# =============================================================================
# PART 1
# =============================================================================

gamma_rate = []
epsilon_rate = []

for place in range(12):
    counts = {
        "1": 0,
        "0": 0,
    }

    for bits in arr:
        counts[bits[place]] += 1
   
    gamma_rate.append(max(counts, key=counts.get))
    epsilon_rate.append(min(counts, key=counts.get))

gamma = int("".join(gamma_rate), 2)
epsilon = int("".join(epsilon_rate), 2)

print(gamma * epsilon)

# =============================================================================
# PART 2
# =============================================================================

def calculate_oxygen(arr) -> str:
    """
    Calculates the oxygen rate of the submarine, filters down the base list of
        inputs and returns the final remaining input.

    Args:
        arr(list) - list of input from input.txt, base data.
    Returns:
        input[0](string) - Individual data entry that has been filtered to.
    """
    input = arr
    while len(input) > 1:
        for pos in range(12):
            counts = {
                "1": 0,
                "0": 0,
            }

            for bits in input:
                counts[bits[pos]] += 1

            most_common = max(counts, key=counts.get)

            input = list(filter(lambda a: a[pos] != most_common, input))

            if len(input) == 1:
                return input[0]

def calculate_co(arr) -> str:
    """
    Calculates the co2 rate of the submarine, filters down the base list of
        inputs and returns the final remaining input.

    Args:
        arr(list) - list of input from input.txt, base data.
    Returns:
        input[0](string) - Individual data entry that has been filtered to.
    """

    input = arr
    while len(input) > 1:
        for pos in range(12):
            counts = {
                "0": 0,
                "1": 0,
            }

            for bits in input:
                counts[bits[pos]] += 1

            least_common = min(counts, key=counts.get)

            input = list(filter(lambda a: a[pos] != least_common, input))

            if len(input) == 1:
                return input[0] 

oxygen = int(calculate_oxygen(arr), 2)
co = int(calculate_co(arr), 2)
print(oxygen)
print(co)
print(oxygen * co)
