"""
Missing Number
https://leetcode.com/problems/missing-number/

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Example 1:
    Input: nums = [3,0,1]
    Output: 2
    Explanation:
        n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
        2 is the missing number in the range since it does not appear in nums.

Example 2:
    Input: nums = [0,1]
    Output: 2
    Explanation:
        n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
        2 is the missing number in the range since it does not appear in nums.

Example 3:
    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8
    Explanation:
        n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
        8 is the missing number in the range since it does not appear in nums.

Constraints:
    * n == nums.length
    * 1 <= n <= 104
    * 0 <= nums[i] <= n
    * All the numbers of nums are unique.

Follow up:
    Implement a solution only O(1) extra space complexity and O(n) runtime complexity.
"""

from typing import List


# Algorithm(s) Used: Two Passes
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def missingNumberI(self, nums: List[int]) -> int:
    max_num = max(nums) # First Pass: O(n) - Find Max

    for num in range(max_num):  # Second Pass: O(n^2) - Find Missing Number
        if num not in nums:
            return num

    return max_num + 1


# Algorithm(s) Used: Two Passes, Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)
def missingNumberII(self, nums: List[int]) -> int:
    n = len(nums)
    seen = {i: -1 for i in range(n + 1)}

    for num in nums:
        seen[num] = num
    
    for i in range(n + 1):
        if seen[i] == -1:
            return i

    return -1


# Algorithm(s) Used: Two Passes
# Time Complexity: O(n)
# Space Complexity: O(1)
def missingNumberIII(self, nums: List[int]) -> int:
    n = len(nums)

    total_sum = sum(nums)
    expected_sum = sum([i for i in range(n + 1)])

    return expected_sum - total_sum


if __name__ == "__main__":
    test_cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([1], 0),
        ([0], 1),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0], 11),
    ]

    funcs = [missingNumberI, missingNumberII, missingNumberIII]

    for func in funcs:
        for nums, expected in test_cases:
            assert func(None, nums) == expected
