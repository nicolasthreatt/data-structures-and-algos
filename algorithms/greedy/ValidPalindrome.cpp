/*
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
*/

#include <cassert>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

class ValidPalindrome {
private:

    // Algorithm(s) Used: Two Pointers
    // Time Complexity: O(n)
    // Space Compexlity: O(1)
    bool isPalindrome(string s, int left, int right) {
        while (left < right) {
            if (s[left] != s[right]) {
                return false;
            }
            left += 1;
            right -= 1;
        }

        return true;
    }

public:

    // Algorithm(s) Used: Greedy, Two Pointers
    // Time Complexity: O(n)
    // Space Compexlity: O(1)
    bool validPalindromeI(string s) {
        int left = 0;
        int right = s.size() - 1;

        while (left < right) {
            // Local Choice - First Mismatch (Allowed)
            if (s[left] != s[right]) {
                // Greedy Choice - Second Mismatch (Not Allowed)
                return (
                    isPalindrome(s, left + 1, right) || isPalindrome(s, left, right - 1)
                );
            }

            // Local Optimal Solution - Update Pointers
            left += 1;
            right -= 1;
        }

        return true;
        
    }
};

int main() {
    ValidPalindrome Solution;

    // (string s, expected)
    vector<tuple<string, bool>> test_cases = {
        {"aba", true},
        {"abca", true},
        {"abc", false},
        {"a", true},
        {"aa", true},
        {"ab", true},
        {"deeee", true},
        {"racecar", true},
        {"radar", true},
        {"abcdef", false},
    };

    vector<bool (ValidPalindrome::*)(string)> funcs = {
        &ValidPalindrome::validPalindromeI,
    };

    for (auto func : funcs) {
        for (auto& tc : test_cases) {
            string s;
            bool expected;
            tie(s, expected) = tc;

            bool result = (Solution.*func)(s);
            assert(result == expected);
        }
    }

    return 0;
}
