"""
https://leetcode.com/problems/frequency-of-the-most-frequent-element/

The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k.
In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

Example 1:
Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element
two times to make nums = [4,4,4].
4 has a frequency of 3.

Example 2:
Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

Example 3:
Input: nums = [3,9,6], k = 2
Output: 1
 
Constraints:
    1 <= nums.length <= 105
    1 <= nums[i] <= 105
    1 <= k <= 105
"""

from typing import List


# Algorithm Used: Sorting, Sliding Window
# Time Complexity: O(k*log(k))
# Space Complexity: O(1)
def maxFrequency(nums: List[int], k: int) -> int:
    # Intialize a variable to store results
    res = 0

    # Sort Input Array
    nums.sort()

    # Sliding Window Algorithm
    l = r = 0
    window_total_sum = 0

    # Use right index as primary iterator of list
    while r < len(nums):
        # Count the total sum of the elements within the window
        window_total_sum += nums[r]

        # Mutiply the value in the right index by the length of the current window, to get
        # the total sum if the right index was the max frequent element, and then see if its 
        # greater or less than the total sum of the elmements within the window plus k.
        # current_window_length = r - l + 1
        while nums[r] * (r - l + 1) > (window_total_sum + k):
            window_total_sum -= nums[l]
            l += 1
        
        # Update the maximum frequeny which is the length of the current window
        res = max(res, (r - l + 1))
        r += 1

    return res
