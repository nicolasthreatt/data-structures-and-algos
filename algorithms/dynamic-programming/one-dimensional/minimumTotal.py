"""
https://leetcode.com/problems/triangle/

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below.
More formally, if you are on index i on the current row,
you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10

Constraints:
    * 1 <= triangle.length <= 200
    * triangle[0].length == 1
    * triangle[i].length == triangle[i - 1].length + 1
    * -10^4 <= triangle[i][j] <= 10^4
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Dynamic Programming, Buttom-Up, Fibonacci Sequence, Binary Tree
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def minimumTotalII(triangle: List[List[int]]) -> int:
    # Initialize an list to keep track of all the elements on the current bottom row + 1
    #  - row + 1 is to account for the last row which will be all 0s because the minimum value
    #    at the botton row will be the bottom most element.
    # NOTE: Every row will increase by an increment of one in the triangle, thus the bottom
    #       row sum size will be incrementally increased from the last subarray group size
    dp = [0] * (len(triangle) + 1)

    # Iterate through the triangle starting at the bottom row
    #   - In other words, iterate array in reverse order
    for row in triangle[::-1]:
        # For each row, iterate through the element in the list and find the minimum path sum
        # NOTE: enumerate() is used to keep track of the index of the element in the list
        for i, n in enumerate(row):
            # NOTE: dp contains the row's BELOW sum for each element
            # For every element on each row, find its two child nodes:
            #   - This done by finding the minimum value of the row below's child nodes
            #       > n is the current element in the row
            #       > dp[i] is the row below's left child node
            #       > dp[i + 1] is the row below's right child node
            dp[i] = n + min(dp[i], dp[i + 1])

    # The minimum path sum will be the first element in the dp list
    # This is because the first element in the dp list is the minimum path sum of the top element
    return dp[0]
