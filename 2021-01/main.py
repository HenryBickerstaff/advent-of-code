import re
import heapq
import math
import itertools
import time
from collections import Counter, defaultdict as dd
from functools import reduce

with open('input.txt', 'r') as f:
    arr = [int(x.strip('\n')) for x in f.readlines()]


# We have to +1 due to...
part1 = sum(y > x for x, y in zip(arr, arr[1:]))
print(part1 + 1)


# We know that since for each sliding window 2 elements are common,
# therefore we only actually need to compare the *different* elements.
# This would be the original element compared to the element 3 elements
# removed. 
part2 = sum(y > x for x, y in zip(arr, arr[3:]))
print(part2)



