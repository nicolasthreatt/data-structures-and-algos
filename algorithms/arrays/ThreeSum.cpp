/*
3Sum
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
        * nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0
        * nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0
        * nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0
        * The distinct triplets are [-1,0,1] and [-1,-1,2]

Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.

Constraints:
    * 3 <= nums.length <= 3000
    * -10^5 <= nums[i] <= 10^5
*/

#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class ThreeSum {
public:

    // Algorithm(s) Used: Binary Search, Sort
    // Time Complexity: O(nlog(n)) + O(n^2) = O(n^2)
    // Space Complexity: O(n)
    vector<vector<int>> threeSumI(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> triplets = {};

        sort(nums.begin(), nums.end()); // Time Compleity: O(nlog(n))
        
        for (int i = 0; i < n; i++) {
            if (i > 0 && nums[i - 1] == nums[i]) continue; // Skip duplicates

            // Perform Binary Search For Each Element (Time Complexity: O(n^2))
            int j = i + 1, k = n - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum > 0) {
                    k -= 1;
                } else if (sum < 0) {
                    j += 1;
                } else {
                    triplets.push_back({nums[i], nums[j], nums[k]});

                    j += 1;
                    while (j < k && nums[j - 1] == nums[j]) j += 1; // Skip duplicates
                }
            }
        }

        return triplets;
    }
};

// Helper function to normalize triplets for comparison
vector<vector<int>> sortTriplets(vector<vector<int>> v) {
    for (auto& t : v) sort(t.begin(), t.end());
    sort(v.begin(), v.end());
    return v;
}

int main() {
    ThreeSum solution;

    vector<pair<vector<int>, vector<vector<int>>>> test_cases = {
        {{-1,0,1,2,-1,-4}, {{-1,-1,2}, {-1,0,1}}},
        {{0,1,1}, {}},
        {{0,0,0}, {{0,0,0}}},
        {{1,2,-2,-1}, {}},
        {{3,-2,1,0}, {}},
        {{0,0,0,0}, {{0,0,0}}},
        {{-2,0,1,1,2}, {{-2,0,2}, {-2,1,1}}},
        {{}, {}},
        {{1,2,3}, {}},
        {{-1,0,1}, {{-1,0,1}}},
        {{-4,-2,-2,-2,0,1,2,2,2}, {{-4,2,2}, {-2,0,2}}}
    };

    for (auto& test : test_cases) {
        auto nums = test.first;
        auto expected = test.second;

        auto result = solution.threeSumI(nums);

        assert(sortTriplets(result) == sortTriplets(expected));
    }

    return 0;
}
