/*
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:
    * 2 <= nums.length <= 10^4
    * -10^9 <= nums[i] <= 10^9
    * -10^9 <= target <= 10^9
    * Only one valid answer exists.

Follow-up:
    Can you come up with an algorithm that is less than O(n2) time complexity?
*/

#include <cassert>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

// Algorithm Used: Brute Force, Nested Iteration
// Time Complexity: O(n^2)
// Space Complexity: O(n)
vector<int> twoSumI(vector<int>& nums, int target) {
    vector<int> result;
    
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] + nums[j] == target) {
                result = {i, j};
                break;
            }
        }
    }

    return result;
}


// Algorithm Used: Hash Map, Single Iteration
// Time Complexity: O(n)
// Space Complexity: O(n)
vector<int> twoSumII(vector<int>& nums, int target) {
    vector<int> result;
    map<int, int> mapper;

    for (int i = 0; i < nums.size(); i++) {
        // Calculate the difference value that will sum to the target
        int diff = target - nums[i];

        // If difference is NOT in the map, add curr number as key and curr index as value
        if (!mapper.contains(diff)) {
            mapper.insert({nums[i], i});
        } else {
            // If difference IS in the map, found a pair so store index of difference and curr index
            result.push_back(mapper.at(diff));
            result.push_back(i);
            break;
        }
    }

    return result;
}

int main() {
        struct TestCase {
        vector<int> nums;
        int target;
        vector<int> expected;
    };

    vector<TestCase> testCases = {
        {{2, 7, 11, 15}, 9, {0, 1}},
        {{3, 2, 4}, 6, {1, 2}},
        {{3, 3}, 6, {0, 1}},
        {{-1, -2, -3, -4, -5}, -8, {2, 4}},
        {{1, 5, 3, 7}, 8, {1, 2}}
    };

    for (auto& test : testCases) {
        vector<int> res1 = twoSumI(test.nums, test.target);
        vector<int> res2 = twoSumII(test.nums, test.target);

        // Check both have correct length
        assert(res1.size() == 2);
        assert(res2.size() == 2);

        // Check sums are correct
        assert(test.nums[res1[0]] + test.nums[res1[1]] == test.target);
        assert(test.nums[res2[0]] + test.nums[res2[1]] == test.target);

        // Check indices match expected
        assert(res1 == test.expected || (res1[0] == test.expected[1] && res1[1] == test.expected[0]));
        assert(res2 == test.expected || (res2[0] == test.expected[1] && res2[1] == test.expected[0]));
    }

    return 0;
}
