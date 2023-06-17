"""
https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
    Input: matrix = [[1]]
    Output: [[1]]

Example 3:
    Input: matrix = [[1,2],[3,4]]
    Output: [[3,1],[4,2]]

Example 4:
    Input: matrix = [5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
    * matrix.length == n
    * matrix[i].length == n
    * 1 <= n <= 20
    * -1000 <= matrix[i][j] <= 1000
"""

# Algorithm Used: Matrix, Spiral Order
# Time Complexity: O(n^2)
# Space Complexity: O(1)
from typing import List

def rotate(matrix: List[List[int]]) -> None:
    # Initialize the left and right boundaries
    # -1 in the right boundary because the right boundary is not inclusive
    left, right = 0, len(matrix[0]) - 1

    # Continue rotating until the left boundary becomes greater than the right boundary
    while left < right:
        # Iterate over the elements in the current layer, which is represented by the right - left
        # NOTE: i is the index of the element in the current layer
        for i in range(right - left):
            # Initialize the top, bottom, left, and right boundaries of the current layer
            top, bottom = left, right

            # Save the value of the top-left element in a temporary variable
            top_left = matrix[top][left + i]

            # Move the bottom-left element into the top-left position
            matrix[top][left + i] = matrix[bottom - i][left]

            # Move the bottom-right element into the bottom-left position
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # Move the top-right element into the bottom-right position
            matrix[bottom][right - i] = matrix[top + i][right]

            # Move the top-left element into the top-right position
            matrix[top + i][right] = top_left

        # Update the boundaries to move to the next inner layer
        right -= 1
        left += 1
