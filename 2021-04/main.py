import re
import heapq
import math
import itertools
import time
from collections import Counter, defaultdict as dd
from functools import reduce

with open('input.txt', 'r') as f:
    arr = [x.strip('\n') for x in f.readlines()]

# ===================================================================================
# PART 1
# ===================================================================================

def generate_boards(arr) -> list:
    """
    Generates 2 lists of "boards", the first having the horizontal rows, and the second
        having the vertical columns. This effectively gives us 2 lists of lists that 
        correspond to a singular "board".

    Args:
        arr(list) - List of input data from input.txt
    Returns:
        boards(list) - list of boards aligned so each element is a horizontal row.
        flipped_boards(list) - list of boards aligned so each element is a vertical column.
    """
    boards = []
    individual_board = []
    flipped_boards = []

    for row in arr[2:]:
        if row != "":
            x = row.split()
            x = map(int, x)
            individual_board.append(list(x))
        else:
            boards.append(individual_board)
            individual_board = []

    for board in boards:
        new_board = []
        for pos in range(5):
            new_row = []
            for row in board:
                new_row.append(row[pos])
            new_board.append(new_row)

        flipped_boards.append(new_board)

    return boards, flipped_boards

def draw_numbers(board_collection) -> int:
    """
    Draws numbers from the input data and "marks" boards as the numbers are revealed. Marking
        consists of adding 1000 to the base number.
    
    Args:
        board_collection(list) - List containing a list of boards, and a list of flipped_boards.
    Returns:
        board(list) - The winning board.
        drawn_number(int) - The last number that was drawn giving the win.
    """
    numbers = list(map(int, arr[0].split(',')))

    for drawn_number in numbers:
        for board_type in board_collection:
            for index, board in enumerate(board_type):
                for row in board:
                    for index, item in enumerate(row):
                        if drawn_number == item:
                            row[index] += 1000
                    if sum(row) > 5000:
                        return board, drawn_number

def calculate_total(board, last_number) -> int:
    """
    Calculates the total of all unmarked board numbers, and multiplies it by the last drawn number.

    Args:
        board(list) - The winning/losing board.
        last_number(int) - The last drawn number.
    Returns:
        last_number * total(int) - The total of all unmarked numbers and the last drawn number.
    """
    total = 0
    for row in board:
        if sum(row) > 5000:
            board.remove(row)
            continue
        row = [x for x in row if x < 1000]
        total += sum(row)

    return last_number * total


boards, flipped_boards = generate_boards(arr)
winning_board, last_number = draw_numbers([boards, flipped_boards])
print(calculate_total(winning_board, last_number))

# ===================================================================================
# PART 2
# ===================================================================================

def draw_numbers_(board_collection) -> int:
    """
    Calculates the "losing" board. Removes boards that have a bingo until only 1 board is left.
        Waits for the last board to also "complete" and then returns that board and the last
        drawn number.

    Args:
        board_collection(list) - List of boards(list) and flipped_boards(list).
    Returns:
        board_collection[0][0](list) - The "losing" or last remaining board.
        drawn_number(int) - The last drawn number resulting in the bingo.
    """
    numbers = list(map(int, arr[0].split(',')))
    for drawn_number in numbers:
        for board_type in board_collection:
            for board_index, board in enumerate(board_type):
                for row in board:
                    for index, item in enumerate(row):
                        if drawn_number == item:
                            row[index] += 1000
                    if sum(row) > 5000:
                        if len(board_type) > 1:
                            board_collection[0].pop(board_index)
                            board_collection[1].pop(board_index)
                            break
                        else:
                            return board_collection[0][0], drawn_number

boards, flipped_boards = generate_boards(arr)
losing_board, last_number = draw_numbers_([boards, flipped_boards])
print(calculate_total(losing_board, last_number))

