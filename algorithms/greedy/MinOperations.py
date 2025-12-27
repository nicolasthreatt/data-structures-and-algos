"""
Minimum Operations to Make the Array Increasing
https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

You are given an integer array nums (0-indexed).
In one operation, you can choose an element of the array and increment it by 1.

For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1.
An array of length 1 is trivially strictly increasing.

Example 1:
    Input: nums = [1,1,1]
    Output: 3
    Explanation: You can do the following operations:
        1) Increment nums[2], so nums becomes [1,1,2].
        2) Increment nums[1], so nums becomes [1,2,2].
        3) Increment nums[2], so nums becomes [1,2,3].

Example 2:
    Input: nums = [1,5,2,4,1]
    Output: 14

Example 3:
    Input: nums = [8]
    Output: 0

Constraints:
    1 <= nums.length <= 5000
    1 <= nums[i] <= 10^4
"""

from typing import List


class MinOperations:

    # Algorithm Used: Greedy, In-Place
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def minOperationsI(self, nums: List[int]) -> int:
        operations = 0     # Global Optimal
        prev_num = nums[0] # Last adjusted value

        for i in range(1, len(nums)):
            if prev_num >= nums[i]:  # Greedy Choice - Count Operations Needed
                prev_num += 1  # Update to be increasing

                needed = prev_num - nums[i] #+ 1
                operations += needed  # Local Optimal Choice
            else:
                prev_num = nums[i]  # Update to keep increasing

        return operations

    # Algorithm Used: Greedy, In-Place
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def minOperationsII(self, nums: List[int]) -> int:
        operations = 0  # Global Optimal

        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:  # Greedy Choice - Count Operations Needed
                needed = nums[i - 1] - nums[i] + 1
                operations += needed  # Local Optimal Choice
                nums[i] = nums[i - 1] + 1  # Update to be increasing

        return operations


if __name__ == "__main__":
    Solution = MinOperations()

    test_cases = [
        # (nums, expected)
        ([1, 1, 1], 3),
        ([1, 5, 2, 4, 1], 14),
        ([8], 0),
        ([1, 2, 3], 0),
        ([3, 2, 1], 6),
        ([1, 1, 2, 2], 4),
        ([5, 5, 5, 5], 6),
        ([1, 3, 2], 2),
    ]

    funcs = [
        Solution.minOperationsI,
        Solution.minOperationsII,
    ]

    for func in funcs:
        for nums, expected in test_cases:
            result = func(nums.copy())
            assert result == expected
