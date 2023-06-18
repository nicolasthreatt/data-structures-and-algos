"""
https://leetcode.com/problems/max-area-of-island/

You are given an m x n binary matrix grid.
An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:

    Input:
        grid = [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]
    Output: 6
    Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:
    * m == grid.length
    * n == grid[i].length
    * 1 <= m, n <= 50
    * grid[i][j] is either 0 or 1.
"""

from collections import deque
from typing import List


# Algorithm Used: Graph, Deph First Search
# Time Complexity: O(m*n), where m is the number of rows and n is the number of columns
# Space Complexity: O(m*n), where m is the number of rows and n is the number of columns
def maxAreaOfIsland(grid: List[List[int]]) -> int:
    # If the grid is empty, return 0
    if not grid or not grid[0]:
        return 0

    # Count the number of rows and columns in the grid
    ROWS, COLS = len(grid), len(grid[0])

    # Initialize a set to store the visited cells.
    visited = set()

    def dfs(r: int, c: int) -> int:
        """Depth First Search helper function to traverse the grid.

        Args:
            r (int): row index
            c (int): column index

        Returns:
            int: area of the island
        """
        # Initally the area of the island is 0
        area = 0

        # If the cell is out of bounds or is water or is already visited, return 0
        if (
            r < 0 or
            r >= ROWS or 
            c < 0 or
            c >= COLS or
            grid[r][c] == 0 or 
            (r, c) in visited
        ):
            return area
        
        # Here it is known that the cell is land and is not visited so add it to the visited set
        # Increment the area of the island by 1
        visited.add((r,c))
        area = 1
        
        # Traverse the adjacent cells
        # The adjacent cells are the cells that are horizontally or vertically adjacent to the current cell
        adjacent_cells = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in adjacent_cells:
            # Increment the area of the island by the area of the adjacent cells
            area += dfs(r + dr, c + dc)

        # Return the area of the island
        return area

    # Initialize the area of the island to 0
    max_area = 0

    # Traverse the grid
    # If the cell is land and is not visited, find the maximum area of the island
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1 and (r, c) not in visited:
                max_area = max(max_area, dfs(r, c))
    
    # Return the max area of the grid
    return max_area