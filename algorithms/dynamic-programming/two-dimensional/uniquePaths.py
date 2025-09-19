"""
https://leetcode.com/problems/unique-paths/

There is a robot on an m x n grid.
The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths
that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
    Input: m = 3, n = 7
    Output: 28

Example 2:
    Input: m = 3, n = 2
    Output: 3
    Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Down -> Down
    2. Down -> Down -> Right
    3. Down -> Right -> Down
 

Constraints:
    * 1 <= m, n <= 100
"""

from functools import cache


# Algorithm Used: Depth First Search
# Time Complexity: O(m * n)
# Memory Complexity: O(m * n)
def uniquePathsI(m: int, n: int) -> int:
    @cache
    def dfs(i: int, j: int) -> :
        # Base Case: Out of Bound
        if i >= m or j >= n:
            return 0
        
        # Base Case: End of Valid Path
        if i == m - 1 and j == n - 1:
            return 1
        
        down, right = dfs(i + 1, j), dfs(i, j + 1)
        return down + right

    return dfs(0, 0)


# Algorithm Used: Dynamic Programming, Two-Dimensional, Buttom-Up
# Time Complexity: O(m * n)
# Memory Complexity: O(n)
def uniquePathsII(m: int, n: int) -> int:
    # Start with the bottom row: only one path from each cell (move right)
    # NOTE: Each cell will represent the number of paths to the bottom right corner
    paths_to_bottom_right = [1] * n

    # Work upwards through the grid, row by row
    for _ in range(m - 1):
        current_row = [1] * n  # Right-most cell always has one path (move down)

        # Loop from second-last column to first (right to left)
        # NOTE: Skip last column because it's already 1 and has no right neighbor
        for j in range(n - 2, -1, -1):
            # Paths from this cell = right neighbor + below (from previous row)
            current_row[j] = current_row[j + 1] + paths_to_bottom_right[j]

        # Prepare for next iteration (move up one row)
        paths_to_bottom_right = current_row

    return paths_to_bottom_right[0]  # Number of paths from top-left


