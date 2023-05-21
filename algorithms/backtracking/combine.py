"""
https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

Constraints:
    * 1 <= n <= 20
    * 1 <= k <= n
"""

from typing import List


# Algorithm Used: Backtracking
# Time Complexity: O(k*n^k)
# Space Complexity: O(n^k)
def combine(n: int, k: int) -> List[List[int]]:
    # Create a list to store all combinations to be returned
    combinations = []

    def backtrack(start: int, current_combiniation: List[int]) -> None:
        # BASE CASE:
        #   - If the current combination is of length k,
        #     append a copy of the current combination to the combinations list.
        #   - This means that the current combination is a valid combination.
        if len(current_combiniation) == k:
            combinations.append(current_combiniation.copy())
            return

        # Iterate through the range of numbers from the start to n
        # n + 1 is used because the range function is exclusive of the stop index
        for i in range(start, n + 1):
            # Append the current number to the current combination
            current_combiniation.append(i)

            # RECURSIVE CASE:
            #   - Recursively call the function to get the rest of the combinations
            #   - NOTE: The start index is incremented by 1 to ensure that the
            #           current number is not added to the current combination again.
            backtrack(i + 1, current_combiniation)

            # Remove the current number from the current combination before the next recursive call.
            # This is to ensure that the current number is not added to the current combination again.
            current_combiniation.pop()  # BACKTRACK

    # Call the helper function to get all combinations
    # NOTE: From problem statement the start index is 1 because the numbers start from 1.
    backtrack(1, [])

    # Return the combinations list
    return combinations
