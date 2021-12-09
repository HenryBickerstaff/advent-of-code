import re
import heapq
import math
import itertools
import time
from collections import Counter, defaultdict as dd
from functools import reduce

with open('input.txt', 'r') as f:
    arr = [[int(a) for a in x.strip('\n').split(',')] for x in f.readlines()][0]

print(arr)

def part1() -> int:
    fuel = 0
    median = len(sorted(arr)) + 1
    median = sorted(arr)[int(abs(median / 2))]
    for crab in arr:
        fuel += abs(median - crab)
    
    return fuel

print(part1())

def part2() -> int:
    totals = []
    for i in range(sorted(arr)[-1] + 1):
        total = 0
        for crab in arr:
            dif = abs(i - crab)
            for j in range(dif + 1):
                k = j + 1
                o = j * k
                o = o / 2
                total += j
        totals.append(total)

    return sorted(totals)[0]

print(part2())



