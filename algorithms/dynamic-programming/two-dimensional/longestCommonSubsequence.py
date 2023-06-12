"""
https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some
characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
    Input: text1 = "abcde", text2 = "ace" 
    Output: 3  
    Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
    Input: text1 = "abc", text2 = "abc"
    Output: 3
    Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
    Input: text1 = "abc", text2 = "def"
    Output: 0
    Explanation: There is no such common subsequence, so the result is 0.

Constraints:
    * 1 <= text1.length, text2.length <= 1000
    * text1 and text2 consist of only lowercase English characters.
"""


# Algorithm Used: Dynamic Programming, Two-Dimensional, Buttom-Up
# Time Complexity: O(n * m)
# Memory Complexity: O(n * m)
def longestCommonSubsequence(text1: str, text2: str) -> int:
    # Initialize dp grid
    #     - lcs_grid will be the size of the strings plus one to account for the empty string.
    #     - lcs_grid[i][j] will be the length of the longest common subsequence between
    #       the substring starting at index i of text1 and the substring starting at index j of text2.
    # Grid will look something similar to this (text1 = "abcde", text2 = "ace"):
    #         a  b  c  d  e
    #         0  0  0  0  0  0
    #     a   0  0  0  0  0  0
    #     c   0  0  0  0  0  0
    #     e   0  0  0  0  0  0
    #         0  0  0  0  0  0
    lcs_grid = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

    # Iterate through dp grid which will be done by iterating through input strings in reverse order.
    # For each cell in the grid/chacter in the strings, check if the characters match.
    # If they do, update the cell to be 1 + the cell below and to the right.
    # Otherwise, update the cell to be the max of the cell below and the cell to the right.
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            below_subseqs = i + 1
            right_subseqs = j + 1
            if text1[i] == text2[j]:  # MATCH FOUND
                lcs_grid[i][j] = 1 + lcs_grid[below_subseqs][right_subseqs]  # UPDATE
            else:
                # lcs_grid[i][right_subseqs] is the cell to the right
                # lcs_grid[below_subseqs][j] is the cell below
                lcs_grid[i][j] = max(lcs_grid[i][right_subseqs], lcs_grid[below_paths][j])

    # Return the cell at the top left of the grid which will be the length of the longest common subsequence.
    return lcs_grid[0][0]
