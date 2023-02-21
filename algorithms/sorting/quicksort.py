""""
Quicksort
    - Divide-and-conqer algorithm
        + Sets a pivot point to partition a data set (usually last or random)
        + High and low index nums are then used to rearrange data nums
          that are on the "wrong" side of the pivot point
    - Uses recursion to operate on datasets
    - Time Complexity: O(nlog(n))
    - Worst case is O(n^2) when data is mostly sorted already
    - Memory Complexity: O(1)
"""

from typing import List


def quicksort(nums: List[int], first: int, last: int):
    if first < last:
        # Determine pivot index of the input list
        pivotIdx = partition(nums, first, last)

        # Sort the two partitions: left side and right side
        # Rememeber, quicksort is a recursive function
        quicksort(nums, first, pivotIdx - 1)
        quicksort(nums, pivotIdx + 1, last)


def partition(nums: List[int], first: int, last: int):
    # Choose the last item as the pivot point
    pivotvalue = nums[last]

    # Create a lower and upper bound indexes
    l = first
    r = last - 1 # NOTE: pivot value is at last index

    # Start searching for the crossing point
    while l < r:
        # Advanced the left index until it reaches the pivot
        while l < last and nums[l] < pivotvalue:
            l += 1
        # Advanced the right index until it reaches the pivot
        while r > first and nums[r] >= pivotvalue:
            r -= 1

        # If the two indexes cross, then found the crossing point.
        # A cross occurs when the lower bound is greater than the upper
        # Notice, here a crossing point was not yet found.
        # Thus, we must swap the valus and continue to search for pivot (l > r).
        if l < r:
            # nums[l], nums[r] = nums[r], nums[l]
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp

    # When crossing point found, exchange position with the element at
    # the last index with the pivot position index
    # NOTE: Since the pivot position was set as the last position, we
    # use the value of 'l' when it was greater than 'r'
    if nums[l] > pivotvalue:
        # nums[l], nums[last] = nums[last], nums[l]
        tmp = nums[last]
        nums[last] = nums[l]
        nums[l] = tmp

    # Recall, from above the crossing point was found at
    # the lower index which caused  the loop to be exited (l > r)
    return l
