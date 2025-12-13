"""
Is Subsequence
https://leetcode.com/problems/is-subsequence/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters.
    - i.e., "ace" is a subsequence of "abcde" while "aec" is not)

Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true

Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false

Constraints:
    * 0 <= s.length <= 100
    * 0 <= t.length <= 10^4
    * s and t consist only of lowercase English letters.

Follow up:
    * Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109,
      and you want to check one by one to see if t has its subsequence.
      In this scenario, how would you change your code?
"""


class IsSubsequence:

    # Algorithm(s) Used: Greedy, Two Pointers
    # Time Complexity: O(t)
    # Space Complexity: O(1)
    def isSubsequenceI(self, s: str, t: str) -> bool:
        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # Local Optimal
                i += 1
            j += 1

        return i == len(s)  # Global Optimal

    # Algorithm(s) Used: Dynammic Programming (2-D), Depth First Search (DFS), Top-Down
    # Time Complexity: O(s * t)
    # Space Complexity: O(s + t)
    def isSubsequenceII(self, s: str, t: str) -> bool:
        def dfs(i: int, j: int) -> bool:
            if i == len(s):
                return True
            
            if j == len(t):
                return False
            
            # Match Found - Increment 's' counter
            if s[i] == t[j]:
                if dfs(i + 1, j + 1):
                    return True

            return dfs(i, j + 1)

        return dfs(0, 0)

    # Algorithm(s) Used: Dynammic Programming (2-D), DFS, Top-Down, Memoization
    # Time Complexity: O(s * t)
    # Space Complexity: O(s * t)
    def isSubsequenceIII(self, s: str, t: str) -> bool:
        memo = {}

        def dfs(i, j):
            if i == len(s):
                return True

            if j == len(t):
                return False

            if (i, j) in memo:
                return memo[(i, j)]

            # Match Found - Increment 's' counter
            if s[i] == t[j]:
                if dfs(i + 1, j + 1):
                    memo[(i, j)] = True
                    return True

            memo[(i, j)] = dfs(i, j + 1)
            return memo[(i, j)]

        return dfs(0, 0)

    # Algorithm(s) Used: Dynammic Programming (2-D), Buttom-Up
    # Time Complexity: O(s * t)
    # Space Complexity: O(s * t)
    def isSubsequenceIV(self, s: str, t: str) -> bool:
        r, c = len(s), len(t)
        dp = [[0] * (c + 1) for _ in range(r + 1)]

        for i in range(1, r + 1):
            for j in range(1, c + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]  # Traverse Board Up and Left
                else:
                    dp[i][j] = dp[i][j - 1]  # Traverse Board Up

        return dp[r][c] == len(s)


if __name__ == "__main__":
    Solution = IsSubsequence()

    test_cases = [
        # (s, t, expected)
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
        ("", "abc", True),
        ("abc", "", False),
        ("a", "a", True),
        ("b", "a", False),
        ("aaaa", "aaaaaaaaaa", True),
        ("abc", "abc", True),
        ("abc", "acb", False),
        ("ace", "abcde", True),
    ]

    for func in [
        Solution.isSubsequenceI,
        Solution.isSubsequenceII,
        Solution.isSubsequenceIII,
        Solution.isSubsequenceIV,
    ]:
        for s, t, expected in test_cases:
            result = func(s, t)
            assert result == expected
