"""
Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

Example 1:
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5

Example 2:
    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4

Constraints:
    * 1 <= k <= nums.length <= 10^5
    * -10^4 <= nums[i] <= 10^4
"""

import heapq
from typing import List


# Algorithm Used: Quick Select
# Time Complexity: O(n)
# Space Complexity: O(1)
def findKthLargestI(nums: List[int], k: int) -> int:
    # Set the target k to the kth largest element
    # Note that the kth largest element is the (len(nums) - k)th smallest element
    k = len(nums) - k

    def quickSelect(left, right):
        # Set the pivot to the right most element
        pivot = nums[right]

        # Set the partition to the left most element
        p = left

        # Iterate through the array, from the left partition to the right partition
        for i in range(left, right):
            # If the current element is less than or equal to the pivot element
            # swap the current element with the partition element and increment the partition.
            # This is to ensure that all elements less than the pivot are to the left of the partition
            # and all elements greater than the pivot are to the right of the partition.
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1

        # Swap the pivot element with the partition element
        # This is to ensure that the pivot element is in the correct position
        nums[right], nums[p] = nums[p], nums[right]

        # If the partition is greater than the target k, then the target k is in the left partition
        if p > k:
            return quickSelect(left, p - 1)
        # If the partition is less than the target k, then the target k is in the right partition
        elif p < k:
            return quickSelect(p + 1, right)
        # If the partition is equal to the target k, then the target k is the partition element
        else:
            return nums[p]

    # Recursively call quickSelect to find the kth largest element
    return quickSelect(0, len(nums) - 1)


# Algorithm Used: Min Heap
# Time Complexity: O(nlog(k))
# Space Complexity: O(k)
def findKthLargestII(nums: List[int], k: int) -> int:
    heapq.heapify(nums)

    while len(nums) > k:
        heapq.heappop(nums)

    return heapq.heappop(nums)


if __name__ == "__main__":
    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([2, 1], 1, 2),
        ([2, 1], 2, 1),
        ([7, 10, 4, 3, 20, 15], 3, 10),
    ]

    funcs = [findKthLargestI, findKthLargestII]

    for func in funcs:
        for nums, k, expected in test_cases:
            assert func(nums.copy(), k) == expected
