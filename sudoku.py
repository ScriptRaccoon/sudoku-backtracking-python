"""Solving algorithm for Sudokus via backtracking and generators"""

from collections.abc import Iterator
from time import perf_counter
from samples import medium_sudoku as sudoku


def print_sudoku(board: list[list[int]]) -> None:
    """Prints a sudoku to the console"""
    for row in board:
        for num in row:
            print(num if num > 0 else "*", end="")
            print(" ", end="")
        print()
    print()


def get_coord(board: list[list[int]]) -> None | tuple[int, int]:
    """Gets the coordinate of an empty cell if there is one"""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None


def is_valid(row: int, col: int, num: int, board: list[list[int]]) -> bool:
    """Checks if a potential number is valid at a given position in the board"""
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(0, 9)]:
        return False
    row_start = 3 * (row // 3)
    col_start = 3 * (col // 3)
    return num not in [
        board[row_start + i][col_start + j] for i in range(0, 3) for j in range(0, 3)
    ]


def get_solutions(board: list[list[int]]) -> Iterator[list[list[int]]]:
    """Generator recursively yielding completions of a Sudoku board"""
    coord = get_coord(board)
    if coord is None:
        yield board
        return
    row, col = coord
    for num in range(1, 10):
        if is_valid(row, col, num, board):
            board[row][col] = num
            yield from get_solutions(board)
            board[row][col] = 0


def main() -> None:
    """Prints the solutions to a sample sudoku"""

    print("\nSudoku:\n")
    print_sudoku(sudoku)

    print("Solutions:\n")

    number_solutions = 0
    solutions = get_solutions(sudoku)

    start_time = perf_counter()

    for solution in solutions:
        number_solutions += 1
        print_sudoku(solution)

    end_time = perf_counter()

    message = f"Found {number_solutions} solution"
    if number_solutions > 1:
        message += "s"
    print(message)

    rounded_time = format(end_time - start_time, ".3f")
    print(f"Ellapsed time: {rounded_time}")


if __name__ == "__main__":
    main()
