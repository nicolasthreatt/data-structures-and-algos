"""
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


# Algorithm Used: Dynamic Programming, One-Dimensional, Fibonacci Sequence, Buttom-Up
# Time Complexity: O(n)
# Space Complexity: O(1)
def robI(nums: List[int]) -> int:
    # Create two variables to keep track of the maximum amount of money robbed
    #  - rob1: Two houses ago robbed, so current house can be robbed
    #  - rob2: Last house was robbed, so current house cannot be robbed.
    #          Will act as the current max value.
    # NOTE: Only need to keep track of two values since we are only considering the previous two houses.
    rob1, rob2 = 0, 0

    # Iterate through the list of houses
    for n in nums:
        # new_house_robbed is used to store the max value between the two options.
        # This is because rob1 and rob2 are updated in the next line.
        # If we update rob1 and rob2 before storing the max value, then we will lose the previous rob1 and rob2 values.
        # n + rob1: The current house is robbed, so add the current house's money to the previous rob1 value.
        #           This means there is a gap between the current house and the previous house.
        # rob2: The current house is not robbed, so use the previous rob2 value
        #       This means there is no gap between the current house and the previous house.  (Includes previous house)
        steal = n + rob1
        skip = rob2
        new_house_robbed = max(steal, skip)  # [rob1, rob2, n, n+1, ..]

        # Update rob1 and rob2

        # Recall that rob1 is two houses ago, so it only cares about
        # the previous rob2 value which was the last house robbed.
        rob1 = rob2

        # Recall that rob2 is the last house robbed, so it only cares about
        # the previous new_house_robbed value which is the max value between the current house.
        rob2 = new_house_robbed

    # Return rob2 since it contains the max value between the two options.
    # rob1 is not returned since it is two houses ago, so it does not contain the max value.
    return rob2
