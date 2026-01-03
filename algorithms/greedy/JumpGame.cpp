/*
Jump Game
https://leetcode.com/problems/jump-game/

You are given an integer array nums.

You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what.
                 Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
    * 1 <= nums.length <= 10^4
    * 0 <= nums[i] <= 10^5
*/

#include <cassert>
#include <vector>

using namespace std;

class JumpGame {
public:

    // Algorithm(s) Used: Greedy
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    bool canJumpI(vector<int>& nums) {
        int jumps = nums[0];

        for (int i = 1; i < nums.size(); ++i) {
            if (jumps <= 0) {
                return false;
            }
            jumps = max(jumps - 1, nums[i]);
        }

        return true;
    }
};

int main() {
    JumpGame solution;

    // (nums, expected)
    vector<pair<vector<int>, bool>> test_cases = {
        {{2, 3, 1, 1, 4}, true},
        {{3, 2, 1, 0, 4}, false},
        {{0}, true},
        {{1, 0}, true},
        {{0, 1}, false},
        {{2, 0, 0}, true},
        {{1, 1, 0, 1}, false},
        {{4, 0, 0, 0, 0}, true},
        {{1, 2, 0, 1}, true},
        {{2, 1, 0, 0}, false},
    };

    vector<bool (JumpGame::*)(vector<int>&)> funcs = {
        &JumpGame::canJumpI,
    };

    for (auto func : funcs) {
        for (auto& tc : test_cases) {
            vector<int> nums = tc.first;
            bool expected = tc.second;

            bool result = (solution.*func)(nums);
            assert(result == expected);
        }
    }

    return 0;
}
