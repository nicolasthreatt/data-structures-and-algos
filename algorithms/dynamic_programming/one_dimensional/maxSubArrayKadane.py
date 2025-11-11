"""
https://leetcode.com/problems/maximum-subarray/
https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum 1.

Example 3:
    Input: nums = [5,4,-1,7,8]
    Output: 23
    Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
    * 1 <= nums.length <= 10^5
    * -10^4 <= nums[i] <= 10^4
"""

from typing import List

# Algorithm Used: Dynamic Programming, One-Dimensional, Kadane's Algorithm, Buttom-Up
# Time Complexity: O(n)
# Space Complexity: O(1)
def maxSubArrayKadane(self, nums: List[int]) -> int:
    """
    Finds the maximum subarray sum using Kadane's algorithm.

    Args:
        nums: A list of integers representing the input array.

    Returns:
        The maximum sum of a contiguous subarray.

    Explanation:
        Kadane's algorithm is an efficient approach for finding the maximum subarray sum in an array.
        The algorithm iterates through the array and calculates the maximum sum of subarrays ending at each position.
        At each step, it makes a choice whether to extend the current subarray or start a new one.

        The maximum sum at index `i` is either the value at index `i` itself (starting a new subarray)
        or the sum of the value at index `i` and the maximum sum ending at index `i-1` (extending the current subarray).

        The algorithm maintains two variables: `max_sum` and `current_sum`.
            - `max_sum` keeps track of the overall maximum subarray sum seen so far.
            - `current_sum` represents the maximum sum of a subarray ending at the current position.

        We initialize `max_sum` with negative infinity to handle cases where all the numbers in the array are negative.
        By updating `max_sum` and `current_sum` dynamically as we iterate through the array,
        we can efficiently find the maximum subarray sum.

        Kadane's algorithm has a time complexity of O(n) since it iterates through the input array once.
        It is a more optimized and efficient approach compared to the simple greedy algorithm for finding the maximum subarray sum.
    """

    # Initialize the maximum sum with negative infinity
    # This handles cases where all the numbers in the array are negative
    max_sum = float('-inf')

    # Initialize the sum of the current subarray
    # This represents the maximum sum of a subarray ending at the current position
    current_sum = 0

    # Loop through the input array
    # Update the current sum and maximum sum seen during each iteration
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    # Return the maximum sum
    return max_sum