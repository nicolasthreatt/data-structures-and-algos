"""
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output: [[1,1,2], [1,2,1], [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
    * 1 <= nums.length <= 8
    * -10 <= nums[i] <= 10
"""

from typing import List


# Algorithm Used: Backtracking, Recursion, Hashmap
# Time Complexity: O(n!)
# Space Complexity: O(n!)
def permuteUnique(nums: List[int]) -> List[List[int]]:
    # Create a list to store all permutations to be returned
    permutations = []

    # Create a list to store the current permutation
    perm_path = []

    # Create a hashmap to store the number of occurrences of each element in the input array
    count = {n: 0 for n in nums}
    for n in nums:
        count[n] += 1

    def dfs() -> None:
        # BASE CASE:
        #   - If the current permutation is the same length as the input array,
        #     append the current permutation to the permutations list and return.
        #   - This means that the current permutation path is a valid permutation.
        if len(perm_path) == len(nums):
            # permutations.append(perm_path[:])
            permutations.append(perm_path.copy())
            return

        # Iterate through the keys for hashmap of occurrences of each element in the input array
        for n in count:
            # If the current element has occurrences, append it to the current permutation and recursively call the function.
            if count[n] > 0:
                perm_path.append(n)

                # Decrement the number of occurrences of the current element before each recursive call.
                # This is to ensure that the current element is not added to the current permutation again.
                count[n] -= 1

                # Recursively call the function to get the rest of the permutations
                dfs()

                # BACKTRACKING:
                #   - Increment the number of occurrences of the current element
                #   - Remove the current element from the current permutation
                #   - These are to ensure that the current permutation is not modified for the next recursive call
                count[n] += 1
                perm_path.pop()

    # Call the recursive backtreacking function to get all permutations
    dfs()

    # Return the permutations
    return permutations
