"""
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List


# Time Complexity: O(n)
# Space Complexity: O(1)
def productExceptSelf(self, nums: List[int]) -> List[int]:
    # Create an output list the size of the input list
    res = [1] * len(nums)

    # Pass through list once, in ORDER, to store the PREFIX multipler for each element in list
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    # Pass through list once, in REVERSE, to calculate the POSTFIX multipler for each element in list
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    
    return res