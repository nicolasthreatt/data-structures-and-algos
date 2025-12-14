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

package algorithms.greedy;

import java.util.HashSet;
import java.util.Set;

public class LongestPalindrome {

    // Algorithm(s) Used: Greedy, Hash Set
    // Time Complexity: O(s)
    // Space Complexity: O(1)
    public int longestPalindromeI(String s) {
        Set<Character> seen = new HashSet<>();
        int longest = 0;

        for (Character ch : s.toCharArray()) {
            if (seen.contains(ch)) {
                longest += 2;  // Greedy - Character Pair Found (Local Optimal)
                seen.remove(ch);
            } else {
                seen.add(ch);
            }
        }

        // Odd Length Palindrome
        if (seen.size() > 0) {
            longest += 1;
        }

        return longest;
    }
}
