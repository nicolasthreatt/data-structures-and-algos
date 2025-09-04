"""
1827. Minimum Operations to Make the Array Increasing
https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

You are given an integer array nums (0-indexed).
In one operation, you can choose an element of the array and increment it by 1.

For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1.
An array of length 1 is trivially strictly increasing.

Example 1:
    Input: nums = [1,1,1]
    Output: 3
    Explanation: You can do the following operations:
        1) Increment nums[2], so nums becomes [1,1,2].
        2) Increment nums[1], so nums becomes [1,2,2].
        3) Increment nums[2], so nums becomes [1,2,3].

Example 2:
    Input: nums = [1,5,2,4,1]
    Output: 14

Example 3:
    Input: nums = [8]
    Output: 0

Constraints:
    1 <= nums.length <= 5000
    1 <= nums[i] <= 10^4

"""

# Algorithm Used: Greedy, In-Place
# Time Complexity: O(n)
# Space Complexity: O(1)
def minOperationsI(nums: list[int]) -> int:
    operations = 0  # total number of increments needed

    for i in range(1, len(nums)):
        # If current number is less than or equal to previous number,
        # increase it to be exactly one more than the previous number
        if nums[i - 1] >= nums[i]:
            needed = nums[i - 1] - nums[i] + 1
            operations += needed                 # add to operations count
            nums[i] = nums[i - 1] + 1  # update current number by exactly one from the previous number

    return operations


# Algorithm Used: Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)
def minOperationsII(self, nums: List[int]) -> int:
    operations = 0     # total number of increments needed
    last_value = 0     # last value in the adjusted (strictly increasing) sequence

    # Go through each number in the list.
    # If current number is less than or equal to previous,
    # increase previous so it's strictly greater than the previous
    for num in nums:
        # If current number is too small or equal to the last increase it to be strictly greater
        if num <= last_value:
            last_value += 1
            operations += last_value - num  # add the difference to the operation count
        else:
            # If current number is already greater, no operation needed
            last_value = num  # just update last_value

    return operations
