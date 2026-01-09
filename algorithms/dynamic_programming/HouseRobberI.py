"""
House Robber
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street.

Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have
security systems connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

Example 2:
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
    * 1 <= nums.length <= 100
    * 0 <= nums[i] <= 400
"""

from typing import List


class HouseRobberI:

    # Algorithm(s) Used: Dynamic Programming (1-D), Bottom-Up, Tabulation
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def robI(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [0, nums[0]]
        for i in range(1, len(nums)):
            two_houses_ago_amount = dp[i - 1] # House CAN be robbed
            one_house_ago_amount = dp[i] # House CANNOT be robbed
            curr_amount = nums[i]

            dp.append(max(two_houses_ago_amount + curr_amount, one_house_ago_amount))

        return dp[-1]


    # Algorithm(s) Used: Dynamic Programming (1-D), Buttom-Up, Fibonacci Sequence
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def robII(self, nums: List[int]) -> int:
        if not nums:
            return 0

        two_houses_ago_amount, one_house_ago_amount = 0, 0
        for curr_amount in nums:
            tmp = two_houses_ago_amount
            two_houses_ago_amount = max(one_house_ago_amount + curr_amount, two_houses_ago_amount) # House CAN be robbed
            one_house_ago_amount = tmp # House CANNOT be robbed

        return two_houses_ago_amount


if __name__ == "__main__":
    solution = HouseRobberI()

    test_cases = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([2, 1, 1, 2], 4),
        ([0], 0),
        ([5], 5),
        ([1, 1, 1, 1], 2),
        ([10, 2, 10, 2, 10], 30),
        ([100, 1, 2, 100], 200),
        ([1, 3, 1], 3),
        ([4, 1, 2, 9, 1, 1, 9], 22),
    ]

    for func in [solution.robI, solution.robII]:
        for nums, expected in test_cases:
            result = func(nums)
            assert result == expected
