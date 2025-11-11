"""
https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

Example 2:
    Input: coins = [2], amount = 3
    Output: -1

Example 3:
    Input: coins = [1], amount = 0
    Output: 0

Constraints:
    * 1 <= coins.length <= 12
    * 1 <= coins[i] <= 231 - 1
    * 0 <= amount <= 104
"""

from typing import List


# Algorithm Used: Dynamic Programming, One-Dimensional, Buttom-Up
# Time Complexity: O(n * m), where n is the total amount of money and m is the number of coins
# Space Complexity: O(n), where n is the total amount of money
def coinChange(coins: List[int], amount: int) -> int:
    # Initialize a default value to represent the minimum number of coins needed to produce the total amount of money.
    DEFAULT_VALUE = float("inf")

    # Initialize an array the size of the total amount of money.
    # The value at each index will represent the minimum number of coins needed to produce that amount of money.
    # Float infinity is used as a placeholder for the minimum number of coins needed to produce that amount of money,
    # which ensures that the minimum number of coins needed to produce that amount of money will be updated.
    # NOTE: dp[i] represents the minimum number of coins needed to produce the amount of money i.
    dp = [DEFAULT_VALUE] * len(amount + 1)  # zero-based

    # It takes 0 coins to produce the total amount of money to be 0 (BASE CASE)
    dp[0] = 0

    # Iterate the total amount of money from 1 to the total amount of money and
    # determine the minimum number of coins needed to produce that amount of money.
    # NOTE: range(1, amount + 1) is used instead of range(amount + 1) to account for the base case.
    #       dp[amount] will be used to determine the minimum number of coins needed to produce the total amount of money.
    for current_amount in range(1, amount + 1):
        # Iterate through each coin to determine the minimum number of coins needed
        # to produce that amount of money.
        for current_coin in coins:
            # If the current coin is less than or equal to the current amount of money,
            # then determine the minimum number of coins needed to produce that amount of money.
            #    - dp[current_amount]: minimum number of coins needed to produce that amount of money.
            #    - 1 + dp[current_amount - current_coin]: minimum number of coins needed to produce the
            #      remaining amount of money after subtracting the current coin from the current amount of money.
            #      Add 1 to minimum number of coins needed to produce remaining amount of money to account for current coin.
            # NOTE: if current_coint = 4 and current_amount = 5, then dp[5] = min(dp[5], 1 + dp[5 - 4])
            if current_amount - current_coin >= 0:
                dp[current_amount] = min(dp[current_amount], 1 + dp[current_amount - current_coin])

    # Return the minimum number of coins needed to produce the total amount of money.
    # If the minimum number of coins needed to produce the total amount of money is infinity,
    # then return -1 since the total amount of money cannot be produced.
    return dp[amount] if dp[amount] != DEFAULT_VALUE else -1
