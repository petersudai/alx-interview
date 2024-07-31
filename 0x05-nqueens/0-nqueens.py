#!/usr/bin/env python3
"""
N Queens Problem Solver
"""

import sys


def is_valid(board, row, col):
    """ Check if a position is safe for placing a queen """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """ Solve the N Queens problem using backtracking """
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)


def print_solutions(solutions, n):
    """ Print the solutions in required format """
    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])


def main():
    """ Main function to handle input and solve problem """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be atleast 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve_nqueens(n, 0, board, solutions)
    print_solutions(solutions, n)


if __name__ == "__main__":
    main()
