"""
Largest Perimeter Triangle
https://leetcode.com/problems/largest-perimeter-triangle/

Given an integer array nums,
return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths.

If it is impossible to form any triangle of a non-zero area, return 0.

Example 1:
    Input: nums = [2,1,2]
    Output: 5
    Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
Example 2:
    Input: nums = [1,2,1,10]
    Output: 0
    Explanation: 
        - You cannot use the side lengths 1, 1, and 2 to form a triangle.
        - You cannot use the side lengths 1, 1, and 10 to form a triangle.
        - You cannot use the side lengths 1, 2, and 10 to form a triangle.
        - As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.

Constraints:
    - 3 <= nums.length <= 10^4
    - 1 <= nums[i] <= 10^6
"""

from typing import List


class LargestPerimeterTriangle:

    # Algorithm(s) Used: Greedy, Sorting
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def largestPerimeterI(self, nums: List[int]) -> int:

        nums.sort(reverse=True)
        for i in range(2, len(nums)):
            c = nums[i - 2]  # Largest Side
            b = nums[i - 1]
            a = nums[i]      # Smallest Side

            if c < a + b:         # Greedy Choice - Valid Triangle (a <= b <= c)
                return a + b + c  # Local Solution - Perimeter (a + b + c)

        # Greedy Solution - No Valid Triangle Found
        return 0


if __name__ == "__main__":
    Solution = LargestPerimeterTriangle()

    # (nums, expected)
    test_cases = [
        ([2, 1, 2], 5),
        ([1, 2, 1, 10], 0),
        ([3, 6, 2, 3], 8),
        ([1, 2, 3], 0),
        ([10, 15, 7, 5, 8], 33),
        ([1, 1, 1, 3, 3], 7),
        ([2, 2, 1], 5),
        ([1, 1, 2, 2, 3, 4], 9),
    ]

    for nums, expected in test_cases:
        result = Solution.largestPerimeterI(nums)
        assert result == expected
