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

package algorithms.string;

import java.util.HashSet;
import java.util.Set;

public class LengthOfLongestSubstring {

    // Algorithm(s) Used: Sliding Window
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public int lengthOfLongestSubstringI(String s) {
        if (s.length() <= 1) return s.length();

        Set<Character> substring = new HashSet<>();
        int longestSubstring = 0;

        int l = 0;
        for (int r = 0; r < s.length(); r++) {
            while (substring.contains(s.charAt(r))) {
                substring.remove(s.charAt(l));
                l += 1;
            }
            substring.add(s.charAt(r));
            longestSubstring = Math.max(longestSubstring, substring.size());
        }

        return longestSubstring;
    }
}
