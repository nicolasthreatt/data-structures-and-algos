"""
Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
 
Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation:
        - Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
        - Note that buying on day 2 and selling on day 1 is not allowed
          because you must buy before you sell.

Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation:
        - In this case, no transactions are done and the max profit = 0.
 
Constraints:
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^4
"""

from typing import List


class MaxProfit:

    # Algorithm Used: Sliding Window, Two Pointers
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfitI(self, prices: List[int]) -> int:
        max_profit = 0

        l = 0
        for r in range(1, len(prices)):
            buy = prices[l]
            sell = prices[r]
            if buy < sell:
                profit = sell - buy
                max_profit = max(max_profit, profit)
            else:
                l = r

        return max_profit


    # Algorithm Used: Greedy
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfitII(self, prices: List[int]) -> int:
        if (len(prices) <= 1):
            return 0

        sell = 0
        buy = prices[0]

        for i in range(len(prices)):
            price = prices[i]
            sell = max(sell, price - buy)

            buy = min(buy, price)

        return sell


    # Algorithm Used: Dynammic Programming (1-D)
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfitIII(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        sell = 0
        buy = -prices[0]

        for price in prices[1:]:
            sell = max(sell, price + buy)
            buy = max(buy, -price)

        return sell


if __name__ == "__main__":
    Solution = MaxProfit()

    test_cases = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([1], 0),
        ([2,4], 2),
        ([4,2], 0),
        ([3,3,3], 0),
        ([1,2,3,4,5], 4),
        ([2,1,2,1,0,1,2], 2),
        ([9,1,5,3,7,4,8], 7),
        ([5,2,10,1,8], 8),
        ([6,1,3,2,8,4], 7),
    ]

    for func in [Solution.maxProfitI, Solution.maxProfitII, Solution.maxProfitIII]:
        for prices, expected in test_cases:
            result = func(prices)
            assert result == expected
