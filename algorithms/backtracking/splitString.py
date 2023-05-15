"""
https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

You are given a string s that consists of only digits.

Check if we can split s into two or more non-empty substrings such that the
numerical values of the substrings are in descending order and the difference
between numerical values of every two adjacent substrings is equal to 1.

For example, the string s = "0090089" can be split into ["0090", "089"] with numerical values [90,89].
The values are in descending order and adjacent values differ by 1, so this way is valid.

Another example, the string s = "001" can be split into ["0", "01"], ["00", "1"], or ["0", "0", "1"]
However all the ways are invalid because they have numerical values [0,1], [0,1], and [0,0,1] respectively,
all of which are not in descending order.

Return true if it is possible to split `s` as described above, or false otherwise.

A substring is a contiguous sequence of characters in a string.

Example 1:
Input: s = "1234"
Output: false
Explanation: There is no valid way to split s.

Example 2:
Input: s = "050043"
Output: true
Explanation: s can be split into ["05", "004", "3"] with numerical values [5,4,3].
The values are in descending order with adjacent values differing by 1.

Example 3:
Input: s = "9080701"
Output: false
Explanation: There is no valid way to split s.

Constraints:
    * 1 <= s.length <= 20
    * s only consists of digits.
"""


# Algorithm Used: Backtracking (Brute Force)
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def splitString(s: str) -> bool:
    # Create a helper function to perform backtracking
    def dfs(i: int, prev: int) -> bool:
        """DFS helper function to perform backtracking.

        Args:
            i (int): The index of the current substring
            prev (int): The previous value of the substring.

        Returns:
            bool: True if the string can be split, False otherwise
        """
        # BASE CASE (LAST INDEX OF INPUT STRING):
        #   - If the index being searched equal to the length of the input string, return True.
        #     This means that the depth first search function has traversed the length
        #     of the input string so the string can be split.
        if i == len(s):
            return True

        # RECURSIVE CASE (NOT AT LAST INDEX OF INPUT STRING):
        #  - Iterate through the input string starting at the current index.
        for j in range(i, len(s)):
            # Get the current substring
            val = int(s[i : j + 1])

            # Check if the current substring value is valid by comparing it to the previous substring value
            # Backtrack by recursively calling the depth first search function on the next substring
            # From problem description, difference between numerical values of every two adjacent substrings is equal to 1
            # NOTE: dfs(j + 1, val) will only executes if val == prev - 1 is True. This save timme and memory space.
            if val + 1 == prev and dfs(j + 1, val):
                return True

        # If the for loop completes without returning True, then the string cannot be split
        return False

    # Determine the first substring
    # NOTE: From problem description, s must be split into two or more substrings
    for i in range(len(s) - 1):
        # Look for a substring from index 0 to index i + 1
        val = int(s[: 1 + i])

        # Recursively check if the backtracking returns True (i.e. the remaining string can be split)
        if dfs(s[i + 1 :], val):
            return True

    # If the for loop completes without returning True, then the string cannot be split
    return False
