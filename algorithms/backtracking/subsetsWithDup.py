"""
https://leetcode.com/problems/subsets-ii/

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
    * 1 <= nums.length <= 10
    * -10 <= nums[i] <= 10
"""

from typing import List


# Algorithm Used: Backtracking, Recursion
# Time Complexity: O(n * 2^n), where 2^n = number of subsets
# Space Complexity: O(n * 2^n)
def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    subsets = []

    # Sort the input array.
    # This is to avoid duplicate subsets and to make the backtracking easier.
    nums.sort()

    def backtrack(i, curr_subset):
        # BASE CASE:
        #   - If the current subset is the same length as the input array,
        #     append the current subset to the subsets list and return.
        if i >= len(nums):  # OUT-OF-BOUNDS CHECK
            subsets.append(curr_subset[::])
            return

        # RECURSIVE CASE I (INCLUDE CURRENT ELEMENT):
        #   - Decision to include the current element in the current subset.
        #   - Append the current element to the current subset.
        #   - Recursively call the helper function to get the rest of the subsets.
        curr_subset.append(nums[i])
        backtrack(i + 1, curr_subset)

        # Remove the current element from the current subset.
        # This is to ensure that the current element is not added to the current subset again.
        curr_subset.pop()  # BACKTRACK

        # RECURSIVE CASE II (EXCLUDE CURRENT ELEMENT):
        #   - Decision to exclude the current element in the current subset.
        #   - Skip over all duplicate elements.
        #   - Recursively call the helper function to get the rest of the subsets.
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        backtrack(i + 1, curr_subset)

    # Call the helper function to get all subsets
    backtrack(0, [])

    # Return the subsets list
    return subsets
