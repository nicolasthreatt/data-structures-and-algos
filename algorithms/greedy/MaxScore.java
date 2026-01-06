/*
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
*/

package algorithms.greedy;

public class MaxScore {

    // Algorithm(s) Used: Brute Force, Nested Iteration
    // Time Complexity: O(n^2)
    // Space Complexity: O(1)
    public int maxScoreI(String s) {
        int max_score = 0;
        
        for (int i = 1; i < s.length(); ++i) {
            int left_zeros = 0;
            int right_ones = 0;

            for (int j = 0; j < s.length(); ++j) {
                if (j <= i && s.charAt(j) == '0') {
                    left_zeros += 1;
                }
                else if (j > i && s.charAt(j) == '1') {
                    right_ones += 1;
                }

                max_score = Math.max(max_score, left_zeros + right_ones);
            }
        }

        return max_score;
    }

    // Algorithm(s) Used: Greedy, Prefix Sum
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public int maxScoreII(String s) {
        int max_score = 0;
        int left_zeros = 0;
        int right_ones = 0;

        // First Pass - Count Total 1's
        // Initially, all '1's are assumed to be on the right side of the split.
        for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) == '1') {
                right_ones += 1;
            }
        }

        // Second Pass - Count Total 0's
        // Stop at s.size() - 1 to ensure both left and right substrings are non-empty.
        for (int i = 0; i < s.length() - 1; ++i) {
            if (s.charAt(i) == '0') {
                left_zeros += 1;  // Greedy Choice: +1 zero is now part of the left side
            }
            else {
                right_ones -= 1;  // Greedy Choice: -1 one moves from right to left
            }

            max_score = Math.max(max_score, left_zeros + right_ones);  // Local Optimal Solution
        }

        return max_score;  // Global Optimal Solution
    }

    public int maxScoreIII(String s) {
        int max_score = 0;
        int curr_score = 0;

        // First Pass - Prefix Count Total 1's
        // Initially, all '1's are assumed to be on the right side of the split.
        for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) == '1') {
                curr_score += 1;
            }
        }

        // Second Pass - Count Total 0's
        // Stop at s.size() - 1 to ensure both left and right substrings are non-empty.
        for (int i = 0; i < s.length() - 1; ++i) {
            if (s.charAt(i) == '0') {
                curr_score += 1;  // Greedy Choice: +1 zero is now part of the left side
            }
            else {
                curr_score -= 1;  // Greedy Choice: -1 one moves from right to left
            }

            max_score = Math.max(max_score, curr_score);  // Local Optimal Solution
        }

        return max_score;  // Global Optimal Solution
    }
}
