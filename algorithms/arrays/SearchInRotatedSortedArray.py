"""
Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an
unknown pivot index k (1 <= k < nums.length) such that the resulting array is
    [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

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
    * -10^4 <= nums[i] <= 10^4
    * All values of nums are unique.
    * nums is an ascending array that is possibly rotated.
    * -10^4 <= target <= 10^4
"""

from typing import List


class SearchInRotatedSortedArray:

    # Algorithm Used: Binary Search, OR
    # Time Complexity: O(log(n))
    # Space Complexity: O(1)
    def searchI(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # Perform Binary Search
        while l <= r:
            mid = (l + r) // 2

            # Found Target
            if target == nums[mid]:
                return mid
            
            # LEFT Half Sorted - [4,5,6,7,0,1,2]
            if nums[l] <= nums[mid]:
                if nums[mid] < target or nums[l] > target:  # Target is SMALLER than SMALLEST value in LEFT half
                    l = mid + 1
                else: 
                    r = mid - 1

            # RIGHT Half Sorted - [6,7,0,1,2,3,4]
            else:
                if nums[mid] > target or nums[r] < target:  # Target is LARGER than LARGEST value in RIGHT half
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

    # Algorithm Used: Binary Search, AND
    # Time Complexity: O(log(n))
    # Space Complexity: O(1)
    def searchII(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # Perform Binary Search
        while l <= r:
            mid = (l + r) // 2

            # Found Target
            if target == nums[mid]:
                return mid
            
            # LEFT Half Sorted - [4,5,6,7,0,1,2]
            if nums[l] <= nums[mid]:
                if nums[mid] > target and nums[l] <= target:  # Target is LARGER than SMALLEST value in LEFT half
                    r = mid - 1
                else: 
                    l = mid + 1

            # RIGHT Half Sorted - [6,7,0,1,2,3,4]
            else:
                if nums[mid] < target and nums[r] >= target:  # Target is SMALLER than LARGEST value in RIGHT half
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

    # Algorithm Used: Binary Search
    # Space Complexity: O(1)
    # Time Complexity: O(log*N)
    def searchIII(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # Perform Binary Search
        while l <= r:
            m = (l + r) // 2

            # Found Target
            if nums[m] == target:
                return m

            # Left Half Sorted - [4,5,6,7,0,1,2]
            if nums[l] <= nums[m]:
                if nums[m] < target or nums[l] > target:  # Target is SMALLER than SMALLEST value in LEFT half
                    l = m + 1
                else: 
                    r = m - 1

            # Right Half Sorted - [6,7,0,1,2,3,4]
            else:
                if nums[m] < target and nums[r] >= target:  # Target is SMALLER than LARGEST value in RIGHT half
                    l = m + 1
                else:
                    r = m - 1

        return -1


if __name__ == "__main__":
    Solution = SearchInRotatedSortedArray()

    # (nums, target, expected_index)
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([1, 2, 3, 4, 5], 3, 2),
        ([5, 1, 2, 3, 4], 1, 1),
        ([6, 7, 8, 1, 2, 3, 4, 5], 6, 0),
        ([6, 7, 8, 1, 2, 3, 4, 5], 5, 7),
        ([2, 3, 4, 5, 6, 7, 1], 1, 6),
    ]

    funcs = [
        Solution.searchI,
        Solution.searchII,
    ]

    for func in funcs:
        for nums, target, expected in test_cases:
            result = func(nums[:], target)  # copy for safety
            assert result == expected
