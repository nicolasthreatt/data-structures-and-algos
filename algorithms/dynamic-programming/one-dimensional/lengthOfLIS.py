"""
https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:
    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
    Input: nums = [0,1,0,3,2,3]
    Output: 4

Example 3:
    Input: nums = [7,7,7,7,7,7,7]
    Output: 1

Constraints:
    * 1 <= nums.length <= 2500
    * -10^4 <= nums[i] <= 10^4
"""

from typing import List


# Algorithm Used: Dynamic Programming, One-Dimensional, Buttom-Up
# Time Complexity: O(n^2)
# Memory Complexity: 0(n)
def lengthOfLISI(nums: List[int]) -> int:
    # Initialize the LIS array to 1 since each element is a subsequence of length 1
    # Each element in LIS array represents the length of the longest increasing subsequencs that ends at that index
    # For example, LIS[0] = 1 means that the longest increasing subsequence that ends at index 0 is of length 1
    LIS = [1] * len(nums)

    # Loop through the list backwards
    for current_index in range(len(nums) - 1, -1, -1):
        # Loop through the list from current_index + 1 to the end of the list
        # This is because we are looking for the longest increasing subsequence that ends at the current_index
        # which can be found by looking at the longest increasing subsequence that ends at the next_index.
        for next_index in range(current_index + 1, len(nums)):
            # If the element at current index is less than the element at next indx, then extend the longest
            # increasing subsequence that ends at current index by 1.
            # For example, if nums = [1, 2, 3, 4, 5], then LIS = [1, 2, 3, 4, 5] since each element is a subsequence
            # of length 1. However, if nums = [1, 2, 3, 4, 5, 0], then LIS = [1, 2, 3, 4, 5, 1] since the longest.
            if nums[current_index] < nums[next_index]:
                LIS[current_index] = max(LIS[current_index], 1 + LIS[next_index])

    # Return the maximum value of the LIS array
    # Recall that LIS[n] represents the length of the longest increasing subsequence that ends at index n.
    return max(LIS)
