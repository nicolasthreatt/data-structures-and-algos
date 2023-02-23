"""
Recursively sum the elements of a lista
"""

from typing import List


def listSum(nums: List[int]) -> int:
    # Base Case
    if len(nums) == 0:
        return 0

    # Move towards base case
    # Recursive Case
    return nums.pop() + listSum(nums)
