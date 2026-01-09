/*
House Robber
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street.

Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have
security systems connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

Example 2:
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
    * 1 <= nums.length <= 100
    * 0 <= nums[i] <= 400
*/

#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class HouseRobberI {
public:

    // Algorithm(s) Used: Dynamic Programming (1-D), Bottom-Up, Tabulation
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    int robI(vector<int>& nums) {
        int n = nums.size();

        // Base Cases
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        if (n == 2) return max(nums[0], nums[1]);

        vector<int> dp(n + 1);
        dp[0] = 0;       // House CAN be robbed (Start With Nothing)
        dp[1] = nums[0]; // House CANNOT be robbed (First House To Rob)

        for (int i = 1; i < n; i++) {
            int two_houses_ago_robbed = dp[i - 1]; // House CAN be robbed
            int one_house_ago_robbed = dp[i];      // House CANNOT be robbed

            int curr_house_robbed = nums[i];

            dp[i + 1] = max(two_houses_ago_robbed + curr_house_robbed, one_house_ago_robbed);
        }

        return dp[n];
    }

    // Algorithm(s) Used: Dynamic Programming (1-D), Buttom-Up, Fibonacci Sequence
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    int robII(vector<int>& nums) {
        int n = nums.size();

        // Base Cases
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        if (n == 2) return max(nums[0], nums[1]);

        int two_houses_ago_robbed = 0;      // House CAN be robbed (Start With Nothing)
        int one_house_ago_robbed = nums[0]; // House CANNOT be robbed (First House To Rob)

        for (int i = 0; i < n; i++) {
            int curr_house_robbed = nums[i];

            int tmp = two_houses_ago_robbed;
            two_houses_ago_robbed = one_house_ago_robbed; // House CAN be robbed
            one_house_ago_robbed = max(tmp + curr_house_robbed, one_house_ago_robbed); // House CANNOT be robbed
        }

        return two_houses_ago_robbed;
    }
};


int main() {
    HouseRobberI Solution;

    vector<pair<vector<int>, int>> testCases = {
        {{1, 2, 3, 1}, 4},
        {{2, 7, 9, 3, 1}, 12},
        {{2, 1, 1, 2}, 4},
        {{0}, 0},
        {{5}, 5},
        {{1, 1, 1, 1}, 2},
        {{10, 2, 10, 2, 10}, 30},
        {{100, 1, 2, 100}, 200},
        {{1, 3, 1}, 3},
        {{4, 1, 2, 9, 1, 1, 9}, 22}
    };

    vector<int(HouseRobberI::*)(vector<int>&)> funcs = {
        &HouseRobberI::robI,
        &HouseRobberI::robII
    };

    for (auto func : funcs) {
        for (auto& test : testCases) {
            vector<int> nums = test.first;
            int expected = test.second;

            int result = (Solution.*func)(nums);
            assert(result == expected);
        }
    }

    return 0;
}
