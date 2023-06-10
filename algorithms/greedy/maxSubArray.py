"""
https://leetcode.com/problems/maximum-subarray/

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


# Algorithm Used: Greedy, Top-Down
# Time Complexity: O(n)
# Space Complexity: O(1)
def maxSubArray(nums: List[int]) -> int:
    """
    Finds the maximum subarray sum using a greedy approach.

    Args:
        nums: A list of integers representing the input array.

    Returns:
        The maximum sum of a contiguous subarray.

    Explanation:
        The algorithm follows a greedy strategy by making locally optimal choices at each step.
        It maintains two variables: `max_sum` (result) and `current_sum`.
        - `max_sum` keeps track of the maximum sum seen so far.
        - `current_sum` represents the sum of the current subarray being considered.

        The algorithm iterates over each element in the `nums` array and performs the following steps:
        1. Add the current element to the `current_sum` variable.
        2. Update the `max_sum` variable with the maximum value between the current `max_sum` and `current_sum`.
        3. If `current_sum` becomes negative, it means that the sum of the current subarray is negative
           and will not contribute to any future subarray's maximum sum.
           So, it resets `current_sum` to zero, effectively starting a new subarray.

        The greedy choice is to include an element in the subarray as long as the cumulative sum (`current_sum`)
        remains positive. By continuously updating the maximum sum (`max_sum`) and resetting `current_sum` when it
        becomes negative, the algorithm considers all possible subarrays and selects the one with the largest sum.

        This approach works because the maximum subarray sum problem exhibits optimal substructure,
        meaning that the maximum sum of a subarray ending at index `i` can be calculated by considering
        the maximum sum of the subarray ending at index `i-1` and the value of the current element at index `i`.
    """
    # Initialize the maximum sum with the first element
    max_sum = nums[0]

    # Initialize the sum of the current subarray
    current_sum = 0

    # Loop through the input array
    # Add the current element to the current sum and update the maximum sum seen so far
    # Reset the current sum to zero if it becomes negative
    #    - This is because the sum of the current subarray is negative and
    #      will not contribute to any future subarray's maximum sum
    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)

        if current_sum < 0:
            current_sum = 0

    # Return the maximum sum
    return max_sum