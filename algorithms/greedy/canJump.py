"""
https://leetcode.com/problems/jump-game/

You are given an integer array nums.
You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what.
                 Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
    * 1 <= nums.length <= 10^4
    * 0 <= nums[i] <= 10^5
"""

from typing import List


# Algorithm Used: Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)
def canJump(nums: List[int]) -> bool:
    """
    Greedy algorithm to check if it is possible to reach the last index from the start.

    The algorithm is considered greedy because it makes the locally optimal choice
    at each step by selecting the position that allows us to jump the furthest towards the target.
    By iteratively updating the target position, it gradually moves closer to the start of the list,
    determining if it is possible to reach the last index.

    Args:
        nums: A list of integers representing the input array.

    Returns:
        True if it is possible to reach the last index from the start, False otherwise.
    """

    # Set the initial target position to the last index of the list
    # NOTE: After each iteration, the target position will be updated to the current position 'i'
    target = len(nums) - 1 

    # Iterate backwards through the list starting from the second-to-last element
    for i in range(len(nums) - 2, -1, -1):
        # Check if the current position 'i' plus the maximum jump length from 'i' is greater than or equal to the target
        # If so, then it is possible to reach the target from the current position 'i' so update the target to 'i'
        if i + nums[i] >= target:
            target = i 

    # If the final target position is 0, it means it is possible to reach the last index from the start
    return target == 0