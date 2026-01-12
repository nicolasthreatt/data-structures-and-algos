"""
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
"""

from typing import List


class SubArraySumEqualsK:

    # Algorithm Used: Prefix Sum
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrays = 0  # Number of subarrays equal to k
        curr_sum = 0   # Current prefix sum

        # prefix_sums[diff] = number of times this sum has appeared
        prefix_sums = {0: 1}  # Allows subarrays starting at index 0

        for n in nums:
            # Count current prefix
            curr_sum += n

            # If curr_sum - k exists, the current subarray sums must be equal to k
            subarrays += prefix_sums.get(curr_sum - k, 0)  # diff = curr_sum - k

            # Update the frequency of the current prefix sum
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1

        return subarrays


if __name__ == "__main__":
    Solution = SubArraySumEqualsK()

    # (nums, k, expected)
    test_cases = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1], 1, 1),
        ([1], 0, 0),
        ([0, 0, 0], 0, 6),
        ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
        ([1, -1, 0], 0, 3),
        ([2, 2, 2], 4, 2),
    ]

    funcs = [
        Solution.subarraySum,
    ]

    for func in funcs:
        for nums, k, expected in test_cases:
            result = func(nums, k)
            assert result == expected
