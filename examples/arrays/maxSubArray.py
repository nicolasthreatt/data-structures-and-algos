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
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


# Time Complexity: O(n)
def maxSubArray(self, nums: List[int]) -> int:
    # Initially set the max subarray sum to the first element in the list
    maxSub = nums[0]

    # Initialize the current sum to 0
    curSum = 0

    # Loop through list
    for n in nums:
        # Check to see if the current sub array sum is negative, if so reset it back to 0
        if curSum < 0:
            curSum = 0
        
        # Always add the current sum with the current element in list
        curSum += n

        # Update max sum array if current sum is greater
        maxSub = max(maxSub, curSum)

    # Return the maximum sub array sum
    return maxSub


# Kadane's Algorithm
# Time Complexity: O(n)
def maxSubArrayKadane(self, nums: List[int]) -> int:
    # Initialize a max for current sub array and a max for the entire input array
        max_current = max_global = nums[0]

        # Loop through list but skip first element
        for i in range(1, len(nums)):
            # Set the maximum of the current sub array to either the max value 
            # of the current index or the sum of current maximum subarray and current index
            max_current = max(nums[i], max_current + nums[i])

            # If the current max sub array is greater than the global max sub array, update
            # the global value
            if max_current > max_global:
                max_global = max_current

        return max_global
