"""
https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that
sum up to target is less than 150 combinations for the given input.

Example 1:
    Input:
        candidates = [2,3,6,7], target = 7
    Output:
        [[2,2,3],[7]]
    Explanation:
        2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
        7 is a candidate, and 7 = 7.
        These are the only two combinations.

Example 2:
    Input:
        candidates = [2,3,5], target = 8
    Output:
        [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
    Input:
        candidates = [2], target = 1
    Output:
        []

Constraints:
* 1 <= candidates.length <= 30
* 2 <= candidates[i] <= 40
* All elements of candidates are distinct.
* 1 <= target <= 40
"""

from typing import List


# Algorithm Used: Backtracking
# Time Complexity: O(2^target)
# Space Complexity: O(2^target)
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    # Create a list to store all combinations to be returned
    combinations = []

    def backtrack(i: int, current: int, total: int) -> None:
        """Backtracking helper function. Recursively generate all combinations.

        Args:
            i (int): The current index of the input array.
            current (int): The current combination.
            total (int): The current sum of the current combination.
        """
        # BASE CASE I (SUCCESS):
        #   - If the current combination total is equal to the target,
        #     append the current combination to the combinations list and return.
        if total == target:
            combinations.append(current.copy())
            return

        # BASE CASE II (FAILURE):
        #   - If if the index is out-of-bounds or the current combination total is greater than the target, return.
        #     This is because the current combination is invalid.
        if i >= len(candidates) or total > target:
            return

        # RECURSIVE CASE I (INCLUDE CURRENT ELEMENT):
        #   - Decision to include the current element in the current combination.
        #   - Append the current element to the current combination.
        #   - Recursively call the helper function to get the rest of the combinations.
        current.append(candidates[i])
        backtrack(i, current, total + candidates[i])

        # RECURSIVE CASE II (EXCLUDE CURRENT ELEMENT):
        #   - Decision to exclude the current element in the current combination.
        #   - Pop the current element from the current combination.
        #   - Recursively call the helper function to get the rest of the combinations.
        current.pop()  # BACKTRACKING - Remove the current element from the current combination
        backtrack(i + 1, current, total)

    # Call the helper function to get all combinations
    backtrack(0, [], 0)

    # Return all combinations
    return combinations
