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


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    chess_board = []
    [chess_board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in chess_board]
    return (chess_board)


def board_deepcopy(chess_board):
    """Return a deepcopy of a chessboard."""
    if isinstance(chess_board, list):
        return list(map(board_deepcopy, chess_board))
    return (chess_board)


def get_solution(chess_board):
    """Return the list of lists representation of a solved chessboard."""
    board_solution = []
    for r in range(len(chess_board)):
        for c in range(len(chess_board)):
            if chess_board[r][c] == "Q":
                board_solution.append([r, c])
                break
    return (board_solution)


def xout(chess_board, row, col):
    """X out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for c in range(col + 1, len(chess_board)):
        chess_board[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        chess_board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(chess_board)):
        chess_board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        chess_board[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(chess_board)):
        if c >= len(chess_board):
            break
        chess_board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chess_board[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chess_board):
            break
        chess_board[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(chess_board)):
        if c < 0:
            break
        chess_board[r][c] = "x"
        c -= 1


def recursive_solve(chess_board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(chess_board):
        solutions.append(get_solution(chess_board))
        return (solutions)

    for c in range(len(chess_board)):
        if chess_board[row][c] == " ":
            tmp_board = board_deepcopy(chess_board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chess_board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(chess_board, 0, 0, [])
    for sol in solutions:
        print(sol)
    print("Found %d solutions" % len(solutions))

    sys.exit(0)
