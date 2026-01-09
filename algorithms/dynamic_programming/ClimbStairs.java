/*
Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.

In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
Explanation:
    There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps

Input: n = 3
Output: 3
Explanation:
    There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step

Constraints:
    * 1 <= n <= 45
*/

package algorithms.dynamic_programming;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ClimbStairs {

    private Map<Integer, Integer> memo = new HashMap<>();

    // Algorithm Used: Brute Force
    // Time Complexity: O(2^n)
    // Space Complexity: O(n)
    public int climbStairsI(int n) {
        // Base Case: Only 1 way to climb 0 or 1 stairs (either take 1 step, or do nothing)
        if (n <= 1) {
            return 1;
        }

        // Recursively calculate number of 1-step moves and 2-step moves
        return climbStairsI(n - 1) + climbStairsI(n - 2);

    }

    // Algorithm Used: Depth First Seach
    // Time Complexity: O(2^n)
    // Space Complexity: O(n)
    private int dfs(int n) {
        // Base Case 1: Reached top stair exactly
        if (n == 0) {
            return 1;
        }

        // Base Case 2: Over-reached the top stair
        if (n < 0) {
            return 0;
        }

        return dfs(n - 1) + dfs(n - 2);
    }

    // Algorithm Used: Decision Tree, Depth First Search (DFS), Recursion
    // Time Complexity: O(2^n)
    // Space Complexity: O(n)
    public int climbStairsII(int n) {
        return dfs(n);
    }

    // Algorithm Used: Dynammic Programming (1-D), Top-Down, Recursion, Memoization
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public int climbStairsIII(int n) {
        if (n <= 1) {
            return 1;
        }

        if (memo.containsKey(n)) {
            return memo.get(n);
        }

        memo.put(n, climbStairsIII(n - 1) + climbStairsIII(n - 2));
        return memo.get(n);
    }

    // Algorithm Used: Dynammic Programming, Bottom-Up, Tabulation
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public int climbStairsIV(int n) {
        if (n <= 1) {
            return 1;
        }

        List<Integer> dp = new ArrayList<>();
        dp.add(1);  // one_step_moves
        dp.add(1);  // two_step_moves

        for (int i = 1; i < n; i += 1) {
            int one_step_moves = dp.get(i - 1);
            int two_step_moves = dp.get(i);
            dp.add(one_step_moves + two_step_moves);
        }

        return dp.get(n);
    }

    // Algorithm Used: Dynamic Programming (1-D), Bottom-Up, Fibonacci
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public int climbStairsV(int n) {
        // Base Case: Only 1 way to climb 0 or 1 stairs (either take 1 step, or do nothing)
        if (n <= 1) {
            return 1;
        }

        // one_step_moves = ways to reach the top from the ONE step below
        // two_step_moves = ways to reach the top from the TWO steps below
        // NOTE: two_step_moves will always be less than or equal to one_step_moves (for n > 2)
        int one_step_moves = 1, two_step_moves = 1;

        // Iterate from the SECOND-TO-LAST step up until the bottom
        for (int i = 0; i < n - 1; i++) {
            int tmp = one_step_moves;

            // If one step below, then can move either 1 or 2 steps up
            one_step_moves = one_step_moves + two_step_moves;

            // Update two_step_moves to represent the next lower position
            two_step_moves = tmp;
        }

        // After looping, one_step_moves represents ways to reach the top from the ground.
        return one_step_moves;
    }
}
