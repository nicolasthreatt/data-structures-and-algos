/*
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
*/

#include <cassert>
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

class LongestPalindrome {
public:

    // Algorithm(s) Used: Greedy, Hash Set
    // Time Complexity: O(s)
    // Space Complexity: O(1)
    int longestPalindromeI(string s) {
        unordered_set<char> seen;
        int longest = 0;

        for (char ch : s) {
            if (seen.contains(ch)) {
                longest += 2;  // Greedy - Character Pair Found (Local Optimal)
                seen.erase(ch);
            } else {
                seen.insert(ch);
            }
        }

        // Odd Length Palindrome
        if (seen.size()) {
            longest += 1;
        }

        return longest;
    }
};

int main() {
    LongestPalindrome Solution;

    // (s, expected)
    vector<tuple<string, int>> test_cases = {
        {"abccccdd", 7},
        {"a", 1},
        {"Aa", 1},
        {"aa", 2},
        {"aaBB", 4},
        {"abc", 1},
        {"ccc", 3},
        {"AaBb", 1},
        {"aaabbbb", 7},
    };

    vector<int (LongestPalindrome::*)(string)> funcs = {
        &LongestPalindrome::longestPalindromeI,
    };

    for (auto func : funcs) {
        for (auto& tc : test_cases) {
            string s;
            int expected;
            tie(s, expected) = tc;

            int result = (Solution.*func)(s);
            assert(result == expected);
        }
    }

    return 0;
}
