"""
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
    * 1 <= s.length <= 1000
    * s consist of only digits and English letters.
"""


# Algorithm Used: Dynamic Programming (1-D), Two Pointers
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def longestPalindrome(s: str) -> str:
    def find_palindrome(l: int, r: int) -> str:
        """
        Find the longest palindrome in a specified window.

        Continue to expand the window until the two characters do not match.
        Note to check if the window is within the bounds of the input string.

        Args:
            s (str): Input string
            l (int): Left index of window
            r (int): Right index of window

        Returns:
            str: Longest palindrome in window
        """
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return s[l + 1 : r]  # Return the palindrome

    # Iterate through the input string
    # Check odd length palindrones - "bab"
    # Check even length palindrones - "bb"
    # After each check update longest palindrome if necessary
    longest_palindrome = ""
    for i in range(len(s)):
        l, r = i, i  # l = r for odd length palindromes - "bab"
        current_palindrome = find_palindrome(l, r)
        if len(current_palindrome) > len(longest_palindrome):
            longest_palindrome = current_palindrome

        l, r = i, i + 1  # l + 1 = r for even length palindromes - "bb"
        current_palindrome = find_palindrome(l, r)
        if len(current_palindrome) > len(longest_palindrome):
            longest_palindrome = current_palindrome

    return longest_palindrome
