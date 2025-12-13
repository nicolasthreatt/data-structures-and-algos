/*
Is Subsequence
https://leetcode.com/problems/is-subsequence/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters.
    - i.e., "ace" is a subsequence of "abcde" while "aec" is not)

Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true

Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false

Constraints:
    * 0 <= s.length <= 100
    * 0 <= t.length <= 10^4
    * s and t consist only of lowercase English letters.

Follow up:
    * Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109,
      and you want to check one by one to see if t has its subsequence.
      In this scenario, how would you change your code?
*/
package algorithms.dynamic_programming.two_dimensional;

import java.util.HashMap;
import java.util.Map;

public class IsSubsequence {

    Map<String, Boolean> MEMO = new HashMap<>();

    Integer ROWS = 0;
    Integer COLS = 0;

    String S = "";
    String T = "";

    // Algorithm(s) Used: Greedy
    // Time Complexity: O(t)
    // Space Complexity: O(1)
    public boolean isSubsequenceI(String s, String t) {
        int i = 0, j = 0;

        while (i < s.length() && j < t.length()) {
            if (s.charAt(i) == t.charAt(i)) { ++i; }  // Local Optimal
            ++j;
        }

        boolean is_sequence = i == s.length();  // Global Optimal
        return is_sequence;
    }

    // Helper Function to Perform Depth First Search (DFS)
    private boolean dfs(Integer i, Integer j) { 
        // Base Case: Found Subsequence
        if (i == this.ROWS) {
            return true;
        }

        // Base Case: Invalid Subsequence
        if (j >= this.COLS) {
            return false;
        }

        // Create Key to Acccess Memo
        String key = i + "," + j;

        // Base Case: Already Compared Characters
        if (this.MEMO.containsKey(key)) {
            return this.MEMO.get(key);
        }

        // Match Found
        if (this.S.charAt(i) == this.T.charAt(j)) {
            if (dfs(i + 1, j + 1)) {
                this.MEMO.put(key, true);
                return true;
            }
        }

        this.MEMO.put(key, dfs(i, j + 1));
        return this.MEMO.get(key);
    }

    // Algorithm(s) Used: Dynammic Programming (2-D), Depth First Search, Top-Down, Memoization
    // Time Complexity: O(s * t)
    // Space Complexity: O(s + t)
    public boolean isSubsequenceII(String s, String t) {
        this.S  = s;
        this.T = t;

        this.ROWS = s.length();
        this.COLS = t.length();

        return dfs(0, 0);
    }

    // Algorithm(s) Used: Dynammic Programming (2-D), Buttom-Up
    // Time Complexity: O(s * t)
    // Space Complexity: O(s * t)
    public boolean isSubsequenceIII(String s, String t) {
        int r = s.length();
        int c = t.length();
        int[][] dp = new int[r + 1][c + 1];

        for (int i = 1; i < r + 1; ++i) {
            for (int j = 1; j < c + 1; ++j) {
                if (s.charAt(i - 1) == t.charAt(j - 1)) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = dp[i][j - 1];
                }
            }
        }

        return dp[r][c] == s.length();
    }
}
