"""
https://leetcode.com/problems/pacific-atlantic-water-flow/

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges,
and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells.
You are given an m x n integer matrix heights where heights[r][c]
represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly
north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height.
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci]
denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Example 2:
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

Constraints:
    * m == heights.length
    * n == heights[r].length
    * 1 <= m, n <= 200
    * 0 <= heights[r][c] <= 105
"""

from typing import List


# Algorithm Used: Graph, Depth First Search
# Time Complexity: O(m*n), where m is the number of rows and n is the number of columns
# Space Complexity: O(m*n), where m is the number of rows and n is the number of columns
def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    ROWS, COLS = len(heights), len(heights[0])
    pacific, atlantic = set(), set()

    def dfs(r: int, c: int, visit: set, prev_height: int) -> None:
        """Depth First Search helper function to traverse the grid.

        Checks if the cell has already been visited or is invalid.
        If it is valid, then add it to the visited set and recursively call dfs on all adjacent cells.

        Args:
            r (int): The row of the current cell.
            c (int): The column of the current cell.
            visit (set): The set of visited cells.
            prev_height (int): The height of the previous cell.
        """
        # BASE CASE (INVALID CALL/PATH)
        # NOTE: Water can only flow from adjacent cells with a less than or equal value,
        #       so it is okay to pass in the same value for the previous position.
        if (
            (r, c) in visit  # Cell already visited
            or r < 0  # Row out of bounds
            or r >= ROWS  # Row out of bounds
            or c < 0  # Column out of bounds
            or c >= COLS  # Columns out of bounds
            or heights[r][c] < prev_height  # Invalid condition
        ):
            return

        # Here its known that the cell has not been visited and is a valid path,
        # so add it to the visited set and recursively call dfs on all adjacent cells
        visit.add((r, c))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # right, left, above, below

        for dr, dc in directions:  # Iterate through all adjacent cells
            # NOTE: The previous height is the current height of the cell
            dfs(r + dr, c + dc, visit, heights[r][c])

    # Iterate through every COLUMN in the FIRST AND LAST ROWS of the graph:
    #   - FIRST ROW will get all cells that border the PACIFIC ocean
    #   - LAST ROW will get all cells that border the ATLANTIC ocean
    for c in range(COLS):
        dfs(0, c, pacific, heights[0][c])  # FIRST ROW - PACIFIFC
        dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])  # LAST ROW - ATLANTIC

    # Iterate through every ROW in the FIRST AND LAST COLUMNS of the graph:
    #   - FIRST COLUMN will get all cells that border the PACIFIC ocean
    #   - LAST COLUMN will get all cells that border the ATLANTIC ocean
    for r in range(ROWS):
        dfs(r, 0, pacific, heights[r][0])  # FIRST COLUMN - PACIFIFC
        dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])  # LAST COLUMN - ATLANTIC

    # Iterate through all cells in the graph and check if they are in both the PACIFIC and ATLANTIC sets
    valid_cells = []
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in pacific and (r, c) in atlantic:
                valid_cells.append([r, c])

    # Return the list of valid cells
    return valid_cells
