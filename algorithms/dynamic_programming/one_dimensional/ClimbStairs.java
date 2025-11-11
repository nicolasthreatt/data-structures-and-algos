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
package algorithms.dynamic_programming.one_dimensional;

public class ClimbStairs {

    // Algorithm Used: Brute Force
    // Time Complexity: O(n^2)
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
    // Space Complexity: O(2^n)
    private int dfs(int steps_remaining) {
        // Base Case 1: Reached top stair exactly
        if (steps_remaining == 0) {
            return 1;
        }

        // Base Case 2: Over-reached the top stair
        if (steps_remaining < 0) {
            return 0;
        }

        return dfs(steps_remaining - 1) + dfs(steps_remaining - 2);
    }

    // Algorithm Used: Decision Tree, Depth First Search
    // Time Complexity: O(2^n)
    // Space Complexity: O(2^n)
    public int climbStairsII(int n) {
        return dfs(n);
    }

    // Algorithm Used: Dynamic Programming (1-D), Bottom-Up, Fibonacci
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public int climbStairsIII(int n) {
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

            // Update two_steps_Away to represent the enxt lower position
            two_step_moves = tmp;
        }

        // After looping, one_step_moves represents ways to reach the top from the ground.
        return one_step_moves;
    }
}
