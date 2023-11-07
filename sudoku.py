from collections.abc import Iterator
from copy import deepcopy
from time import perf_counter
from samples import sudoku1

BLOCK_SIZE = 3
BLOCK_NUMBER = 3
SIZE = BLOCK_SIZE * BLOCK_NUMBER


def print_sudoku(board: list[list[int]]) -> None:
    for row in board:
        for num in row:
            print(num if num > 0 else "*", end="")
            print(" ", end="")
        print()
    print()


def get_empty_coord(board: list[list[int]]) -> None | tuple[int, int]:
    for y in range(SIZE):
        for x in range(SIZE):
            if board[y][x] == 0:
                return (x, y)
    return None


def is_valid(x: int, y: int, val: int, board: list[list[int]]) -> bool:
    row = board[y]
    col = [board[i][x] for i in range(SIZE)]
    x0 = BLOCK_SIZE * (x // BLOCK_NUMBER)
    y0 = BLOCK_SIZE * (y // BLOCK_NUMBER)
    block = [
        board[y0 + i][x0 + j] for i in range(BLOCK_SIZE) for j in range(BLOCK_SIZE)
    ]
    return not (val in row or val in col or val in block)


def solution_generator(board: list[list[int]]) -> Iterator[list[list[int]]]:
    coord = get_empty_coord(board)
    if coord is None:
        yield board
    else:
        x, y = coord
        for val in range(1, SIZE + 1):
            ok = is_valid(x, y, val, board)
            if ok:
                _board = deepcopy(board)
                _board[y][x] = val
                yield from solution_generator(_board)


def main():
    sudoku_to_solve = sudoku1
    print("\nSudoku:\n")
    print_sudoku(sudoku_to_solve)
    print("Solutions:\n")
    number_solutions = 0
    solutions = solution_generator(sudoku_to_solve)
    start_time = perf_counter()
    for solution in solutions:
        number_solutions += 1
        print_sudoku(solution)
    end_time = perf_counter()
    rounded_time = format(end_time - start_time, ".3f")
    if number_solutions > 1:
        print(f"There are {number_solutions} solutions.")
    else:
        print(f"There is {number_solutions} solution.")
    print(f"Ellapsed time: {rounded_time}")


if __name__ == "__main__":
    main()
