"""
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
    * 1 <= s.length <= 2 * 105
    * s consists only of printable ASCII characters.
"""


# Time Complexity: O(n)
# Memeory Complexity: O(n)
def isPalindromeI(s: str) -> bool:
    newStr = ""

    # Iterate through input string and only check for alpha-numeric characters
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    
    # Check if current string is the same when reversed
    return newStr == newStr[::-1]


# Algorithm Used: Two Pointers
# Time Complexity: O(n)
# Memory Complexity: O(1)
def isPalindromeII(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:

        # Check to see if both the left and right pointer are alphanumeric
        while l < r and not alphaNum(s[l]):
            l += 1
        while l < r and not alphaNum(s[r]):
            r -= 1

        # Check to see if the left and right pointer are equal
        if s[l].lower() != s[r].lower():
            return False

        # Increment pointers
        l += 1
        r -= 1

    return True


# Check ascii value to determine if the character is alphanumeric
def alphaNum(c):
    return (
            (ord('A') <= ord(c) <= ord('Z')) or
            (ord('a') <= ord(c) <= ord('z')) or
            (ord('0') <= ord(c) <= ord('9'))
           )
