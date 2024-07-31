#!/usr/bin/python3
"""
Solving the N Queens problem using backtracking
"""

import sys

# Validate input arguments
if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    sys.exit(1)

if n < 4:
    print('N must be at least 4')
    sys.exit(1)


def is_safe(board, row, col):
    """Check if it's safe to place a queen at the given position"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens_rec(board, row, n, solutions):
    """Recursively solve the N Queens problem"""
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens_rec(board, row + 1, n, solutions)
            board[row] = -1


def solve_nqueens(n):
    """Find all solutions for the N Queens problem"""
    board = [-1] * n
    solutions = []
    solve_nqueens_rec(board, 0, n, solutions)
    return solutions


def format_solution(solution):
    """Format the solution in the required output format"""
    formatted = []
    for i, col in enumerate(solution):
        formatted.append([i, col])
    return formatted


# Solve the N Queens problem and print solutions
solutions = solve_nqueens(n)

for solution in solutions:
    print(format_solution(solution))
