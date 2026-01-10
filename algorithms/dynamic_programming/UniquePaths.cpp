/*
Unique Paths
https://leetcode.com/problems/unique-paths/

There is a robot on an m x n grid.

The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths
that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
    Input: m = 3, n = 7
    Output: 28

Example 2:
    Input: m = 3, n = 2
    Output: 3
    Explanation:
        From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
            1. Right -> Down -> Down
            2. Down -> Down -> Right
            3. Down -> Right -> Down

Constraints:
    * 1 <= m, n <= 100
*/

#include <cassert>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class UniquePaths {

private:
    int ROWS = 0;
    int COLS = 0;
    unordered_map<string, int> memo = {};

    // Algorithm(s) Used: Depth First Search, Recurision
    // Time Complexity: O(ROWS * COLS)
    // Space Complexity: O(i * j)
    int dfs(int i, int j) {
        // Base Case: Out of Bound
        if (i >= ROWS || j >= COLS) {
            return 0;
        }

        // Base Case: End of Valid Path
        if (i == ROWS - 1 && j == COLS - 1) {
            return 1;
        }

        string key = to_string(i) + "," + to_string(j);

        // Base Case: Position Already Visited
        if (memo.contains(key)) {
            return memo[key];
        }

        int right = dfs(i, j + 1);
        int down = dfs(i + 1, j);

        memo[key] = down + right;
        return memo[key];
    }

public:

    // Algorithm(s) Used: Dynammic Programming, Top Down, Memoization, Depth First Search
    // Time Complexity: O(ROWS * COLS)
    // Space Complexity: O(m * n)
    int uniquePathsI(int m, int n) {
        ROWS = m;
        COLS = n;

        memo.clear();
        return dfs(0, 0);
    }

    // Algorithm(s) Used: Dynamic Programming (2-D), Buttom-Up, Tabulation
    // Time Complexity: O(m * n)
    // Space Complexity: O(m * n)
    int uniquePathsII(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, 0));

        // Base Case: Only 1 Valid Path From Last Row
        for (int i = 0; i < m; ++i) {
            dp[i][0] = 1;
        }

        // Base Case: Only 1 Valid Path From Last Row
        for (int j = 0; j < n; ++j) {
            dp[0][j] = 1;
        }

        // Traverse each ROW, i, from TOP to BOTTOM (Exclude Last Row)
        // Traver each COLUMN, j, from LEFT to RIGHT (Exclude Last Col)
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                int top = dp[i][j - 1];
                int left = dp[i - 1][j];
                dp[i][j] = top + left;
            }
        }

        return dp[m - 1][n - 1];
    }

    // Algorithm(s) Used: Dynamic Programming (1-D), Buttom-Up, Tabulation
    // Time Complexity: O(m * n)
    // Space Complexity: O(n)
    int uniquePathsIII(int m, int n) {
        vector<int> dp(n, 1);  // dp[j] = # of paths to reach column j in the current row

        // Start from the BOTTOM row
        // Traverse each ROW, i, from TOP to BOTTOM (Exclude BOTTOM Row)
        // Traver each COLUMN, j, from LEFT to RIGHT (Exclude LAST Column)
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                int top = dp[j];
                int left = dp[j - 1];
                dp[j] = top + left;
            }
        }

        return dp[n - 1];
    }
};

int main() {
    UniquePaths Solution;

    vector<pair<pair<int, int>, int>> testCases = {
        {{3, 7}, 28},
        {{3, 2}, 3},
        {{1, 1}, 1},
        {{1, 5}, 1},
        {{5, 1}, 1},
        {{2, 2}, 2},
        {{2, 3}, 3},
        {{3, 3}, 6},
        {{3, 4}, 10},
        {{4, 4}, 20},
        {{5, 5}, 70},
        {{10, 10}, 48620}
    };

    vector<int (UniquePaths::*)(int, int)> funcs = {
        &UniquePaths::uniquePathsI,
        &UniquePaths::uniquePathsII,
        &UniquePaths::uniquePathsIII,
    };

    for (auto func : funcs) {
        for (auto& test : testCases) {
            int m = test.first.first;
            int n = test.first.second;
            int expected = test.second;

            int result = (Solution.*func)(m, n);
            assert(result == expected);
        }
    }

    return 0;
}
