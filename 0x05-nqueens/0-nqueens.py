#!/usr/bin/env python3
"""
Solves the N-Queens problem.
"""

import sys

def print_usage():
    print("Usage: nqueens N")
    sys.exit(1)

def print_error(message):
    print(message)
    sys.exit(1)

def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on board[row][col].
    """
    # Check the row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, n, solutions):
    """
    Solve the N-Queens problem using backtracking.
    """
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens(board, col + 1, n, solutions)
            board[i][col] = 0  # backtrack

def nqueens(n):
    """
    Solve the N-Queens problem for a given size n.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_error("N must be a number")

    if n < 4:
        print_error("N must be at least 4")

    solutions = nqueens(n)
    for solution in solutions:
        print(solution)
