"""
https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an
unknown pivot index k (1 <= k < nums.length) such that the resulting array is
    [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target
if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
 
Constraints:
    * 1 <= nums.length <= 5000
    * -104 <= nums[i] <= 104
    * All values of nums are unique.
    * nums is an ascending array that is possibly rotated.
    * -104 <= target <= 104
"""

from typing import List


# Algorithm Used: Binary Search
# Time Complexity: O(log(n))
# Space Complexity: O(1)
def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        # Compute middle value of left and right iterators
        mid = (l + r) // 2

        # Check to see if target is equal to the middle value 
        if target == nums[mid]:
            return mid
        
        # Middle a part of left sorted portion
        if nums[l] <= nums[mid]:

            # If target is greater than middle value OR
            # If target is less than the left most value then
            # SEARCH RIGHT
            if target > nums[mid] or target < nums[l]: 
                l = mid + 1
            # Target is less than the middle value AND
            # Targer is greater than the left most value
            # SEARCH LEFT
            else: 
                r = mid - 1
        
        # Middle is a part of right sorted portion
        else:

            # If target less than middle value OR
            # If target is greater than right most value then
            # SEARCH LEFT
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            # Target value is greater than middle value AND
            # Target is less than the right most value
            # SEARCH RIGHT
            else:
                l = mid + 1

    # Return -1 if binary search is not successful
    return -1
