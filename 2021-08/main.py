import re
import heapq
import math
import itertools
import time
from collections import Counter, defaultdict as dd
from functools import reduce

with open('input.txt', 'r') as f:
    arr = [x.strip('\n') for x in f.readlines()]

#print(arr)
#print(arr[0].split('|'))

def part1() -> int:
    totals = {
        "1": 0,
        "4": 0,
        "7": 0,
        "8": 0,
    }
    new_outputs = []
    outputs = [x.split('|') for x in arr]
    for i in outputs:
        new_outputs.append([x.split() for x in i][1])
    print(new_outputs)

    for j in new_outputs:
        for segment in j:
            if len(segment) == 2:
                totals["1"] += 1
            elif len(segment) == 3:
                totals["7"] += 1
            elif len(segment) == 4:
                totals["4"] += 1
            elif len(segment) == 7:
                totals["8"] += 1
    
    return sum(totals.values())

#part1()

def part2():
    new_segments = []
    segments = [x.split('|') for x in arr]
    for segment in segments:
        new_segments.append([x.split() for x in segment])

    for i in new_segments:
        lookup = {
            "top": [],
            "top_left": [],
            "top_right": [],
            "mid": [],
            "bot_left": [],
            "bot_right": [],
            "bot": [],
        }
        a = sorted(i[0], key=len)
        lookup["top_right"] = [x for x in a[0]]
        lookup["bot_right"] = [x for x in a[0]]
        lookup["top"] = [x for x in a[1] if x not in lookup["top_right"]]
        lookup["mid"] = [x for x in a[3] if x not in lookup["top_right"]]
        lookup["top_left"] = lookup["mid"]

part2()

