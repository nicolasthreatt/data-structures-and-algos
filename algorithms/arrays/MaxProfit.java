/*
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
*/
package algorithms.arrays;

public class MaxProfit {

    // Algorithm(s) Used: Kadane, Two Pointers
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public int maxProfitI(int[] prices) {
        if (prices.length <= 1) return 0;

        int max_profit = 0;

        int buy = 0;
        for (int sell = 1; sell < prices.length; sell++) {
            int profit = prices[sell] - prices[buy];
            if (profit < 0) buy = sell;
            else max_profit = Math.max(max_profit, profit);
        }

        return max_profit;
    }

    // Algorithm(s) Used: Greedy
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public int maxProfitII(int[] prices) {
        if (prices.length <= 1) return 0;

        int sell = 0;
        int buy = prices[0];

        for (int i = 1; i < prices.length; i++) {
            int price = prices[i];

            sell = Math.max(sell, price - buy);
            buy = Math.min(buy, price);
        }

        return sell;
    }

    // Algorithm(s) Used: Dynammic Programming (1-D)
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public int maxProfitIII(int[] prices) {
        if (prices.length <= 1) return 0;

        int sell = 0;
        int buy = -prices[0];

        for (int i = 1; i < prices.length; i += 1) {
            int price = prices[1];

            int profit = price + buy;
            sell = Math.max(sell, profit);
            buy = Math.max(buy, -price);
        }

        return sell;
    }   
}
