"""
https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word,
return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
    * m == board.length
    * n = board[i].length
    * 1 <= m, n <= 6
    * 1 <= word.length <= 15
    * board and word consists of only lowercase and uppercase English letters.
 

Follow up:
    * Could you use search pruning to make your solution faster with a larger board?
"""

from typing import List


# Algorithms Used:
#   - Backtracking
#   - Recursion
#   - DFS
# Time Complexity: O(m*n*4^s), where
#   - m is the number of rows
#   - n is the number of columns
#   - s is the length of the word
# Space Complexity: O(m*n), where
#   - m is the number of rows
#   - n is the number of columns
def existI(board: List[List[str]], word: str) -> bool:
    # Count the number of rows and columns in the board.
    ROWS, COLS = len(board), len(board[0])

    # Initialize a set to store the visited cells.
    # This is necessary because we cannot visit the same cell twice.
    path = set()

    # Create depth first search function to traverse the board which takes in the row, column, and index of the word.
    # Returns True if the word exists in the board, False otherwise.
    def dfs(r, c, i):
        # If the current length is equal to the length of the word, return True.
        # This means that we have found the word.
        if i == len(word):
            return True

        # If the current row or column is out of bounds, return False.
        if (
            r < 0  # Check if row is out of bounds.
            or r >= ROWS  # Check if row is out of bounds.
            or c < 0  # Check if column is out of bounds.
            or c >= COLS  # Check if column is out of bounds.
            or word[i] != board[r][c]  # Check if letter isnt equal to letter in board.
            or (r, c) in path  # Check if cell has already been visited.
        ):
            return False

        # Add the current cell to the path since it has not been visited yet.
        path.add((r, c))

        # Create a variable to store the result of the dfs function.
        # Note that we are incrementing the index by 1 since we have found the current letter.
        exists = (
            dfs(r + 1, c, i + 1)  # Check the cell below.
            or dfs(r - 1, c, i + 1)  # Check the cell above.
            or dfs(r, c + 1, i + 1)  # Check the cell to the right.
            or dfs(r, c - 1, i + 1)  # Check the cell to the left.
        )

        # Remove the current cell from the path since we have already visited it.
        path.remove((r, c))

        return exists

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True


# Algorithms Used:
# Time Complexity:
# Space Complexity:
def existII(board: List[List[str]], word: str) -> bool:
    pass
