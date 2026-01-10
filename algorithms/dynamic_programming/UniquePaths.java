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

package algorithms.dynamic_programming;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class UniquePaths {

    private int ROWS = 0;
    private int COLS = 0;
    private Map<String, Integer> memo = new HashMap<>();

    // Algorithm(s) Used: Depth First Search, Recurision
    // Time Complexity: O(ROWS * COLS)
    // Space Complexity: O(i * j)
    private int dfs(int i, int j) {
        // Base Case - Out of Bounds
        if (i >= this.ROWS || j >= this.COLS) {
            return 0;
        }

        // Base Case - End of Valid Path
        if (i == this.ROWS - 1 && j == this.COLS - 1) {
            return 1;
        }

        String key = i + "," + j;

        // Base Case - Position Already Visited
        if (this.memo.containsKey(key)) {
            return this.memo.get(key);
        }

        int right = dfs(i, j + 1);
        int down = dfs(i + 1, j);

        this.memo.put(key, down + right);
        return this.memo.get(key);
    }

    // Algorithm(s) Used: Dynammic Programming, Top Down, Memoization, Depth First Search
    // Time Complexity: O(m * n)
    // Space Complexity: O(m * n)
    public int uniquePathsI(int m, int n) {
        this.ROWS = m;
        this.COLS = n;

        return dfs(0, 0);
    }

    // Algorithm(s) Used: Dynamic Programming (2-D), Buttom-Up, Tabulation
    // Time Complexity: O(m * n)
    // Space Complexity: O(m * n)
    public int uniquePathsII(int m, int n) {
        int[][] dp = new int[m][n];
        
        // Base Case - Only 1 Valid Path From Last Row
        for (int i = 0; i < m; ++i) {
            dp[i][0] = 1;
        }

        // Base Case - Only 1 Valid Path From Last Row
        for (int j = 0; j < n; ++j) {
            dp[0][j] = 1;
        }

        // Traverse each ROW, i, from TOP to BOTTOM (Exclude Last Row)
        // Traver each COLUMN, j, from LEFT to RIGHT (Exclude Last Col)
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                int left = dp[i - 1][j];
                int top = dp[i][j - 1];
                dp[i][j] = top + left;
            }
        }

        return dp[m - 1][n - 1];
    }

    // Algorithm(s) Used: Dynamic Programming (1-D), Buttom-Up, Tabulation
    // Time Complexity: O(m * n)
    // Space Complexity: O(n)
    public int uniquePathsIII(int m, int n) {
        int[] dp = new int[n];    // dp[j] = # of unique paths to reach column j in the current row
        Arrays.fill(dp, 1);  // Start from the BOTTOM row

        // Traverse each ROW, i, from TOP to BOTTOM (Exclude BOTTOM Row)
        // Traver each COLUMN, j, from LEFT to RIGHT (Exclude BOTTOM Col)
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                int left = dp[j - 1];
                int top = dp[j];
                dp[j] = top + left;
            }
        }

        return dp[n - 1];  // Bottom-Right Cell (m-1, n-1)
    }
}
