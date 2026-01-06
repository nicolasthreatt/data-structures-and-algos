"""
Maximum Score After Splitting a String
https://leetcode.com/problems/maximum-score-after-splitting-a-string/

Given a string s of zeros and ones,
return the maximum score after splitting the string into two non-empty substrings.
    - i.e. left substring and right substring.

The score after splitting a string is
    - Number of zeros in the left substring + Number of ones in the right substring.

Example 1:
    Input: s = "011101"
    Output: 5 
    Explanation: 
        - All possible ways of splitting s into two non-empty substrings are:
        - left = "0" and right = "11101", score = 1 + 4 = 5 
        - left = "01" and right = "1101", score = 1 + 3 = 4 
        - left = "011" and right = "101", score = 1 + 2 = 3 
        - left = "0111" and right = "01", score = 1 + 1 = 2 
        - left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:
    Input: s = "00111"
    Output: 5
    Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Example 3:
    Input: s = "1111"
    Output: 3

Constraints:
    * 2 <= s.length <= 500
    * The string s consists of characters '0' and '1' only.
"""

class MaxScore:

    # Algorithm Used: Brute Force, Iteration
    # Time Complexity: O(n^2)
    # Space Compexity: O(n)
    def maxScoreI(self, s: str) -> int:
        score = 0

        for i in range(1, len(s)):
            left_zeros = sum([1 for char in s[:i] if char == "0"])
            right_ones = sum([1 for char in s[i:] if char == "1"])
            score = max(score, left_zeros + right_ones)

        return score

    # Algorithm Used: Greedy, Two-Passes, Prefix Counting
    # Time Complexity: O(n)
    # Space Compexity: O(1)
    def maxScoreII(self, s: str) -> int:
        score = 0

        left_zeros = 0
        right_ones = s.count("1")  # Prefix Count (First Pass)

        for i in range(1, len(s)):
            if s[i] == "0":
                left_zeros += 1  # Greedy Choice: +1 zero is now part of the left side
            else:
                right_ones -= 1  # Greedy Choice: -1 one moves from right to left

            score = max(score, left_zeros + right_ones)  # Local Optimal Solution

        return score  # Global Optimal Solution

    # Algorithm Used: Greedy, Two-Passes, Prefix Counting
    # Time Complexity: O(n)
    # Space Compexity: O(1)
    def maxScoreIII(self, s: str) -> int:
        max_score = 0
        curr_score = s.count("1")  # Prefix Count (First Pass)

        for i in range(1, len(s)):
            if s[i] == "0":
                curr_score += 1  # Greedy Choice: +1 zero is now part of the left side
            else:
                curr_score -= 1  # Greedy Choice: -1 one moves from right to left
            
            max_score = max(max_score, curr_score)  # Local Optimal Solution
        
        return max_score  # Global Optimal Solution


if __name__ == "__main__":
    Solution = MaxScore()

    # (s, expected)
    test_cases = [
        ("011101", 5),
        ("00111", 5),
        ("1111", 3),
        ("00", 1),
        ("01", 2),
        ("10", 0),
        ("10101", 3),
        ("0000", 3),
        ("1100", 1),
        ("010101", 4),
    ]

    funcs = [
        Solution.maxScoreI,
        Solution.maxScoreII,
        Solution.maxScoreIII,
    ]

    for func in funcs:
        for s, expected in test_cases:
            result = func(s)
            assert result == expected
