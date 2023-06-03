"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.

In how many distinct ways can you climb to the top?

Example 1:
    Input: n = 2
    Output: 2
    Explanation:
        There are two ways to climb to the top.
            1. 1 step + 1 step
            2. 2 steps

Example 2:
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


# Algorithms Used: Dynamic Programming (1-D), Bottom-Up, Fibonacci
# Time Complexity: O(n)
# Space Complexity: O(n)
def climbStairsI(n: int) -> int:
    # Create two variables to store the number of ways to reach the top and initialize them to 1.
    # Starting from top and work your way down, so matter the value of n, the nth and (n-1)th steps are always one step
    # away from the top.
    #   - one_step_away: Initially starts (n - 1) steps away from the top.
    #   - two_steps_away: Initially starts at the nth step, which is the top step.
    # NOTE: If n = 5, then at the 4th step, we are already one step away from the top.
    one_step_away, two_steps_away = 1, 1

    # Starting the top stair, work your way down to the first stair.
    # At each step, update the number of ways to reach the top from one step away and two steps away.
    # This is done by adding the number of ways to reach the top from one step away and the number of
    # ways to reach the top from two steps away.
    # NOTE: The number of ways to reach the top is the sum of the number of ways to reach the
    # top from one step away and the number of ways to reach the top from two steps away.
    for _ in range(n - 1):
        tmp = one_step_away
        # Add two_steps_away to one_step_away to get the number of ways to reach the top from one step away.
        # This is because after taking one step, we are now two step away from the top.
        # Recall that one_step_away is initially at the (n - 1)th step, so if we take one step, are now at the nth step.
        one_step_away += two_steps_away

        # Update two_steps_away to be the number of ways to reach the top from two steps away.
        # This is now only one step away from the top since we just took one step.
        # Recall that two_steps_away is initially at the top step, so if take only one step,
        # we are now one step away from the top.
        two_steps_away = tmp

    # Return the number of ways to reach the top from one step away.
    # This is because after walking down the stairs, one_step_away will be at the group floor.
    # However, two_steps_away will be one step above from the ground floor.
    return one_step_away


# Algorithms Used: Decision Tree, Depth First Search
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
def climbStairsII(n: int) -> int:
    pass


# Algorithms Used: Brute Force
# Time Complexity:
# Space Complexity:
def climbStairsIII(n: int) -> int:
    pass
