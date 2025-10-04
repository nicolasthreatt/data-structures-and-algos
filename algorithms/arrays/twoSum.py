"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

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
    * 2 <= nums.length <= 10^4
    * -10^9 <= nums[i] <= 10^9
    * -10^9 <= target <= 10^9
    * Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

from typing import List


# Algorithm Used: Iteration
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def twoSumI(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        # Loop through list again, but at one index ahead of previous loop
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:  # Determine is elements sum to the target
                return [i, j]
    return []


# Algorithm Used: Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)
def twoSumII(nums: List[int], target: int) -> List[int]:
    prevMap = {}  # {number: index}

    for i, n in enumerate(nums):
        # Calculate the difference value that will sum to the target
        diff = target - n

        # If the difference value is in the hashmap, return the summons
        if diff in prevMap:
            return [prevMap[diff], i]

        # If the difference value is NOT in the hashmap, add value as the key and its index as the value
        prevMap[n] = i

    return []


if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2], 3, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
        ([1, 3, 5, 7], 10, [1, 3]),
    ]

    for func in [twoSumI, twoSumII]:
        for nums, target, expected in test_cases:
            result = func(nums, target)
            assert set(result) == set(expected)
