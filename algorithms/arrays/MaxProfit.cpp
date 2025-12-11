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

#include <iostream>
#include <cassert>
#include <vector>

using namespace std;

class MaxProfit {

public:

    // Algorithm(s) Used: Sliding Window, Two Pointers
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    int maxProfitI(vector<int>& prices) {
        if (prices.size() <= 1) return 0;

        int maxProfit = 0;

        int buy = 0;
        for (int sell = 1; sell < prices.size(); sell++) {
            int profit = prices[sell] - prices[buy];
            if (profit < 0) {
                buy = sell;
            } else {
                maxProfit = max(maxProfit, profit);
            }
        }

        return maxProfit;
    }

    // Algorithm(s) Used: Greedy
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    int maxProfitII(vector<int>& prices) {
        if (prices.size() <= 1) return 0;

        int sell = 0;
        int buy = prices[0];

        for (int i = 0; i < prices.size(); i++) {
            int price = prices[i];

            sell = max(sell, price - buy);
            buy = min(buy, price);
        }

        return sell;
    }

    // Algorithm(s) Used: Dynammic Programming (1-D)
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    int maxProfitIII(vector<int>& prices) {
        if (prices.size() <= 1) return 0;

        int sell = 0;  // max_profit
        int buy = -prices[0];

        for (int i = 1; i < prices.size(); i += 1) {
            int price = prices[i];
            sell = max(sell, price + buy);
            buy = max(buy, -price);
        }

        return sell;
    }
};

int main() {
    // Struct to hold test case data
    struct TestCase {
        vector<int> prices;
        int expected;
    };

    vector<TestCase> testCases = {
        {{7,1,5,3,6,4}, 5},
        {{7,6,4,3,1}, 0},
        {{1}, 0},
        {{2,4}, 2},
        {{4,2}, 0},
        {{3,3,3,3}, 0},
        {{1,2,3,4,5}, 4},
        {{5,4,3,2,1,2}, 1},
        {{2,1,2,1,0,1,2}, 2},
        {{9,1,5,3,7,4,8}, 7},
    };

    MaxProfit Solution;
    for (size_t i = 0; i < testCases.size(); ++i) {
        vector<int> prices = testCases[i].prices;

        int result1 = Solution.maxProfitI(prices);
        int result2 = Solution.maxProfitII(prices);
        int result3 = Solution.maxProfitIII(prices);

        assert(result1 == testCases[i].expected);
        assert(result2 == testCases[i].expected);
        assert(result3 == testCases[i].expected);
    }

    return 0;
}