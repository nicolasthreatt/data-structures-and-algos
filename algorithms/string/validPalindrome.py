"""
Valid Palindrome
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
    * 1 <= s.length <= 2 * 10^5
    * s consists only of printable ASCII characters.
"""


# Algorithm Used: Iteration
# Time Complexity: O(n)
# Memeory Complexity: O(n)
def isPalindromeI(s: str) -> bool:
    s = "".join(char.lower() for char in s if char.isalnum())

    return s == s[::-1]  # Check if string is same when reversed


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


if __name__ == "__main__":
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("", True),
        ("a", True),
        ("aa", True),
        ("ab", False),
        ("0P", False),
        ("No lemon, no melon", True),
        ("Was it a car or a cat I saw?", True),
        ("12321", True),
        ("1231", False),
        ("!!!", True),
        ("ab@#a", True),
        ("abcba", True),
        ("abccba", True),
        ("abcdba", False),
    ]

    functions = [isPalindromeI, isPalindromeII]
    for func in functions:
        for s, expected in test_cases:
            assert func(s) == expected
