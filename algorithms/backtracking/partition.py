"""
https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
    * 1 <= s.length <= 16
    * s contains only lowercase English letters.
"""

from typing import List


# Algorithm Used: Backtracking (Brute Force), Recursion
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)
def partition(s: str) -> List[List[str]]:
    # Create a list to store all partitions to be returned
    partitions = []

    # Create a list to store the current partition path
    current_partition_path = []

    def dfs(i: int) -> None:
        """Depth-first search (DFS) helper function. Recursively generate all partitions.

        Args:
            i: The current index of the input string.
        """
        # BASE CASE (LAST INDEX OF INPUT STRING):
        #   - If the index being searched is out-of-bounds, append the
        #     current partition path to the partitions list. This means
        #     that the depth first search function has traversed the length
        #     of the input string so the current partition path is a valid partition.
        if i >= len(s):
            partitions.append(current_partition_path.copy())
            return

        # RECURSIVE CASE (NOT AT LAST INDEX OF INPUT STRING):
        #  - Iterate through the input string starting at the current index.
        #  - If the current substring is a palindrome:
        #       * Append the current substring to the current partition path.
        #       * Recursively call the helper function to get the rest of the partitions.
        #       * Backtrack by removing the current substring from the current partition path.
        for j in range(i, len(s)):
            if isPalidrone(s, i, j):
                current_partition_path.append(s[i : j + 1])
                dfs(j + 1)

                # Ensure that the current partition path is not modified by the next iteration of the loop.
                current_partition_path.pop()

    # Start the depth-first search at the first index of the input string.
    dfs(0)

    # Return the list of all partitions.
    return partitions


def isPalidrone(s: str, l: int, r: int) -> bool:
    """Check if the input string is a palindrome.

    Args:
        s: The input string.
        l: The left index of the input string.
        r: The right index of the input string.

    Returns:
        bool: True if the input string is a palindrome, False otherwise.
    """
    # Iterate through the input string from the left and right indices.
    while l < r:
        # If characters at left and right indices are not the same, the input string is not a palindrome.
        if s[l] != s[r]:
            return False

        # Increment the left index and decrement the right index.
        # These will move the indices closer to the middle of the input string.
        l = l + 1
        r = r - 1

    # If the iteration completes successfully, then the input string is a palindrome.
    return True
