"""
Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/

Given a string s,
return true if the s can be palindrome after deleting at most one character from it.

Example 1:
    Input: s = "aba"
    Output: true

Example 2:
    Input: s = "abca"
    Output: true
    Explanation: You could delete the character 'c'.

Example 3:
    Input: s = "abc"
    Output: false

Constraints:
    * 1 <= s.length <= 10^5
    * s consists of lowercase English letters.
"""


class ValidPalindrome:

    # Algorithm(s) Used: Two Pointers
    # Time Complexity: O(n)
    # Space Compexlity: O(1)
    def is_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    # Algorithm(s) Used: Greedy, Two Pointers
    # Time Complexity: O(n)
    # Space Compexlity: O(1)
    def validPalindromeI(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:  # Local Choice - First Mismatch (Allowed)
                return (      # Greedy Choice - Second Mismatch (Not Allowed)
                    self.is_palindrome(s, l + 1, r) or
                    self.is_palindrome(s, l, r - 1)
                )

            # Local Optimal Solution - Update Pointers
            l += 1
            r -= 1

        return True


if __name__ == "__main__":
    Solution = ValidPalindrome()

    test_cases = [
        # (s, expected)
        ("aba", True),
        ("abca", True),
        ("abc", False),
        ("a", True),
        ("aa", True),
        ("ab", True),
        ("deeee", True),
        ("racecar", True),
        ("radar", True),
        ("abcdef", False),
    ]

    funcs = [
        Solution.validPalindromeI,
    ]

    for func in funcs:
        for s, expected in test_cases:
            result = func(s)
            assert result == expected
