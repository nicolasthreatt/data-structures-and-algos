"""
Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Example 2:
    Input: nums = [1], k = 1
    Output: [1]
 
Constraints:
    * 1 <= nums.length <= 10^5
    * -10^4 <= nums[i] <= 10^4
    * k is in the range [1, the number of unique elements in the array].
    * It is guaranteed that the answer is unique.

Follow up:
    * Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

import heapq

from collections import Counter
from typing import List


class TopKFrequentElements:

    # Algorithm(s) Used: Max Heap
    # Time Complexity: O(n + klog(n))
    # Space Complexity: O(n)
    def topKFrequentI(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        max_heap = [(-count, num) for num, count in freq.items()]  # O(n)
        heapq.heapify(max_heap)  # O(log(n)))

        return [heapq.heappop(max_heap)[1] for _ in range(k)]      # O(klog(n))

    # Algorithm(s) Used: Max Heap
    # Time Complexity: O(nlog(k))
    # Space Complexity: O(n)
    def topKFrequentII(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        max_heap = []

        for num, count in freq.items():
            heapq.heappush(max_heap, (count, num))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [num for _, num in max_heap]

    # Algorithm(s) Used: Bucket Sort
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def topKFrequentIII(self, nums: List[int], k: int) -> List[int]:
        pass


if __name__ == "__main__":
    Solution = TopKFrequentElements()

    test_cases = [
        # (nums, k, expected_set)
        ([1, 1, 1, 2, 2, 3], 2, {1, 2}),
        ([1], 1, {1}),
        ([4, 4, 4, 5, 5, 6], 2, {4, 5}),
        ([7, 7, 8, 8, 9], 1, {7, 8}),
        ([10, 10, 10, 20, 20, 30], 3, {10, 20, 30}),
        ([-1, -1, -2, -2, -2, 3], 2, {-2, -1}),
    ]

    funcs = [
        Solution.topKFrequentI,
        Solution.topKFrequentII,
        # Solution.topKFrequentIII,
    ]

    for func in funcs:
        for nums, k, expected in test_cases:
            result = func(nums.copy(), k)

            assert len(result) == k
            for num in result:
                assert num in expected
