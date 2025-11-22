/*
Missing Number
https://leetcode.com/problems/missing-number/

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Example 1:
    Input: nums = [3,0,1]
    Output: 2
    Explanation:
        n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
        2 is the missing number in the range since it does not appear in nums.

Example 2:
    Input: nums = [0,1]
    Output: 2
    Explanation:
        n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
        2 is the missing number in the range since it does not appear in nums.

Example 3:
    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8
    Explanation:
        n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
        8 is the missing number in the range since it does not appear in nums.

Constraints:
    * n == nums.length
    * 1 <= n <= 10^4
    * 0 <= nums[i] <= n
    * All the numbers of nums are unique.

Follow up:
    Implement a solution only O(1) extra space complexity and O(n) runtime complexity.
*/

#include <cassert>
// #include <map>
#include <vector>

using namespace std;

// Algorithm(s) Used: Two Passes, Hash Map
// Time Complexity: O(n)
// Space Complexity: O(n)
int missingNumberI(vector<int>& nums) {
    int n = nums.size();
    vector<int> seen(n + 1, -1);

    for (int num : nums) {
        seen[num] = num;
    }

    for (int i = 0; i <= n; i++) {
        if (seen[i] == -1) {
            return i;
        }
    }

    return -1;
}

// Algorithm(s) Used: Two Passes
// Time Complexity: O(n)
// Space Complexity: O(1)
int missingNumberII(vector<int>& nums) {
    int n = nums.size();

    int total_sum = 0;
    for (int num : nums) {
        total_sum += num;
    }

    int expected_sum = 0;
    for (int i = 0; i <= n; i++) {
        expected_sum += i;
    }

    return expected_sum - total_sum;
}

int main() {
    vector<pair<vector<int>, int>> test_cases = {
        {{3, 0, 1}, 2},
        {{0, 1}, 2},
        {{9, 6, 4, 2, 3, 5, 7, 0, 1}, 8},
        {{1}, 0},
        {{0}, 1},
        {{1,2,3,4,5,6,7,8,9,10,0}, 11},
    };

    vector<int(*)(vector<int>&)> funcs = {
        missingNumberI,
        missingNumberII
    };

    for (auto func : funcs) {
        for (auto &tc : test_cases) {
            vector<int> nums = tc.first;
            int expected = tc.second;
            assert(func(nums) == expected);
        }
    }

    return 0;
}
