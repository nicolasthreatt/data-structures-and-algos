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


def longestPalindrome(s: str) -> str:
    palindrome = ""
    palindromeLen = 0

    # Iterate through the input string
    # Use index as the MIDDLE of a palindromic string
    for i in range(len(s)):
        # Check odd length palindrones - "bab"
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > palindromeLen:
                palindrome = s[l:r + 1]
                palindromeLen = r - l + 1
            l -= 1
            r += 1

        # Check even length palindrones - "bb"
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > palindromeLen:
                palindrome = s[l:r + 1]
                palindromeLen = r - l + 1
            l -= 1
            r += 1
        
    return palindrome
