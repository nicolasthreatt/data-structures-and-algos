/*
Climbing Stairs
https://leetcode.com/problems/climbing-stairs

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

#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

// Algorithms Used: Brute Force, Decision Tree, Depth First Search, Recursion
// Time Complexity: O(2^n)
// Space Complexity: O(n)
int climbStairsI(int n) {
    // Base Case: Only 1 way to climb 0 or 1 stair(s)
    if (n <= 1) {
        return 1;
    }

    // Recursively calculate number of 1-step moves and 2-step moves
    return climbStairsI(n - 1) + climbStairsI(n - 2);
}

// Algorithms Used: Brute Force, Decision Tree, Depth First Search, Recursion
// Time Complexity: O(2^n)
// Space Complexity: O(n)
int climbStairsII(int n) {
    // Base Case 1: Reached top stair exactly
    if (n == 0) {
        return 1;
    }

    // Base Case 2: Over-reached the top stair
    if (n < 0) {
        return 0;
    }

    return climbStairsII(n - 1) + climbStairsII(n - 2);
}

// Algorithms Used: Dynamic Programming (1-D), Bottom-Up, Fibonacci
// Time Complexity: O(n)
// Space Complexity: O(1)
int climbStairsIII(int n) {
    // Base Case: Only 1 way to climb 0 or 1 stair(s)
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

        // If one step below, then can move eitehr 1 or 2 steps up
        one_step_moves += two_step_moves;

        // Update two_step_moves to represent the next lower position
        two_step_moves = tmp;
    }

    return one_step_moves;
}

int main() {
    vector<pair<int, int>> testCases = {
        {1, 1},
        {2, 2},
        {3, 3},
        {4, 5},
        {5, 8},
        {6, 13},
        {10, 89},
        {20, 10946},
        {30, 1346269},
        {45, 1836311903}
    };

    for (auto& [n, expected] : testCases) {
        if (n <= 10) {
            assert(climbStairsI(n) == expected);
        }
        assert(climbStairsII(n) == expected);
        assert(climbStairsIII(n) == expected);
    }

    return 0;
}
