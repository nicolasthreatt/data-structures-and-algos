"""
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map
of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically.

You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
    * m == grid.length
    * n == grid[i].length
    * 1 <= m, n <= 300
    * grid[i][j] is '0' or '1'.
"""

from collections import deque
from typing import List


# Algorithm Used: Graph, Deph First Search
# Time Complexity: O(m*n), where m is the number of rows and n is the number of columns
# Space Complexity: O(m*n), where m is the number of rows and n is the number of columns
def numIslandsI(grid: List[List[str]]) -> int:
    # If the grid is empty, return 0
    if not grid or not grid[0]:
        return 0

    # Count the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])

    # Initialize a set to store the visited cells.
    visit = set()

    # Initialize a variable that'll return the number of islands
    islands = 0

    def dfs(r: int, c: int) -> None:
        """Depth First Search helper function to traverse the grid.

        DFS will visit all adjacent cells first before moving on to the next cell.

        Args:
            r (int): The row of the current cell.
            c (int): The column of the current cell.
        """
        # BASE CASE:
        # If the current cell is not land and has been visited, return.
        # This is to avoid infinite recursion.
        if (
            r not in range(rows)  # Out-of-bounds check
            or c not in range(cols)  # Out-of-bounds check
            or grid[r][c] != "1"  # Non-land cell
            or (r, c) in visit  # Visited cell
        ):
            return  # End the recursion which signifies the end of an island

        # Here its known that the current cell is land and has not been visited.
        # For each recursive call, mark the current cell as visited
        visit.add((r, c))

        # Recursively visit all adjacent cells, which will treat each adjacent cell as first cell in island.
        adjacent_cells = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # right, left, above, below
        for adjacent_r, adjacent_c in adjacent_cells:
            dfs(r + adjacent_r, c + adjacent_c)

    # Iterate through the grid and find all islands
    for r in range(rows):
        for c in range(cols):
            # If the current cell is land and has not been visited, visit it and increment the number of islands
            if grid[r][c] == "1" and (r, c) not in visit:
                dfs(r, c)
                islands += 1

    # Return the number of islands
    return islands


# Algorithm Used: Graph, Breadth First Search
# Time Complexity: O(m*n), where m is the number of rows and n is the number of columns
# Space Complexity: O(m*n), where m is the number of rows and n is the number of columns
def numIslandsII(grid: List[List[str]]) -> int:
    # If the grid is empty, return 0
    if not grid:
        return 0

    # Count the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])

    # Initialize a set to store the visited cells.
    visit = set()

    # Initialize a variable that'll return the number of islands
    islands = 0

    def bfs(r, c):
        """Breadth First Search helper function to traverse the grid.
        Finds all adjacent cells that are land and marks them as visited.

        BFS is used here because we want to visit all adjacent cells first.
        This is because BFS uses a queue to store the cells to visit.

        Args:
            r (int): The row of the current cell.
            c (int): The column of the current cell.
        """
        # Initialize a queue to store the cells to visit and add the current cell to the queue
        queue = deque((r, c))

        # Mark the current cell as visited and add it to the queue
        visit.add((r, c))

        # While the queue is not empty, visit all adjacent cells and mark them as visited
        while queue:
            row, col = queue.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # right, left, above, below

            for dr, dc in directions:
                # Get the adjacent cell
                r, c = row + dr, col + dc

                # If the adjacent cell is land and has not been visited,
                # add it to the queue and mark it as visited. Otherwise, skip it.
                if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visit:
                    queue.append((r, c))
                    visit.add((r, c))

    # Iterate through the grid and find all islands
    # If the current cell is land and has not been visited, visit it and increment the number of islands
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visit:
                bfs(r, c)
                islands += 1

    # Return the number of islands
    return islands
