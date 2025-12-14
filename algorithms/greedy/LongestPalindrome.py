"""
Longest Palindrome
https://leetcode.com/problems/longest-palindrome/

Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:
    Input: s = "abccccdd"
    Output: 7
    Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
    Input: s = "a"
    Output: 1
    Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:
    * 1 <= s.length <= 2000
    * s consists of lowercase and/or uppercase English letters only.
"""

class LongestPalindrome:

    # Algorithm(s) Used: Greedy, Hash Set
    # Time Complexity: O(s)
    # Space Complexity: O(1)
    def longestPalindromeI(self, s: str) -> int:
        seen = set()
        longest = 0

        for ch in s:
            if ch in seen:  # Greedy - Character Pair Found (Local Optimal)
                longest += 2
                seen.remove(ch)
            else:
                seen.add(ch)
        
        if seen: # Odd Length Palindrome
            longest += 1

        return longest  # Global Optimal


if __name__ == "__main__":
    Solution = LongestPalindrome()

    test_cases = [
        # (s, expected)
        ("abccccdd", 7),
        ("a", 1),
        ("Aa", 1),
        ("aa", 2),
        ("aaBB", 4),
        ("abc", 1),
        ("ccc", 3),
        ("AaBb", 1),
        ("aaabbbb", 7),
    ]

    funcs = [
        Solution.longestPalindromeI,
    ]

    for func in funcs:
        for s, expected in test_cases:
            result = func(s)
            assert result == expected
