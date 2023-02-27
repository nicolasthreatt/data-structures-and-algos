"""
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return
the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
    * 0 <= nums.length <= 105
    * -109 <= nums[i] <= 109
"""

from typing import List


# Time Complexity: O(n)
# Memory Complexity: O(n)
def longestConsecutive(self, nums: List[int]) -> int:

    # Create a set of the input elements to later use as a lookup
    numsSet = set(nums)

    # Initialize the current longest sequence as 0
    longestSeq = 0

    # Iterate through the input list
    for n in nums:
        # Check if n is start of a sequence
        if (n - 1) not in numsSet:
            length = 0

            # Iterating through numsSet to keep count of the 
            # sequence length until the its no longer valid
            while (n + length) in numsSet:
                length += 1

            # Update Longest Sequence
            longestSeq = max(longestSeq, length)

    return longestSeq
