"""
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Example 3:
Input: nums = [-3,0,1,-2]
Output: 1
Explanation: [1] and product of itself has the largest product
 
Constraints:
1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List


# Time Complexity: O(n)
# Memory Complexity: 0(1)
def maxProduct(self, nums: List[int]) -> int:
    # Initialize the result to the max element of list
    res = max(nums)

    # Initialize both the current minimun and current maximum products to 1 since its neutral
    curMin, curMax = 1, 1

    # Loop through the list once
    for n in nums:

        # Reset the current maximum and minimum back to 1 if current num is 0
        # This will ensure that the current maximum and mininum products are 
        # not 0 for the rest of the iteration
        if n == 0:
            curMin, curMax = 1, 1
            continue
        
        # Temporarily store the current max product as it gets recalculated below
        tmp = curMax * n

        # Determine both the current maximum and minimum since n can be negative or positive
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)

        # Determine the maxmimum value of the sub-array
        res = max(res, curMax)

    return res