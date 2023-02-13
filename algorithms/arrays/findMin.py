"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:
    - [4,5,6,7,0,1,2] if it was rotated 4 times.
    - [0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:
> n == nums.length
> 1 <= n <= 5000
> -5000 <= nums[i] <= 5000
> All the integers of nums are unique.
> nums is sorted and rotated between 1 and n times.
"""

from typing import List


# Binary Search
def findMin(nums: List[int]) -> int:
    # Initialize the result to the first element in the array
    res = nums[0]

    # Set left pointer to the first index of the array
    # Set right pointer to the last index of the array
    l, r = 0, len(nums) - 1

    # Begin binary search
    while l <= r:

        # If the left element node is less than the right element node, then
        # the left and right nodes are in the sorted portion of the array, thus
        # the left node node element will be the mininum of the entire array.
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        # We now know that the right node is greater than the left node
        # Determine mid point node
        m = (l + r) // 2
        res = min(res, nums[m])

        # If the midpoint is part of the left portion of the array, increament the left pointer one spot past the mid point.
        # If the midpoint is part of the right portion of the array, increament the rught pointer one spot before the mid point.
        # This ensures the next search range will be apart of the smaller sorted portion of the array
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1

    return res
