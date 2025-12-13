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

#include <cassert>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct hash_pair {
    template <class T1, class T2>
    std::size_t operator() (const std::pair<T1, T2> &v) const
    {
        return std::hash<T1>()(v.first) ^ (std::hash<T2>()(v.second) << 1);
    }
};

class IsSubsequence {
private:
    int ROWS = 0;
    int COLS = 0;
    string S = "";
    string T = "";
    unordered_map<pair<int, int>, bool, hash_pair> memo;

    bool dfs(int i, int j) {
        if (i == ROWS) {
            return true;
        }

        if (j >= COLS) {
            return false;
        }

        pair<int, int> key = {i, j};
        if (memo.contains(key)) {
            return memo[key];
        }

        if (S[i] == T[j]) {
            if (dfs(i + 1, j + 1)) {
                memo[key] = true;
                return true;
            }
        }

        memo[key] = dfs(i, j + 1);
        return memo[key];
    }

public:
    // Algorithm(s) Used: Greedy
    // Time Complexity: O(t)
    // Space Complexity: O(1)
    bool isSubsequenceI(string s, string t) {
        int i = 0;
        int j = 0;

        while (i < s.size() && j < t.size()) {
            if (s[i] == t[j]) { i++; }  // Local Optimal
            j++;
        }

        bool is_subseqence = i == s.size();  // Global Optimal
        return is_subseqence;
    }

    // Algorithm(s) Used: Dynammic Programming (2-D), DFS, Top-Down, Memoiozation
    // Time Complexity: O(s * t)
    // Space Complexity: O(s + t)
    bool isSubsequenceII(string s, string t) {
        ROWS = s.length();
        COLS = t.length();

        S = s;
        T = t;

        if (ROWS == 0) return true;    // empty string is always subsequence
        if (COLS == 0) return false;   // non-empty s can't be subsequence of empty t

        memo.clear();
        return dfs(0, 0);
    }

    // Algorithm(s) Used: Dynammic Programming (2-D)
    // Time Complexity: O(s * t)
    // Space Complexity: O(s * t)
    bool isSubsequenceIII(string s, string t) {
        size_t r = s.size();
        size_t c = t.size();
        vector<vector<int>> dp(r + 1, vector<int>(c + 1, 0));

        for (int i = 1; i < r + 1; i++) {
            for (int j = 1; j < c + 1; j++) {
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = dp[i][j - 1];
                }
            }
        }

        bool is_subseqence = dp[r][c] == s.size();
        return is_subseqence;
    }
};

int main() {
    IsSubsequence Solution;

    // (s, t, expected)
    vector<tuple<string, string, bool>> test_cases = {
        {"abc", "ahbgdc", true},
        {"axc", "ahbgdc", false},
        {"",    "abc",    true},
        {"abc", "",       false},
        {"a",   "a",      true},
        {"b",   "a",      false},
        {"aaaa", "aaaaaaaaaa", true},
        {"abc", "abc", true},
        {"abc", "acb", false},
        {"ace", "abcde", true},
    };

    vector<bool(IsSubsequence::*)(string, string)> funcs = {
        &IsSubsequence::isSubsequenceI,
        &IsSubsequence::isSubsequenceII,
        &IsSubsequence::isSubsequenceIII,
    };

    for (size_t f = 0; f < funcs.size(); f++) {
        auto func = funcs[f];

        for (auto& tc : test_cases) {
            string s, t;
            bool expected;
            tie(s, t, expected) = tc;

            bool result = (Solution.*func)(s, t);
            assert(result == expected);
        }
    }

    return 0;
}
