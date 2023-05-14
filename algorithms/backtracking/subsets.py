"""
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
    * 1 <= nums.length <= 10
    * -10 <= nums[i] <= 10
    * All the numbers of nums are unique.
"""

from typing import List


# Algorithm Used: Backtracking, Recursion
# Time Complexity: O(n * 2^n), where 2^n = number of subsets
# Space Complexity: O(n * 2^n)
def subsets(nums: List[int]) -> List[List[int]]:
    """
    Create a list to store all subsets to be returned.

    2^n = number of subsets
    """
    # Create a list to store all subsets to be returned
    subsets = []

    # Create a list to store the current subset path
    current_subset = []

    def dfs(i: int) -> None:
        """
        Depth-first search (DFS) helper function.
        Recursively generate all subsets.

        Args:
            i (int): The current index of the input array.
        """
        # BASE CASE:
        #   - If the current subset is the same length as the input array,
        #     append the current subset to the subsets list and return.
        if i >= len(nums):  # OUT-OF-BOUNDS CHECK
            subsets.append(current_subset.copy())
            return

        # RECURSIVE CASE I:
        #   - Decision to include the current element in the current subset.
        #   - Append the current element to the current subset.
        #   - Recursively call the helper function to get the rest of the subsets.
        current_subset.append(nums[i])
        dfs(i + i)

        # RECURSIVE CASE II:
        #   - Decision to not include the current element in the current subset.
        #   - Pop the current element from the current subset, which should result in an empty subset.
        #   - Recursively call the helper function to get the rest of the subsets.
        current_subset.pop()
        dfs(i + 1)

    # Call the helper function to generate all subsets
    dfs(0)

    # Return the list of subsets
    return subsets
