"""
https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
    * 1 <= nums.length <= 6
    * -10 <= nums[i] <= 10
    * All the integers of nums are unique.
"""

from typing import List


# Algorithm Used: Backtracking
# Time Complexity: O(n!)
# Space Complexity: O(n!)
def permute(nums: List[int]) -> List[List[int]]:
    # Create a list to store all permutations to be returned
    permutations = []

    # BASE CASE: If the input array only has one element, return that element as a nested list.
    if len(nums) == 1:
        return [nums[:]]

    # Iterate through the input array for each recursive call
    for i in range(len(nums)):
        # Remove the first element from the input array.
        # This will act as the current element to get the rest of the permutations.
        n = nums.pop(0)

        # Recursively call the function on the remaining elements in the input array.
        # This will return all permutations of the remaining elements in the input array.
        perms = permute(nums)

        # For each permutation, append the current element to the end of the permutation.
        for perm in perms:
            perm.append(n)

        # Extend the permutations list with the permutations of the remaining elements in the input array.
        # This will add the permutations of the remaining elements in the input array to the permutations list.
        permutations.extend(perms)

        # Append the current element back to the input array.
        # This is to ensure that the input array is not modified for the next recursive call.
        nums.append(n)

    # After all recursive calls, return the permutations list.
    return permutations
