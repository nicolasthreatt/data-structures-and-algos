"""
Maximize Sum Of Array After K Negations
https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/

Given an integer array nums and an integer k, modify the array in the following way:
    - Choose an index i and replace nums[i] with -nums[i].

You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.

Example 1:
    Input: nums = [4,2,3], k = 1
    Output: 5
    Explanation: Choose index 1 and nums becomes [4,-2,3].

Example 2:
    Input: nums = [3,-1,0,2], k = 3
    Output: 6
    Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].

Example 3:
    Input: nums = [2,-3,-1,5,-4], k = 2
    Output: 13
    Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].

Constraints:
    * 1 <= nums.length <= 10^4
    * -100 <= nums[i] <= 100
    * 1 <= k <= 10^4
"""

from typing import List

class MaxSumAfterKNegations:

    # Algorithm(s) Used: Greedy, Sorting
    # Time Complexity: (O(n*log(n)))
    # Space Complexity: O(1)
    def largestSumAfterKNegationsI(self, nums: List[int], k: int) -> int:
        nums.sort()

        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:  # Greedy Choice - Flip negatives to increase sum
                nums[i] = -nums[i]
                k -= 1

        # If k is still odd, flip smallest absolute value
        # Represent the remaining k flips since any index can be chosen multiple times
        if k % 2 == 1:
            nums.sort()
            nums[0] = -nums[0]
        
        return sum(nums)  # Global Solution - Max sum possible


if __name__ == "__main__":
    Solution = MaxSumAfterKNegations()

    test_cases = [
        ([4, 2, 3], 1, 5),
        ([3, -1, 0, 2], 3, 6),
        ([2, -3, -1, 5, -4], 2, 13),
        ([-1, -2, -3], 1, 0),
        ([-1, -2, -3], 2, 4),
        ([-1, -2, -3], 3, 6),
        ([1, 2, 3], 1, 4),
        ([1, 2, 3], 2, 6),
        ([1, 2, 3], 3, 4),
        ([0, 1, 2], 1, 3),
        ([0, 1, 2], 5, 3),
        ([5], 1, -5),
        ([5], 2, 5),
        ([-5], 1, 5),
        ([-5], 2, -5),
        ([1, -1], 1000, 0),
        ([1, -1], 999, 2),
        ([-2, 9, 9], 1, 20),
        ([-2, 9, 9], 2, 16),
    ]

    funcs = [
        Solution.largestSumAfterKNegationsI,
    ]

    for func in funcs:
        for nums, k, expected in test_cases:
            result = func(nums[:], k)
            assert result == expected

