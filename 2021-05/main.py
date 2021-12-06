import re
import heapq
import math
import itertools
import time
from collections import Counter, defaultdict as dd
from functools import reduce

with open('input.txt', 'r') as f:
    arr = [x.strip('\n') for x in f.readlines()]

coordinates = []
common = Counter()

for line in arr:
    x = re.split(',| -> ', line)
    x = [int(a) for a in x]
    coordinates.append(x)

for [x1, y1, x2, y2] in coordinates:
    line = max(abs(x2 - x1), abs(y2 - y1))
    dx, dy = (x2 - x1) // line, (y2 - y1) // line
    for pos in range(line + 1):
        common[x1 + dx * pos, y1 + dy * pos] += 1

common = dict((k, v) for k, v in common.items() if v >= 2)
print(len(common))

