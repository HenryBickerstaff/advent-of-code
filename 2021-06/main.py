import re
import heapq
import math
import itertools
import time
from collections import Counter, defaultdict as dd
from functools import reduce

with open('input.txt', 'r') as f:
    arr = [[int(a) for a in x.strip('\n').split(',')] for x in f.readlines()][0]

original_length = len(arr)
part2_arr = arr

def part1(school1, days) -> list:
    """
    Calculates the total number of fish after a certain amount of days.
        Keeps every fish seperate and cycles through their days adding
        a new fish to the list as they are created.

    Args:
        school1(list) - List of fish
        days(int) - Number of days to cycle through
    Returns:
        school1(list) - New list of fish containing all the new fish as
            well.
    """
    for day in range(days):
        for index, fish in enumerate(school1):
            school1[index] -= 1
            if fish == 0:
                school1[index] = 6
                school1.append(9)
    return school1

def part2(school2, days) -> list:
    """
    Calculates the number of fish at each day of a fish's cycle.
        The total number of fish at each day of the cycle then cycles
        through, having the fish at day 0 not only return to day 6,
        but create a new fish at day 8.

    Args:
        school2(list) - List of "fish" containing an int of a day in a 
            fish cycle.
        days(int) - The number of days to cycle through.
    Returns:
        fish_cycles(list) - List of days of a cycle with the number of 
            fish currently on that day.
    """
    fish_cycles = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in school2:
        fish_cycles[fish] += 1

    for day in range(days):
        breeders = fish_cycles[0]
        fish_cycles.append(fish_cycles.pop(0))
        fish_cycles[6] += breeders

    return fish_cycles

# PART 1
fishies = part1(arr, 80)
print(len(fishies))

# PART 2
new_fishies = part2(part2_arr, 256)
print(sum(new_fishies))


