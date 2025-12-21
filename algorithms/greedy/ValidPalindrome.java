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

package algorithms.greedy;

public class ValidPalindrome {

    // Algorithm(s) Used: Two Pointers
    // Time Complexity: O(n)
    // Space Compexlity: O(1)
    private boolean isPalindrome(String s, int left , int right) {
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left += 1;
            right -= 1;
        }
        
        return true;
    }

    // Algorithm(s) Used: Greedy, Two Pointers
    // Time Complexity: O(n)
    // Space Compexlity: O(1)
    public boolean validPalindromeI(String s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            // Local Choice - First Mismatch (Allowed)
            if (s.charAt(left) != s.charAt(right)) {
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
}
