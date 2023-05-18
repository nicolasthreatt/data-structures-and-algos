"""
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

Constraints:
    * 1 <= candidates.length <= 100
    * 1 <= candidates[i] <= 50
    * 1 <= target <= 30
"""

from typing import List


# Algorithm Used: Backtracking
# Time Complexity: O(2^target)
# Space Complexity: O(2^target)
def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    # Sort the candidates list
    # This is to avoid duplicate combinations and to make the backtracking easier
    # Time Complexity: O(nlogn)
    candidates.sort()

    # Create a list to store all combinations to be returned
    combinations = []

    def backtrack(cur, pos, target):
        # BASE CASE I (SUCCESS):
        # If the target is 0, then we have found a combination that sums to the target
        if target == 0:
            combinations.append(cur.copy())

        # BASE CASE II (FAILURE):
        # If the target is less than or equal to 0, then the current combination is invalid
        # Return nothing and backtrack
        if target <= 0:
            return

        # Create a variable to store the previous candidate
        # This is to avoid duplicate combinations
        # Initialize it to -1 because the candidates list contains positive integers
        prev = -1

        # Iterate through the candidates list to generate all possible combinations starting from the current position
        # This will treat each candidate as the first element in the combination
        for i in range(pos, len(candidates)):
            # If the current candidate is the same as the previous candidate, skip it
            # This is to avoid duplicate combinations
            if candidates[i] == prev:
                continue

            # RECURSIVE CASE (INCLUDE CURRENT ELEMENT):
            #   - Append the current candidate to the current combination
            #   - Recursively call backtrack() with the current combination, the next index, and the target minus the current candidate
            #      * The next index is used to avoid duplicate combinations
            #   - Pop the current candidate from the current combination
            #       * This is to backtrack so that the current combination is not modified for the next iteration
            combinations.append(candidates[i])
            backtrack(cur, i + 1, target - candidates[i])
            combinations.pop()  # Backtrack

            # Update the previous candidate
            prev = candidates[i]

    # Call the backtrack() helper function to generate all combinations
    backtrack([], 0, target)

    # Return the combinations list
    return combinations
