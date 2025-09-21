"""
Count Negative Numbers in a Sorted Matrix
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
return the number of negative numbers in grid.

Example 1:
    Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    Output: 8
    Explanation: There are 8 negatives number in the matrix.

Example 2:
    Input: grid = [[3,2],[1,0]]
    Output: 0

Constraints:
    * m == grid.length
    * n == grid[i].length
    * 1 <= m, n <= 100
    * -100 <= grid[i][j] <= 100

"""

from typing import List


# Algorithm Used: Binary Search
# Time Complexity: O(mlog(n))
# Space Complexity: O(1)
def countNegativesI(grid: List[List[int]]) -> int:
    negatives = 0

    # Binary search for the negative letters in the array
    def binary_search(row: List[int]) -> int:
        l, r = 0, len(row) - 1
        while l <= r:
            m = (l + r) // 2
            if row[m] >= 0:  # Keep pushing until past all positive numbers
                l = m + 1
            else:
                r = m - 1
        return len(row) - l  # l will be first instance of negative number
    
    for row in grid:
        negatives += binary_search(row)  # Count negatives in each row

    return negatives


# Algorithm Used: Two Pointers
# Time Complexity: O(m + n)
# Space Complexity: O(1)
def countNegativesII(grid: List[List[int]]) -> int:
    negatives = 0

    # Start at bottom-left corner in grid
    i = len(grid) - 1
    j = 0

    # Move up OR right until out of bounds
    while i >= 0 and j < len(grid[0]):
        if grid[i][j] < 0:
            negatives += len(grid[0]) - j  # Count negtaives along current row
            i -= 1  # Move one row up
        else:
            j += 1  # Current value is positive, so move right until negative

    return negatives


if __name__ == "__main__":
    grid1 = [[4, 3, 2, -1],
             [3, 2, 1, -1],
             [1, 1, -1, -2],
             [-1, -1, -2, -3]]

    grid2 = [[3, 2],
             [1, 0]]

    grid3 = [[-1]]

    grid4 = [[5, 1, 0],
             [-5, -5, -5]]

    for func in [countNegativesI, countNegativesII]:
        assert func(grid1) == 8      # multiple negatives in different rows
        assert func(grid2) == 0      # no negatives
        assert func(grid3) == 1      # single negative element
        assert func(grid4) == 3      # second row all negatives
        assert func([[1]]) == 0      # single positive element
        assert func([[0]]) == 0      # single zero element
