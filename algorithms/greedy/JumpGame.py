"""
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
"""

from typing import List


class JumpGame:

    # Algorithm(s) Used: Greedy
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def canJumpI(self, nums: List[int]) -> bool:
        jumps = nums[0]  # Max remaining steps reachable at current index

        for i in range(1, len(nums)):

            # Greedy Choice - No more jumps
            if jumps <= 0:
                return False

            # Local Optimum Solution
            jumps = max(jumps - 1, nums[i])

        return True  # Global Optimum Solution


if __name__ == "__main__":
    Solution = JumpGame()

    # (nums, expected)
    test_cases = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([1, 0], True),
        ([0, 1], False),
        ([2, 0, 0], True),
        ([3, 0, 0, 0], True),
        ([1, 1, 0, 1], False),
        ([4, 0, 0, 0, 0], True),
        ([1, 2, 0, 1], True),
        ([2, 1, 0, 0], False),
        ([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0] , True)
    ]

    funcs = [
        Solution.canJumpI,
    ]

    for func in funcs:
        for nums, expected in test_cases:
            result = func(nums)
            assert result == expected
