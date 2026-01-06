/*
Maximum Score After Splitting a String
https://leetcode.com/problems/maximum-score-after-splitting-a-string/

Given a string s of zeros and ones,
return the maximum score after splitting the string into two non-empty substrings.
    - i.e. left substring and right substring.

The score after splitting a string is
    - Number of zeros in the left substring + Number of ones in the right substring

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

#include <cassert>
#include <cstring>
#include <vector>

using namespace std;

class MaxScore {
public:

    // Algorithm(s) Used: Brute Force, Nested Iteration
    // Time Complexity: O(n^2)
    // Space Complexity: O(n)
    int maxScoreI(string s) {
        int max_score = 0;

        for (int i = 1; i < s.size(); ++i) {
            int left_zeroes = 0;
            int right_ones = 0;

            for (int j = 0; j < s.size(); ++j) {
                if (j < i && s[j] == '0') {
                    left_zeroes += 1;  // Greedy Choice: +1 zero is now part of the left side
                }
                else if (j >= i && s[j] == '1') {
                    right_ones += 1;   // Greedy Choice: -1 one moves from right to left
                }

                max_score = max(max_score, left_zeroes + right_ones);
            }
        }
        
        return max_score;
    }

    // Algorithm(s) Used: Greedy, Two-Passes, Prefix Counting
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    int maxScoreII(string s) {
        int max_score = 0;
        int left_zeroes = 0;
        int right_ones = 0;

        // First Pass - Count Total 1's
        // Initially, all '1's are assumed to be on the right side of the split.
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '1') {
                right_ones += 1;
            }
        }

        // Second Pass - Count Total 0's
        // Stop at s.size() - 1 to ensure both left and right substrings are non-empty.
        for (int i = 0; i < s.size() - 1; ++i) {
            if (s[i] == '0') {
                left_zeroes += 1;  // Greedy Choice: +1 zero is now part of the left side
            }
            else if (s[i] == '1') {
                right_ones -= 1;   // Greedy Choice: -1 one moves from right to left
            }

            max_score = max(max_score, left_zeroes + right_ones);  // Local Optimal Solution
        }
        
        return max_score;  // Global Optimal Solution
    }

    // Algorithm(s) Used: Greedy, Two-Passes, Prefix Counting
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    int maxScoreIII(string s) {
        int max_score = 0;
        int curr_score = 0;

        // First Pass - Count Total 1's
        // Initially, all '1's are assumed to be on the right side of the split.
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '1') {
                curr_score += 1;
            }
        }

        // Second Pass - Count Total 0's
        // Stop at s.size() - 1 to ensure both left and right substrings are non-empty.
        for (int i = 0; i < s.size() - 1; ++i) {
            if (s[i] == '0') {
                curr_score += 1;  // Greedy Choice: +1 zero is now part of the left side
            }
            else if (s[i] == '1') {
                curr_score -= 1;  // Greedy Choice: -1 one moves from right to left
            }

            max_score = max(max_score, curr_score);  // Local Optimal Solution
        }
        
        return max_score;  // Global Optimal Solution
    }
};

int main() {
    MaxScore Solution;

    // (s, expected)
    vector<pair<string, int>> test_cases = {
        {"011101", 5},
        {"00111", 5},
        {"1111", 3},
        {"00", 1},
        {"01", 2},
        {"10", 0},
        {"10101", 3},
        {"0000", 3},
        {"1100", 1},
        {"010101", 4},
    };

    vector<int (MaxScore::*)(string)> funcs = {
        &MaxScore::maxScoreI,
        &MaxScore::maxScoreII,
        &MaxScore::maxScoreIII,
    };

    for (auto func : funcs) {
        for (auto& tc : test_cases) {
            string s = tc.first;
            int expected = tc.second;

            int result = (Solution.*func)(s);
            assert(result == expected);
        }
    }

    return 0;
}
