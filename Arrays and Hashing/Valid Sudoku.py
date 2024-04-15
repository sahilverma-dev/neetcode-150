from typing import List

"""
https://leetcode.com/problems/valid-sudoku/description/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Brute force solution 1
        find the repetition for row,col and 3x3 sub grid
        """
        n = len(board)
        m = len(board[0])
        # both will 9

        for i in range(m):
            row = board[i]
            row_map = {}
            col_map = {}

            for j in range(n):
                # for row
                cell = row[j]
                if cell != ".":
                    if row_map.get(cell) == None:
                        row_map[cell] = cell
                    elif row_map.get(cell) == cell:
                        return False

                # for col
                el = board[j][i]
                if el != ".":
                    if col_map.get(el) == None:
                        col_map[el] = el
                    elif col_map.get(el) == el:
                        return False

        # Check 3x3 sub grids
        for k in range(0, n, 3):
            for l in range(0, m, 3):
                sub_grid_map = {}
                for i in range(k, k + 3):
                    for j in range(l, l + 3):
                        cell = board[i][j]
                        if cell != ".":
                            if sub_grid_map.get(cell) == cell:
                                return False
                            else:
                                sub_grid_map[cell] = cell

        return True


s = Solution()

# Example 1 should return true
print(
    s.isValidSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)


# Example 2 should return false because value is repeating in first col
print(
    s.isValidSudoku(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)

# Example 3 should return false value is repeating in 3x3 sub grid
print(
    s.isValidSudoku(
        [
            [".", ".", ".", ".", "5", ".", ".", "1", "."],
            [".", "4", ".", "3", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "3", ".", ".", "1"],
            #
            ["8", ".", ".", ".", ".", ".", ".", "2", "."],
            [".", ".", "2", ".", "7", ".", ".", ".", "."],
            [".", "1", "5", ".", ".", ".", ".", ".", "."],
            #
            [".", ".", ".", ".", ".", "2", ".", ".", "."],
            [".", "2", ".", "9", ".", ".", ".", ".", "."],
            [".", ".", "4", ".", ".", ".", ".", ".", "."],
        ]
    )
)
