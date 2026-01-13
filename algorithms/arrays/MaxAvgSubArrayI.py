"""
Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/

You are given an integer array nums consisting of n elements,
and an integer k.

Find a contiguous subarray whose length is equal to k
that has the maximum average value and return this value.

Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
    - Input: nums = [1,12,-5,-6,50,3], k = 4
    - Output: 12.75000
              Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
    - Input: nums = [5], k = 1
    - Output: 5.00000

Constraints:
    * n == nums.length
    * 1 <= k <= n <= 10^5
    * -10^4 <= nums[i] <= 10^4
"""


class MaxAvgSubArrayI:

    # Algorithm: Sliding Window, Two Pointers
    # Time Complexity: O(n)
    # Space Complexiity: O(1)
    def findMaxAverageI(self, nums: list, k: int) -> float:
        window_sum = 0
        max_sum = float("-inf")

        left = 0
        for right in range(len(nums)):
            window_sum += nums[right]
            window_legnth = right - left + 1

            if window_legnth == k:
                max_sum = max(max_sum, window_sum)
                window_sum -= nums[left]
                left += 1

        return max_sum / k

    # Algorithm: Fixed Sliding Window
    # Time Complexity: O(n)
    # Space Complexiity: O(1)
    def findMaxAverageII(self, nums: list, k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k


if __name__ == "__main__":
    Solution = MaxAvgSubArrayI()

    # (nums, k, expected)
    test_cases = [
        ([1, 12, -5, -6, 50, 3], 4, 12.75),
        ([5], 1, 5.0),
        ([0, 0, 0, 0], 2, 0.0),
        ([4, 2, 1, 3, 3], 2, 3.0),
        ([-1, -12, -5, -6, -50, -3], 3, -6.0),
        ([7, 4, 5, 6, 1], 1, 7.0),
        ([7, 4, 5, 6, 1], 5, 4.6),
    ]

    funcs = [
        Solution.findMaxAverageI,
        Solution.findMaxAverageII,
    ]

    EPS = 1e-5

    for func in funcs:
        for nums, k, expected in test_cases:
            result = func(nums, k)
            assert abs(result - expected) < EPS
