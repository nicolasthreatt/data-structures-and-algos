/*
Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/

You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:
    Input: cost = [10,15,20]
    Output: 15
    Explanation:
        You will start at index 1.
            - Pay 15 and climb two steps to reach the top.
        The total cost is 15.

Example 2:
    Input: cost = [1,100,1,1,1,100,1,1,100,1]
    Output: 6
    Explanation:
        You will start at index 0.
        - Pay 1 and climb two steps to reach index 2.
        - Pay 1 and climb two steps to reach index 4.
        - Pay 1 and climb two steps to reach index 6.
        - Pay 1 and climb one step to reach index 7.
        - Pay 1 and climb two steps to reach index 9.
        - Pay 1 and climb one step to reach the top.
    The total cost is 6.

Constraints:
    * 2 <= cost.length <= 1000
    * 0 <= cost[i] <= 999 
*/
#include <cassert>
#include <vector>

using namespace std;

// Algorithm(s) Used: Dynamic Prgramming (1-D), Bottom-Up
// Time Complexity: O(n)
// Space Complexity: O(1)
int minCostClimbingStairs(vector<int>& cost) {
    int one_step_cost = cost[0], two_steps_cost = cost[1];

    for (int i = 2; i < cost.size(); i++) {
        int curr_step_cost = cost[i] + min(one_step_cost, two_steps_cost);
        one_step_cost = two_steps_cost;
        two_steps_cost = curr_step_cost;
    }

    return min(one_step_cost, two_steps_cost);
}

int main() {
    vector<pair<vector<int>, int>> test_cases = {
        {{10, 15, 20}, 15},
        {{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}, 6},
        {{0, 0}, 0},
        {{1, 2, 3, 4}, 4},
        {{2, 2, 2, 2, 2}, 4},
    };

    for (auto& p : test_cases) {
        auto cost = p.first;
        int expected = p.second;
        assert(minCostClimbingStairs(cost) == expected);
    }

    return 0;
}
