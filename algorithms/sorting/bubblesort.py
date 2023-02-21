"""
Bubble Sort
    - Time Complexity: O(n^2)
"""

from typing import List


def bubbleSort(nums: List[int]):
    """
    First, iterate through the list in reverse order.
    Next, iterate over the index window.
    Within the index window, check if the two neighbor indexes are in order.
    If the neighbor indexes are not in order, reverse them.
    """

    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+ 1]:
                tmp = nums[j]

                nums[j] = nums[j + 1]
                nums[j + 1] = tmp
