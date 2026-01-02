/*
Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum 1.

Example 3:
    Input: nums = [5,4,-1,7,8]
    Output: 23
    Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
    * 1 <= nums.length <= 10^5
    * -10^4 <= nums[i] <= 10^4
*/

#include <cassert>
#include <tuple>
#include <vector>

using namespace std;

class MaxSubArray {
public:

    // Algorithm(s) Used: Brute Force
    // Time Complexity: O(n^2)
    // Splace Complexity: O(1)
    int maxSubArrayI(vector<int>& nums) {
        int max_sum = nums[0];  // Sum of entire array

        // Iterate over each element as if it's the start of a new subarray
        for (int i = 0; i < nums.size(); ++i) {
            int curr_sum = 0;   // Sum of current subarray
            for (int j = i; j < nums.size(); ++j) {
                curr_sum += nums[j];
                max_sum = max(max_sum, curr_sum);
            }
        }

        return max_sum;
    }

    // Algorithm(s) Used: Greedy
    // Time Complexity: O(n)
    // Splace Complexity: O(1)
    int maxSubArrayII(vector<int>& nums) {
        int max_sum = nums[0];  // Sum of entire array
        int curr_sum = 0;       // Sum of current subarray

        for (int num : nums) {
            curr_sum += num;
            max_sum = max(max_sum, curr_sum);

            if (curr_sum < 0) {
                curr_sum = 0;
            }
        }

        return max_sum;  // Global Solution - Max subarray sum
    }

    // Algorithm(s) Used: Greedy, Kadane's Algorithm
    // Time Complexity: O(n)
    // Splace Complexity: O(1)
    int maxSubArrayIII(vector<int>& nums) {
        int max_sum = nums[0];  // Sum of entire array
        int curr_sum = 0;       // Sum of current subarray

        for (int num : nums) {
            curr_sum = max(curr_sum + num, num);  // // Greedy Choice - Extend or Reset SUBARRAY Sum
            max_sum = max(max_sum, curr_sum);
        }

        return max_sum;  // Global Solution - Max subarray sum
    }
};

int main() {
    MaxSubArray Solution;

    // (nums, expected_output)
    vector<tuple<vector<int>, int>> test_cases = {
        {{-2, 1, -3, 4, -1, 2, 1, -5, 4}, 6},
        {{1}, 1},
        {{5, 4, -1, 7, 8}, 23},
        {{-1, -2, -3, -4}, -1},
        {{0}, 0},
        {{0, 0, 0}, 0},
        {{1, 2, 3, 4}, 10},
        {{-2, -1}, -1},
        {{2, -1, 2, 3, 4, -5}, 10},
        {{100000}, 100000},
    };

    vector<int (MaxSubArray::*)(vector<int>&)> funcs = {
        &MaxSubArray::maxSubArrayI,
        &MaxSubArray::maxSubArrayII,
        &MaxSubArray::maxSubArrayIII,
    };

    for (auto func : funcs) {
        for (auto& tc : test_cases) {
            vector<int> nums;
            int expected;
            tie(nums, expected) = tc;

            int result = (Solution.*func)(nums);
            assert(result == expected);
        }
    }

    return 0;
}
