"""
https://leetcode.com/problems/find-the-duplicate-number/

Given an array of integers nums containing n + 1 integers where each
integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Constraints:
    * 1 <= n <= 105
    * nums.length == n + 1
    * 1 <= nums[i] <= n
    * All the integers in nums appear only once except for precisely one integer which appears two or more times.
    
Follow up:
    * How can we prove that at least one duplicate number must exist in nums?
    * Can you solve the problem in linear runtime complexity?
"""


from typing import List


# Algorithm Used: Hash Set
# Time Complexity: O(n)
# Memory Complexity: O(n)
def findDuplicateI(nums: List[int]) -> int:
    pass


# Algorithm Used: Linked List Cycle, Floyd's Tortoise & Hare
# Time Complexity: O(n)
# Memory Complexity: O(1)
def findDuplicateII(nums: List[int]) -> int:
    slow, fast = 0, 0

    # Iterate through input array until an intersection/cycle is found.
    # Update the slow pointer one position and fast pointer two positions
    # after each iteration
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    # Initialize another slow pointer
    # Iterate through input list again and find intersection between the two slow pointers.
    # This intersect position will be the repeated number position
    # Update the slow pointers one position each after each iteration
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]

        if slow == slow2:
            return slow
