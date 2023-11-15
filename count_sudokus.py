"""computation of all sudokus"""

from sudoku import get_solutions
from samples import first_row_given


def main():
    """computes the number of all complete sudokus, up to permutation of numbers,
    by generating all solutions to the underdetermined sudoku with only
    the first row given as (1,2,...,9)
    """
    counter = 0
    solutions = get_solutions(first_row_given)
    for _ in solutions:
        counter += 1
        if counter % 1000 == 0:
            print(counter)
    print(f"\nThere are {counter} sudokus (up to permutation of numbers)")


if __name__ == "__main__":
    main()
