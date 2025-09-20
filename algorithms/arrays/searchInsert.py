"""
Search Insert Position
https://leetcode.com/problems/search-insert-position

Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log(n)) runtime complexity.

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4

Constraints:
    * 1 <= nums.length <= 10^4
    * -10^4 <= nums[i] <= 10^4
    * nums contains distinct values sorted in ascending order.
    * -10^4 <= target <= 10^4
"""

from typing import List


# Algorithm Used: Binary Search
# Time Complexity: O(log(n))
# Space Complexity: O(1)
def searchInsert(nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid  # target found

        # Target not found, so left is greater than right
        # Left is where target would go since all elements before left are less than target
        return l


if __name__ == "__main__":
    # Examples
    assert searchInsert([1, 3, 5, 6], 5) == 2
    assert searchInsert([1, 3, 5, 6], 2) == 1
    assert searchInsert([1, 3, 5, 6], 7) == 4

    # Additional edge cases
    assert searchInsert([1, 3, 5, 6], 0) == 0         # Insert at beginning
    assert searchInsert([1, 3, 5, 6], 6) == 3         # Insert at end (exact match)
    assert searchInsert([1, 3, 5, 6], 4) == 2         # Between two elements
    assert searchInsert([1], 0) == 0                  # Single element list, insert before
    assert searchInsert([1], 2) == 1                  # Single element list, insert after
    assert searchInsert([1, 3], 2) == 1               # Between two elements
    assert searchInsert([1, 3, 5], 4) == 2            # Another between case
