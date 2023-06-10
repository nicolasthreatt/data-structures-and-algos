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


# Algorithm Used: Dynamic Programming, Two-Dimensional, Buttom-Up, 0-1 Knapsack
# Time Complexity: O(m * n)
# Memory Complexity: O(n)
def uniquePaths(m: int, n: int) -> int:
    # Initialize the bottom row of the grid with all cells set to 1
    # This is because there is only one way for each cell in the bottom row
    # to reach the bottom right corner, which is to move right.
    # NOTE: Each cell will represent the number of paths to the bottom right corner
    paths_to_bottom_right = [1] * n

    # Iterate through the grid, starting from the second to last row
    # (since the bottom row is already set to 1's)
    for i in range(m - 1):
        # Initialize the current row with all cells set to 1
        # This is done because initially, each cell in the current row has only one possible path
        # to reach the bottom right corner, which is to move directly right.
        current_row = [1] * n

        # Iterate through the row, starting from the second to last column
        # Calculate the number of paths (right and below) to the bottom
        # right corner for each cell in the current row.
        for j in range(n - 2, -1, -1):
            paths_to_right = current_row[j + 1]
            paths_below = paths_to_bottom_right[j]
            current_row[j] = paths_to_right + paths_below

        # Update the paths_to_bottom_right variable to be used in the next iteration
        paths_to_bottom_right = current_row
    
    # Return the number of paths to the bottom right corner from the top left corner
    return paths_to_bottom_right[0]

