"""
Find The Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/

Given an array of integers nums containing n + 1 integers where each
integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
    Input: nums = [1,3,4,2,2]
    Output: 2

Example 2:
    Input: nums = [3,1,3,4,2]
    Output: 3

Constraints:
    * 1 <= n <= 10^5
    * nums.length == n + 1
    * 1 <= nums[i] <= n
    * All the integers in nums appear only once except
      for precisely one integer which appears two or more times.

Follow up:
    * How can we prove that at least one duplicate number must exist in nums?
    * Can you solve the problem in linear runtime complexity?
"""

from typing import List


class FindDuplicates:

    # Algorithm Used: Hash Set
    # Time Complexity: O(n)
    # Memory Complexity: O(n)
    def findDuplicateI(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                return num

            seen.add(num)

        return None

    # Algorithm Used: Binary Search
    # Time Complexity: O(n*logn)
    # Memory Complexity: O(1)
    def findDuplicateII(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Count values that are less than or equal to mid
            # If count is greater than mid, duplicate is in the left half.
            #   - More than mid values in [1..mid] means at least one value repeats.
            count = 0

            for num in nums:
                if num <= mid:
                    count += 1

            if count > mid:
                right = mid
            else:
                left = mid + 1

        return left

    # Algorithm Used: Linked List Cycle, Floyd's Tortoise & Hare, Two Passes
    # Time Complexity: O(n)
    # Memory Complexity: O(1)
    def findDuplicateIII(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        # Move slow by 1 and fast by 2 until they meet inside the cycle
        # End 1st Pass when slow and fast point to the same index.
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Move one pointer from start and one from meeting point at the same speed.
        # The node where they meet is the cycle entry, which is the duplicate value.
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


if __name__ == "__main__":
    Solution = FindDuplicates()

    test_cases = [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([1, 1], 1),
        ([1, 4, 6, 2, 6, 3, 5], 6),
        ([2, 2, 2, 2, 2], 2),
        ([2, 5, 1, 1, 4, 3], 1),
        ([4, 3, 1, 4, 2], 4),
        ([5, 4, 3, 2, 1, 5], 5),
    ]

    funcs = [
        Solution.findDuplicateI,
        Solution.findDuplicateII,
        Solution.findDuplicateIII
    ]

    for func in funcs:
        for nums, expected in test_cases:
            result = func(nums)
            assert result == expected
