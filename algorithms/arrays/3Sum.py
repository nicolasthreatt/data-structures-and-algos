"""
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
    * 3 <= nums.length <= 3000
    * -105 <= nums[i] <= 105
"""

from typing import List


# Time Complexity: O(nlog(n)) + O(n^2) = O(n^2)
def threeSum(self, nums: List[int]) -> List[List[int]]:
    # Initialize an empty list to store the return result
    res = []

    # Sort the input array
    nums.sort()

    # Iterate through list with an index
    for i, a in enumerate(nums):
        # Look to see if element was a duplicate
        # If duplicate element is found, skip it
        if i > 0 and a == nums[i - 1]:
            continue

        # Perform Two Sum with the current element in iteration in the list
        # with rest of the array to see if the triplet sums to 0
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])

                # To prevent an infinite loop, increment the left pointer
                l += 1

                # Keep incrementing left pointer if current value is the same
                # the same as previous value and less the r
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res