"""
https://leetcode.com/problems/palindromic-substrings/

Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:
    * 1 <= s.length <= 1000
    * s consists of lowercase English letters.
"""


# Algorithm Used: Dynamic Programming (1-D), Two Pointers
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def countSubstrings(s: str) -> int:
    total_palindromes = 0

    # Iterate through the input string
    for i in range(len(s)):
        # Count odd length palindrones - "bab"
        total_palindromes += countPalindromes(s, l=i, r=i)

        # Count even length palindrones - "bb"
        total_palindromes += countPalindromes(s, l=i, r=i + 1)

    return total_palindromes


# Algorithm Used: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
def countPalindromes(s, l, r):
    """
    Count the number of palindrones in a specified window

    Args:
        s (str): Input string
        l (int): Left index of window
        r (int): Right index of window

    Returns:
        int: Number of palindromes in window
    """

    num_palindromes = 0

    # Check left and right indexes are inbounds and the two characters match
    # Continue to iterate over window if palindrome is found
    while l >= 0 and r < len(s) and s[l] == s[r]:
        num_palindromes += 1
        l -= 1
        r += 1

    return num_palindromes
