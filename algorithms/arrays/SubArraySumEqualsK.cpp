/*
Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k,
return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [1,1,1], k = 2
    Output: 2

Example 2:
    Input: nums = [1,2,3], k = 3
    Output: 2

Constraints:
    * 1 <= nums.length <= 2 * 10^4
    * -1000 <= nums[i] <= 1000
    * -10^7 <= k <= 10^7
*/

#include <cassert>
#include <unordered_map>
#include <vector>

using namespace std;

class SubArraySumEqualsK {
public:

    // Algorithm Used: Prefix Sum
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    int subarraySumI(vector<int>& nums, int k) {
        int subarrays = 0;  // Number of subarrays equal to k
        int curr_sum = 0;   // Current prefix sum

        unordered_map<int, int> prefix_sums;  // { sum: # of times sum has appeared }
        prefix_sums[0] = 1;                   // Allows subarrays starting at index 0

        for (int num : nums) {
            // Count current prefix
            curr_sum += num;

            // If curr_sum - k exists, the current subarray sums must be equal to k
            subarrays += prefix_sums[curr_sum - k];

            // Update the frequency of the current prefix sum
            prefix_sums[curr_sum]++;
        }

        return subarrays;
    }
};

int main() {
    SubArraySumEqualsK Solution;

    // (nums, k, expected)
    vector<tuple<vector<int>, int, int>> test_cases = {
        {{1, 1, 1}, 2, 2},
        {{1, 2, 3}, 3, 2},
        {{1}, 1, 1},
        {{1}, 0, 0},
        {{0, 0, 0}, 0, 6},
        {{3, 4, 7, 2, -3, 1, 4, 2}, 7, 4},
        {{1, -1, 0}, 0, 3},
        {{2, 2, 2}, 4, 2},
    };

    vector<int (SubArraySumEqualsK::*)(vector<int>&, int)> funcs = {
        &SubArraySumEqualsK::subarraySumI,
    };

    for (auto func : funcs) {
        for (auto& tc : test_cases) {
            vector<int> nums;
            int k, expected;
            tie(nums, k, expected) = tc;

            int result = (Solution.*func)(nums, k);
            assert(result == expected);
        }
    }

    return 0;
}
