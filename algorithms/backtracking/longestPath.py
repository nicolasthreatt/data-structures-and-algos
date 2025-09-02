"""
DoorDash Interview Question

Given a grid of numbers, find the longest path you can take by walking only on adjacent numbers of the same value.
You cannot walk on the same number twice in the same path.

The solution is O(R * C * (4 ^ (R * C)) brute force. Dynamic programming does not work.
[
    [1, 1, 2, 1],
    [5, 5, 5, 5],
    [5, 5, 5, 1]
]
"""

# Algorithm: Depth First Search, Backtracking
# Time Complexity: O(R * C * (4 ^ (R * C)))
# Space Complexity: O(R * C * (4 ^ (R * C)))
def longestPath(grid):
    """Find the longest route in the grid.

    Args:
        grid (List[List[int]]): grid of numbers

    Returns:
        int: longest route
    
     Explanation:
        - The algorithm explores all possible paths in the grid using backtracking.
        - It starts by traversing the grid cell by cell and backtracks when necessary.
        - In each cell, it marks it as visited and increments the path length.
        - It explores all valid adjacent cells with the same value and continues recursively.
        - If a dead end is reached, it backtracks to the previous cell and continues exploring other paths.
        - The algorithm maintains a set of visited cells to avoid revisiting the same cell in the same path.
        - By exploring all paths and keeping track of the longest one, it finds the length of the longest route.
    """
    # If the grid is empty, return 0
    if not grid or not grid[0]:
        return 0

    # Determine the length of the grid
    ROWS, COLS = len(grid), len(grid[0])

    # Initialize a set to store the visited cells
    visited = set()

    def is_valid_cell(r: int, c int):
        return 0 <= r < ROWS and 0 <= c < COLS

    def dfs(r: int, c: int) -> int:
        # Base Case - If the cell is out of bounds or has been visited, return 0
        area = 0
        if not is_valid_cell(r, c) or (r, c) in visited:
            return area
        
        # Here it is known that the cell is valid and has not been visited
        # Add the cell to the visited set
        visited.add((r, c))
        area = 1

        # Traverse the adjacent cells
        # The adjacent cells are the cells that are horizontally or vertically adjacent to the current cell
        # If the adjacent cell is valid and has the same value as the current cell, increment the area of the island by 1.
        # The maximum area of the island is the maximum of the area of the island and the area of the adjacent cell.
        adjacent_cells = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in adjacent_cells:
            if (
                0 <= r + dr < ROWS
                and 0 <= c + dc < COLS
                and grid[r + dr][c + dc] == grid[r][c]
            ):
                area = max(area, 1 + dfs(r + dr, c + dc))

        # BACKTRACKING - Remove the current path from the visited set 
        # This ensures that the cell can be visited again along in a different path
        visited.remove((r, c))

        # Return the area of the island
        return area

    # Initialize the maximum path to 0
    max_path = 0

    # Traverse the grid (log(R * C))
    # If the cell is not visited, find the maximum path
    for r in range(ROWS):
        for c in range(COLS):
                if (r, c) not in visited:
                    max_path = max(max_path, dfs(r, c)) # O(4 ^ (R * C))

    # Return the maximum path
    return max_path


if __name__ == "__main__":
    grid = [
        [1, 1, 2, 1],
        [5, 5, 5, 5],
        [5, 5, 5, 1]
    ]
    assert longestPath(grid) == 7


    grid = [
        [5, 1, 2, 1],
        [5, 5, 5, 5],
        [5, 5, 5, 1]
    ]
    assert longestPath(grid) == 7

    grid = [
        [4, 4, 4],
        [2, 2, 1],
        [1, 2, 2],
        [1, 1, 1]
    ]
    assert longestPath(grid) == 4

    grid = [
        [3, 3, 3, 3],
        [1, 2, 2, 3],
        [1, 1, 2, 2],
        [4, 4, 4, 4]
    ]
    assert longestPath(grid) == 5
