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

def countSubstrings(s: str) -> int:
    palindromeCount = 0

    # Iterate through the input string
    # Use index as the MIDDLE of a palindromic string
    for i in range(len(s)):
        # Count odd length palindrones - "bab"
        palindromeCount += countPalindromes(s, i, i)

        # Count even length palindrones - "bb"
        palindromeCount += countPalindromes(s, i, i + 1)
        
    return palindromeCount


def countPalindromes(s, l, r):
    """
    Count the number of palindrones in a specified window
    """

    palindromeCount = 0

    # Check left and right indexes are inbounds and the two characters match
    # Continue to iterate over window if palindrome is found
    while l >= 0 and r < len(s) and s[l] == s[r]:
        palindromeCount += 1
        l -= 1
        r += 1

    return palindromeCount
