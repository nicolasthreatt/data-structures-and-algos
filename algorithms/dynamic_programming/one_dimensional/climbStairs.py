"""
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
"""


# Algorithms Used: Brute Force
# Time Complexity: O(2^n)
# Space Complexity: O(n)
def climbStairsI(n: int) -> int:
    # Base Case: Only 1 way to climb 1 or 0 stairs (either take 1 step, or do nothing)
    if n <= 1:
        return 1

    # Recursively calculate number of 1-step moves and 2-step moves
    return climbStairsI(n - 1) + climbStairsI(n - 2)


# Algorithms Used: Decision Tree, Depth First Search
# Time Complexity: O(2^n)
# Space Complexity: O(n)
def climbStairsII(n: int) -> int:
    def dfs(steps_remaining: int) -> int:
        # Base Case 1: Reached the top exactly
        if steps_remaining == 0:
            return 1

        # Base Case 2: Over-reached the top
        if steps_remaining < 0:
            return 0
        
        # Try taking 1 step and 2 steps recursively
        return dfs(steps_remaining - 1) + dfs(steps_remaining -2)

    return dfs(n)


# Algorithms Used: Dynamic Programming (1-D), Bottom-Up, Fibonacci
# Time Complexity: O(n)
# Space Complexity: O(1)
def climbStairsIII(n: int) -> int:
    # Base case: Only 1 way to climb 0 or 1 stair
    if n <= 1:
        return 1

    one_step_away, two_steps_away = 1, 1

    # Starting from the 2nd-to-last stair, build up the number of ways to climb to the top
    for _ in range(n - 1):
        one_step_away, two_steps_away = one_step_away + two_steps_away, one_step_away

    # Final result is the number of ways from the ground (n steps away)
    return one_step_away


if __name__ == "__main__":
    test_cases = [
        (1, 1),  # Only one way: [1]
        (2, 2),  # [1+1], [2]
        (3, 3),  # [1+1+1], [1+2], [2+1]
        (4, 5),  # [1+1+1+1], [1+2+1], [2+1+1], [2+2], [1+1+2]
        (5, 8),  # Fibonacci-like growth
    ]

    for func in [climbStairsI, climbStairsII, climbStairsIII]:
        for n, expected in test_cases:
            result = func(n)
            assert result == expected
