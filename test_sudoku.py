"""tests for sudoku solver"""

from sudoku import get_solutions
from samples import medium_sudoku


def test_medium_sudoku():
    """test the medium sudoku solution"""
    solution = next(get_solutions(medium_sudoku))

    # the solution extends the given sudoku
    assert all(
        medium_sudoku[i][j] == solution[i][j]
        for i in range(9)
        for j in range(9)
        if medium_sudoku[i][j] > 0
    )
    # each row has 9 numbers
    for row in range(9):
        assert len(set(solution[row])) == 9

    # each column has 9 numbers
    for col in range(9):
        assert len(set(solution[row][col] for row in range(9))) == 9

    # each block has 9 numbers
    for start_row in range(0, 9, 3):
        for start_col in range(0, 9, 3):
            block = {
                solution[start_row + i][start_col + j]
                for i in range(3)
                for j in range(3)
            }
            assert len(block) == 9
