"""
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
"""

from typing import List


class MaxSubArray:

    # Algorithm Used: Brute Force
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def maxSubArrayI(self, nums: List[int]) -> int:
        max_sum = nums[0]  # Sum of entire array

        # Iterate over each element as if it's the start of a new subarray
        for i in range(len(nums)):
            curr_sum = 0  # Sum of current subarray
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)

        return max_sum

    # Algorithm Used: Greedy
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxSubArrayII(self, nums: List[int]) -> int:
        max_sum = nums[0]  # Sum of entire array
        current_sum = 0    # Sum of current subarray

        for num in nums:
            current_sum += num  # Greedy Choice 1 - Extend SUBARRAY sum
            max_sum = max(max_sum, current_sum)

            # Greedy Choice 2 - Reset SUBARRAY sum, if negagive
            if current_sum < 0:
                current_sum = 0

        return max_sum  # Global Solution - Max subarray sum

    # Algorithm Used: Greedy, Kadane's Algorithm
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxSubArrayIII(self, nums: List[int]) -> int:
        max_sum = nums[0]  # Sum of entire array
        current_sum = 0    # Sum of current subarray

        for num in nums:
            current_sum = max(num, current_sum + num)  # Greedy Choice - Extend or Reset SUBARRAY Sum
            max_sum = max(max_sum, current_sum)

        return max_sum  # Global Solution - Max subarray sum


if __name__ == "__main__":
    Solution = MaxSubArray()

    # (nums, expected_output)
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-1, -2, -3, -4], -1),
        ([0], 0),
        ([0, 0, 0], 0),
        ([1, 2, 3, 4], 10),
        ([-2, -1], -1),
        ([2, -1, 2, 3, 4, -5], 10),
        ([100000], 100000),
    ]

    funcs = [
        Solution.maxSubArrayI,
        Solution.maxSubArrayII,
        Solution.maxSubArrayIII,
    ]

    for func in funcs:
        for nums, expected in test_cases:
            result = func(nums[:])  # copy to avoid side effects
            assert result == expected
