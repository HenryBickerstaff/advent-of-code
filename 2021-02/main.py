import re
import heapq
import math
import itertools
import time
from collections import Counter, defaultdict as dd
from functools import reduce

with open('input.txt', 'r') as f:
    arr = [(x.strip('\n')) for x in f.readlines()]

amount_multipliers = {
    "up": -1,
    "down": 1, 
}

# ==============================================================================
# PART 1
# ==============================================================================

position = [0, 0]

for command in arr:
    direction, amount = command.split()
    amount = int(amount) 

    if direction == 'forward':
        position[0] += amount
    else:
        position[1] += amount * amount_multipliers[direction]

print(position)
print(position[0] * position[1])

# ==============================================================================
# PART 2
# ==============================================================================

position = [0, 0]
aim = 0

for command in arr:
    direction, amount = command.split()
    amount = int(amount) 

    if direction == 'forward':
        position[0] += amount
        position[1] += amount * aim
    else:
        aim += amount * amount_multipliers[direction]

print(position)
print(position[0] * position[1])

