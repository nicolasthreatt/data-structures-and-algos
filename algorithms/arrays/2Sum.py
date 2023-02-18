"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

from typing import List


def twoSum_On(self, nums: List[int], target: int) -> List[int]:
    # Create hash map
    prevMap = {} # val : index

    # Loop through list
    for i, n in enumerate(nums):
        # For each element in the list, calculate the difference value that will sum to the target
        diff = target - n

        # If the difference value is in the hashmap, return the summons
        if diff in prevMap:
            return [prevMap[diff], i]

        # If the difference value is NOT in the hashmap, add value as the key and its index as the value
        prevMap[n] = i
    return

def twoSum_On2(self, nums: List[int], target: int) -> List[int]:
    # Loop through list
    for i in range(len(nums)):
        # Loop through list again, but at one index ahead of previous loop
        for j in range(i + 1, len(nums)):
            # Determine is elements sum to the target
            if nums[i] + nums[j] == target:
                return [i, j]