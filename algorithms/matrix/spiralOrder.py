"""
https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

Example 2:
    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
    * m == matrix.length
    * n == matrix[i].length
    * 1 <= m, n <= 10
    * -100 <= matrix[i][j] <= 100
"""


# Algorithm Used: Matrix, Spiral Order
# Time Complexity: O(m * n)
# Space Complexity: O(1)
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    # Initialize the top, bottom, left, and right boundaries
    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])

    # Initialize a list to store the spiral order of the matrix
    spiral_order = []

    # Iterate through matrix (while lleft < right and top < bottom) and append each element to the spiral order list
    # During each iteration, update the boundaries to ensure that the next iteration will not traverse same row or column again.
    # The boundaries are updated in the following order:
    #     - top columns -> right-most rows -> bottom column-> left-most rows
    # Repeat until the top and bottom or left and right boundaries meet
    while left < right and top < bottom:
        # Get every column in the top row
        for i in range(left, right):
            spiral_order.append(matrix[top][i])
        top += 1

        # Get every row in the right most column
        for i in range(top, bottom):
            spiral_order.append(matrix[i][right - 1])
        right -= 1

        # Reverify that the top and bottom or left and right boundaries meet
        if not (left < right and top < bottom):
            break

        # Get every column in the bottom row
        for i in reversed(range(left, right)):
            spiral_order.append(matrix[bottom - 1][i])
        bottom -= 1

        # Get every column in the left most column
        for i in reversed(range(top, bottom)):
            spiral_order.append(matrix[i][left])
        left += 1

    # Return the spiral order of the matrix
    return spiral_order
