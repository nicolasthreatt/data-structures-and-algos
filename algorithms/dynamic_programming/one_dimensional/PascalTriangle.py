"""
Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.

Example 1:
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
    Input: numRows = 1
    Output: [[1]]

Constraints:
    * 1 <= numRows <= 30
"""

from typing import List


class PascalTriangle:

    # Algorithm(s) Used: Recursion, Top-Down
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    def generateI(self, numRows: int) -> List[List[int]]:
        # Base Case
        if numRows == 1:
            return [[1]]

        # Previous Rows
        prevs = self.generateI(numRows - 1)

        # Last Row
        last = prevs[-1]

        # Curr Row
        curr = [1] + [last[i] + last[i + 1] for i in range(len(last) - 1)] + [1] # O(numRums)

        return prevs + [curr]

    # Algorithm(s) Used: Dynammic Programming (1-D), Bottom-Up
    # Time Complexity: O(n^2)
    # Space Compexity: O(n^2)
    def generateII(self, numRows: int) -> List[List[int]]:
        dp = [[1]]

        for i in range(1, numRows):
            prev = dp[i - 1]
            curr = [prev[j] + prev[j + 1] for j in range(i - 1)] # O(numRums)
            dp.append([1] + curr + [1])

        return dp

    # Algorithm(s) Used: Dynammic Programming (1-D), Bottom-Up
    # Time Complexity: O(n^2)
    # Space Compexity: O(n^2)
    def generateIII(self, numRows: int) -> List[List[int]]:
        dp = []

        prev = [1]
        for i in range(numRows):
            dp.append(prev)
            curr = [prev[j] + prev[j + 1] for j in range(i)] # O(numRums)
            prev = [1] + curr + [1]

        return dp


if __name__ == "__main__":
    pascal = PascalTriangle()

    test_cases = [
        (1, [[1]]),
        (2, [[1], [1, 1]]),
        (3, [[1], [1, 1], [1, 2, 1]]),
        (4, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]),
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (6, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]),
    ]

    for func in [pascal.generateI, pascal.generateII, pascal.generateIII]:
        for numRows, expected in test_cases:
            result = func(numRows)
            assert result == expected
