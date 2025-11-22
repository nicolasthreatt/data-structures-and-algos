/*
Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
    Input: nums = [1,2,3,1]
    Output: true

Example 2:
    Input: nums = [1,2,3,4]
    Output: false

Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

Constraints:
    * 1 <= nums.length <= 10^5
    * -10^9 <= nums[i] <= 10^9
*/

#include <cassert>
#include <set>
#include <vector>

using namespace std;

// Algorithm(s) Used: Brute Force
// Time Complexity: O(n^2)
// Space Complexity: O(1)
bool containsDuplicateI(vector<int>& nums) {
    for (int i = 0; i < nums.size(); i++) {
        for (int j = 0; j < nums.size(); j++) {
            if (i != j && nums[i] == nums[j]) {
                return true;
            }
        }
    }

    return false;
}

// Algorithm(s) Used: Hash Map
// Time Complexity: O(n)
// Space Complexity: O(n)
bool containsDuplicateII(vector<int>& nums) {
    set<int> mapper = {};

    for (int num : nums) {
        if (mapper.contains(num)) {
            return true;
        }
        mapper.insert(num);
    }

    return false;
}

int main() {
    vector<pair<vector<int>, bool>> test_cases = {
        {{1, 2, 3, 1}, true},
        {{1, 2, 3, 4}, false},
        {{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}, true},
        {{0}, false},
        {{5, 5}, true},
        {{-1, -1}, true},
        {{10, 20, 30}, false},
    };

    vector<bool(*)(vector<int>&)> funcs = {
        containsDuplicateI,
        containsDuplicateII
    };

    for (auto func : funcs) {
        for (auto &tc : test_cases) {
            vector<int> nums = tc.first;
            bool expected = tc.second;
            assert(func(nums) == expected);
        }
    }

    return 0;
}
