"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 
Constraints:
    * 2 <= numbers.length <= 3 * 104
    * -1000 <= numbers[i] <= 1000
    * numbers is sorted in non-decreasing order.
    * -1000 <= target <= 1000
"""

from typing import List


# Algorithm Used: Two Pointers
# Time Complexity: O(n)
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # When using the Two Pointer technique there must be
    # left and right pointers, where left starts at 0 and 
    # right start at the end of the array
    l, r = 0, len(numbers) - 1

    # Iterate through array/list while l is less than r.
    # This ensures no overlaps when iterating.
    while l < r:
        # Compute the current sum of the two pointers
        curSum = numbers[l] + numbers[r]

        # If the current sum is GREATER than the target value, 
        # then we know to SEARCH LEFT since the array is sorted
        if curSum > target:
            r -= 1
        # If the current sum is LESS than the target value, 
        # then we know to SEARCH RIGHT since the array is sorted
        elif curSum < target:
            l += 1
        
        # Return the indexes for the proper sum
        else:
            return[l + 1, r + 1]

