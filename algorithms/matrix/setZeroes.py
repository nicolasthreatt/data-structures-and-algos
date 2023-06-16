"""
https://leetcode.com/problems/set-matrix-zeroes/

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
    * m == matrix.length
    * n == matrix[0].length
    * 1 <= m, n <= 200
    * -2^31 <= matrix[i][j] <= 2^31 - 1
"""


# Algorithm Used: Matrix, Spiral Order
# Time Complexity: O(m * n)
# Space Complexity: O(m + n)
def setZeroesI(matrix: List[List[int]]) -> None:
    pass


# Algorithm Used: Matrix, Spiral Order
# Time Complexity: O(m * n)
# Space Complexity: O(1)
def setZeroesII(matrix: List[List[int]]) -> None:
    # Get the number of rows and columns in the matrix
    ROWS, COLS = len(matrix), len(matrix[0])

    # Initialize a boolean to determine if the first row needs to be zeroed
    # This will be used to determine if the first column needs to be zeroed
    # as it cannot be done in place since it will affect the first row.
    # The first row will be zero if there is a zero in any column of the first row.
    # NOTE: If the first row is zero, the top-left cell (0, 0) will be zero, but
    #       this cannot be done in place since it will affect the first column.
    is_first_row_zero = False

    # Iterate through each cell in the matrix
    # If a cell value is zero, update the corresponding cells in the first row and first column
    # This will mark the presence of zero in that row and column for later processing
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0  # Update corresponding cell in the first row
                if r > 0:
                    matrix[r][0] = 0  # Update corresponding cell in the first column
                else:  # r == 0
                    is_first_row_zero = True  # Set the flag indicating the first row has a zero

    # Iterate through the matrix (excluding first row and first column)
    # This is done to avoid zeroing the first row and first column prematurely.
    # If the corresponding cell in the first row or first column is zero, set the cell to zero
    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    # Check if the top-left cell (0, 0) is zero
    # If it is zero, set the entire first column to zero
    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0

    # Check if the first row needs to be zeroed
    # If the flag is set, set every cell in the first row to zero
    if is_first_row_zero:
        for c in range(COLS):
            matrix[0][c] = 0
