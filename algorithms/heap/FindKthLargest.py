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
    

class FindKthLargest:

    # Algorithm Used: Quick Select
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findKthLargestI(self, nums: List[int], k: int) -> int:
        return self._quickSelect(0, len(nums) - 1)

    def _quickSelect(self, left: int, right: int) -> int:
        return 0  # PLACEHOLDER

    # Algorithm Used: Min Heap
    # Time Complexity: O(nlog(k))
    # Space Complexity: O(k)
    def findKthLargestII(self, nums: List[int], k: int) -> int:
        minHeap = nums.copy()
        heapq.heapify(minHeap)  # In Python, heapq always implements a min-heap

        while len(minHeap) > k:
            heapq.heappop(minHeap)  # Remove smallest elements until only k elements remain

        return heapq.heappop(minHeap)  # TOP of min heap is always the kth largest element


if __name__ == "__main__":
    Solution = FindKthLargest()

    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([2, 1], 1, 2),
        ([2, 1], 2, 1),
        ([7, 10, 4, 3, 20, 15], 3, 10),
    ]

    funcs = [
        # Solution.findKthLargestI,
        Solution.findKthLargestII
    ]

    for func in funcs:
        for nums, k, expected in test_cases:
            assert func(nums.copy(), k) == expected
