"""
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

You are given an array of strings arr.
A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by
deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are
- "chaers" ("cha" + "ers")
- "acters" ("act" + "ers").

Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.

Constraints:
    - 1 <= arr.length <= 16
    - 1 <= arr[i].length <= 26
    - arr[i] contains only lowercase English letters.
"""

from typing import List


# Algorithm Used: Backtracking, Recursion
# Time Complexity: O(n * 2^n), where n is the length of the input array
# Space Complexity: O(n * 2^n), where n is the length of the input array
def maxLength(arr: List[str]) -> int:
    charSet = set()

    def overlap(charSet: set, s: str):
        """
        Check if the current string overlaps with the current character set.

        Args:
            charSet (set): The current character set.
            s (str): The current string.

        Returns:
            bool: True if the current string overlaps with the current character set, False otherwise.
        """
        # Create a set to store the previous characters in the current string.
        prev = set()

        # Iterate through the current string.
        # If the current character is in the current character set or the previous characters set, return True.
        # Otherwise, add the current character to the previous characters set.
        # After iterating through the current string its known that the current string does not overlap with the
        # current character set, so return False.
        for c in s:
            if c in charSet or c in prev:
                return True
            prev.add(c)

        return False

    def backtrack(i: int) -> int:
        # BASE CASE:
        #   - If the current index is greater than or equal to the length of the input array,
        #     return the length of the current character set.
        if i >= len(arr):  # OUT-OF-BOUNDS CHECK
            return len(charSet)

        # For each recursive call, initialize the max length to 0.
        # Remember that the base case returns the length of the current character set.
        max_len = 0

        # RECURSIVE CASE I (INCLUDE CURRENT STRING):
        #   - If the current string does not overlap, meaning containing no duplicates, with the current character set:
        #       * Add the current string to the current character set.
        #       * Recursively call the backtrack function to get the rest of the character set.
        #       * Backtrack by removing the current string from the current character set.
        if not overlap(charSet, arr[i]):
            for c in arr[i]:
                charSet.add(c)

            # Since the base case returns the length of the current character set, the max length is the max of the
            # current character set and the rest of the character set.
            max_len = backtrack(i + 1)

            for c in arr[i]:
                charSet.remove(c)  # BACKTRACK/CLEANUP

        # RECURSIVE CASE II (DO NOT INCLUDE CURRENT STRING):
        #   - Recursively call the backtrack function to get the rest of the character set.
        #   - The max length is the max of the current character set and the rest of the character set.
        return max(max_len, backtrack(i + 1))

    # Call the backtrack function with the starting index of 0.
    return backtrack(0)
