"""
Unique Paths
https://leetcode.com/problems/unique-paths/

There is a robot on an m x n grid.

The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths
that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
    Input: m = 3, n = 7
    Output: 28

Example 2:
    Input: m = 3, n = 2
    Output: 3
    Explanation:
        From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
            1. Right -> Down -> Down
            2. Down -> Down -> Right
            3. Down -> Right -> Down

Constraints:
    * 1 <= m, n <= 100
"""


class UniquePaths:
    def __init__(self):
        self.memo = {}

    # Algorithm Used: Brute Force, Depth First Search
    # Time Complexity: O(2^(m * n))
    # Space Complexity: O(m + n)
    def uniquePathsI(self, m: int, n: int) -> int:
        self.ROWS = m
        self.COLS = n

        def dfs(i: int, j: int) -> int:

            # Base Case: Out of Bound
            if i >= self.ROWS or j >= self.COLS:
                return 0
            
            # Base Case: End of Valid Path
            if i == self.ROWS - 1 and j == self.COLS - 1:
                return 1
            
            down, right = dfs(i + 1, j), dfs(i, j + 1)
            return down + right

        return dfs(0, 0)

    # Algorithm Used: Dynammic Programming, Top Down, Memoization, Depth First Search
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def uniquePathsII(self, m: int, n: int) -> int:
        self.ROWS = m
        self.COLS = n

        def dfs(i: int, j: int) -> int:
            # Base Case: Out of Bound
            if i >= self.ROWS or j >= self.COLS:
                return 0

            # Base Case: End of Valid Path
            if i == self.ROWS - 1 and j == self.COLS - 1:
                return 1
            
            key = (i, j)
            if key in self.memo:
                return self.memo[key]

            down, right = dfs(i, j + 1), dfs(i + 1, j)

            self.memo[key] = down + right
            return self.memo[key]

        return dfs(0, 0)

    # Algorithm Used: Dynamic Programming (2-D), Buttom-Up, Tabulation
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def uniquePathsIII(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        # Base Case: Only 1 Valid Path From Last Row
        for i in range(m):
            dp[i][0] = 1

        # Base Case: Only 1 Valid Path From Last Row
        for j in range(n):
            dp[0][j] = 1

        # Traverse each row from top to bottom (excluding last row)
        # Traverse each column from left to right (excluding last column)
        for i in range(1, m):
            for j in range(1, n):
                top = dp[i - 1][j]
                left = dp[i][j - 1]

                dp[i][j] = top + left

        return dp[m - 1][n - 1]

    # Algorithm Used: Dynamic Programming (1-D), Buttom-Up, Tabulation
    # Time Complexity: O(m * n)
    # Space Complexity: O(n)
    def uniquePathsIV(self, m: int, n: int) -> int:
        # Start from the FIRST row
        dp = [1] * n  # dp[j] = number of unique paths to reach column j in the current row

        # Traverse each row from top to bottom (excluding the first row)
        # Traverse each column from left to right (excluding the first column)
        for _ in range(1, m):
            for j in range(1, n):
                top = dp[j]
                left = dp[j - 1]

                dp[j] = top + left

        return dp[n - 1]


if __name__ == "__main__":
    Solution = UniquePaths()

    test_cases = [
        ((3, 7), 28),
        ((3, 2), 3),
        ((1, 1), 1),
        ((1, 5), 1),
        ((5, 1), 1),
        ((2, 2), 2),
        ((2, 3), 3),
        ((3, 3), 6),
        ((3, 4), 10),
        ((4, 4), 20),
        ((5, 5), 70),
        ((10, 10), 48620),
    ]

    for func in [
        Solution.uniquePathsI,
        Solution.uniquePathsII,
        Solution.uniquePathsIII,
        Solution.uniquePathsIV,
    ]:
        for (m, n), expected in test_cases:
            Solution.memo = {}
            assert func(m, n) == expected
