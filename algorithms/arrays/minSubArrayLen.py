"""
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of positive integers nums and a positive integer target, return
the minimal length of a  subarray whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
    * 1 <= target <= 109
    * 1 <= nums.length <= 105
    * 1 <= nums[i] <= 104
 
Follow up:
    - If you have figured out the O(n) solution, try coding another solution of
      which the time complexity is O(n log(n)).
"""


from typing import List

# Algorithm Used: Sliding Window
# Time Complexity: O(nums)
# Space Complexity: O(1) 
def minSubArrayLen(target: int, nums: List[int]) -> int:
    # Initialize a variable to keep track of the mininum sub array length
    min_window = float('inf')

    # Sliding Window Algorithm:
    # Start left and right indexes at the beginning of array
    # Use right index as primary iterator
    # Find the window where the sum is greater or equal to the target value
    # and adjust the sum and left index
    l = sum = 0
    for r in range(len(nums)):
        sum += nums[r] 

        while sum >= target:
            current_window = r - l + 1
            min_window = min(min_window, current_window)
            sum -= nums[l]
            l += 1

    return 0 if min_window == float('inf') else min_window
