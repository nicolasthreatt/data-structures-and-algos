"""
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
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

# Time Complexity O(n)
def containsDuplicate(self, nums: List[int]) -> bool:
    # Create a set for the elements 
    hashset = set()

    # Loop through list ONCE
    for n in nums:

        # Check to see if number is in hash set
        # This means there is a duplicate
        if n in hashset:
            return True

        # Add number to hash set if NOT in hash set
        hashset.add(n)

    # Return False is there are no duplicates
    return False