/*
Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an
unknown pivot index k (1 <= k < nums.length) such that the resulting array is
    [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

Example 3:
    Input: nums = [1], target = 0
    Output: -1

Constraints:
    * 1 <= nums.length <= 5000
    * -10^4 <= nums[i] <= 10^4
    * All values of nums are unique.
    * nums is an ascending array that is possibly rotated.
    * -10^4 <= target <= 10^4
*/

#include <cassert>
#include <iostream>
#include <tuple>
#include <vector>

using namespace std;

class SearchInRotatedSortedArray {
public:

    // Algorithm(s) Used: Binary Search
    // Time Complexity: O(log(n))
    // Space Complexity: O(1)
    int searchI(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;

        // Perform Binary Search
        while (l <= r) {
            int m = (l + r) / 2;

            // Found Target
            if (nums[m] == target) {
                return m;
            }

            // Left Half Sorted - [4,5,6,7,0,1,2]
            if (nums[l] <= nums[m]) {
                if (nums[m] < target || nums[l] > target) { // Target is SMALLER than SMALLEST value in LEFT half
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }

            // Right Half Sorted - [6,7,0,1,2,3,4]
            else {
                if (nums[m] > target || nums[r] < target) { // Target is LARGER than LARGEST value in RIGHT half
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            }
        }

        return -1;
    }

    // Algorithm(s) Used: Binary Search
    // Time Complexity: O(log(n))
    // Space Complexity: O(1)
    int searchII(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;

        // Perform Binary Search
        while (l <= r) {
            int m = (l + r) / 2;

            // Found Target
            if (nums[m] == target) {
                return m;
            }

            // Left Half Sorted - [4,5,6,7,0,1,2]
            if (nums[l] <= nums[m]) {
                if (nums[m] > target && nums[l] <= target) { // Target is LARGER than SMALLEST value in LEFT half
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            }

            // Right Half Sorted - [6,7,0,1,2,3,4]
            else {
                if (nums[m] < target && nums[r] >= target) { // Target is SMALLER than LARGEST value in RIGHT half
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
        }

        return -1;
    }

    // Algorithm(s) Used: Binary Search
    // Time Complexity: O(log(n))
    // Space Complexity: O(1)
    int searchIII(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;

        // Perform Binary Search
        while (l <= r) {
            int m = (l + r) / 2;

            // Found Target
            if (nums[m] == target) {
                return m;
            }

            // Left Half Sorted - [4,5,6,7,0,1,2]
            if (nums[l] <= nums[m]) {
                if (nums[m] < target || nums[l] > target) { // Target is SMALLER than SMALLEST value in LEFT half
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }

            // Right Half Sorted - [6,7,0,1,2,3,4]
            else {
                if (nums[m] < target && nums[r] >= target) { // Target is SMALLER than LARGEST value in RIGHT half
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
        }

        return -1;
    }
};

int main() {
    SearchInRotatedSortedArray Solution;

    // (nums, target, expected_index)
    vector<tuple<vector<int>, int, int>> test_cases = {
        {{4, 5, 6, 7, 0, 1, 2}, 0, 4},
        {{4, 5, 6, 7, 0, 1, 2}, 3, -1},
        {{1}, 0, -1},
        {{1}, 1, 0},
        {{1, 2, 3, 4, 5}, 3, 2},
        {{5, 1, 2, 3, 4}, 1, 1},
        {{6, 7, 8, 1, 2, 3, 4, 5}, 6, 0},
        {{6, 7, 8, 1, 2, 3, 4, 5}, 5, 7},
        {{2, 3, 4, 5, 6, 7, 1}, 1, 6},
    };

    vector<int (SearchInRotatedSortedArray::*)(vector<int>&, int)> funcs = {
        &SearchInRotatedSortedArray::searchI,
        &SearchInRotatedSortedArray::searchII,
        &SearchInRotatedSortedArray::searchIII,
    };

    for (auto func : funcs) {
        for (auto& tc : test_cases) {
            vector<int> nums;
            int target, expected;
            tie(nums, target, expected) = tc;

            int result = (Solution.*func)(nums, target);
            assert(result == expected);
        }
    }

    return 0;
}
