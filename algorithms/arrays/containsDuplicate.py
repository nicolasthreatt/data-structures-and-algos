"""
Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
    Input: nums = [1,2,3,1]
    Output: true

Example 2:
    Input: nums = [1,2,3,4]
    Output: false

Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

Constraints:
    * 1 <= nums.length <= 10^5
    * -10^9 <= nums[i] <= 10^9
"""

from typing import List


# Algorithm(s) Used: Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)
def containsDuplicate(self, nums: List[int]) -> bool:
    seen = set()

    for n in nums:

        # Check to see if number is in hash set, indicating a duplicate.
        if n in seen:
            return True

        # Add number to hash set if NOT in hash set
        seen.add(n)

    return False


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([0], False),
        ([5, 5], True),
        ([-1, -1], True),
        ([10, 20, 30], False),
    ]

    funcs = [containsDuplicate]

    for func in funcs:
        for nums, expected in test_cases:
            assert func(None, nums) == expected
