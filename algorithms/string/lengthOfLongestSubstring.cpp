/*
Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.

Constraints:
    * 0 <= s.length <= 5 * 10^4
    * s consists of English letters, digits, symbols and spaces.
*/

#include <iostream>
#include <set>

using namespace std;

// Algorithm(s) Used: Sliding Window
// Time Complexity: O(n)
// Space Complexity: O(n)
int lengthOfLongestSubstring(string s) {
    if (s.size() <= 1) return s.size();

    set<char> substring = {};
    int longest_substring = INT_MAX;

    int l = 0;
    for (int r = 0; r < s.size(); r++) {
        while (substring.contains(s[r])) {
            substring.erase(s[l]);
            l += 1;
        }
        substring.insert(s[r]);

        int window = s.size();  // r - l + 1
        longest_substring = max(longest_substring, window);
    }

    return longest_substring;
}