#!/usr/bin/python3
# 101-nqueens.py
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""

import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at a given position."""
    for i in range(row):
        if board[i] == col or board[i] - col == i - row or board[i] - col == row - i:
            return False
    return True


def solve_n_queens(n, row=0, board=[]):
    """Recursively solve the N-queens puzzle."""
    if row == n:
        solutions.append(list(board))
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            solve_n_queens(n, row + 1, board)
            board.pop()


def print_solutions():
    """Print all the solutions."""
    for solution in solutions:
        print(solution)


def main():
    """Main function."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queens(n)
    print_solutions()


if __name__ == "__main__":
    solutions = []
    main()
