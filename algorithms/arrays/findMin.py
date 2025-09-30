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
    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    All the integers of nums are unique.
    nums is sorted and rotated between 1 and n times.
"""

from typing import List


# Algorithm Used: Binary Search
# Time Complexity: O(log(n))
# Space Complexity: O(1)
def findMinI(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        
        if nums[r] < nums[mid]:  # If mid element is greater than right, then min must be right of mid
            l = mid + 1
        else:  # Otherwise, min is at mid or to the left of mid
            r = mid

    # After loop l == r (NOT l > r), meaning the search space is narrowed to one element, the minimum
    return nums[l]

# Algorithm Used: Binary Search
# Time Complexity: O(log(n))
# Space Complexity: O(1)
def findMinII(nums: List[int]) -> int:
    res = nums[0]

    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2

        # Subarray is fully sorted and nums[l] is the minimum
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        # Update result with the current minimum
        res = min(res, nums[m])

        # If mid is in the left sorted portion, discard it and search right
        # If mid is in the right unsorted portion, search left
        if nums[l] <= nums[m]:
            l = m + 1
        else:
            r = m - 1

    return res
