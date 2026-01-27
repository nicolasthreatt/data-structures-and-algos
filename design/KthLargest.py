"""
Kth Largest Element in a Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
    * KthLargest(int k, int[] nums)
        - Initializes the object with the integer k and the stream of integers nums.
    * int add(int val)
        - Appends the integer val to the stream and
          returns the element representing the kth largest element in the stream.

Input
    - ["KthLargest", "add", "add", "add", "add", "add"]
    - [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

Output
    - [null, 4, 5, 5, 8, 8]
    
Explanation
    - KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
    - kthLargest.add(3);   // return 4
    - kthLargest.add(5);   // return 5
    - kthLargest.add(10);  // return 5
    - kthLargest.add(9);   // return 8
    - kthLargest.add(4);   // return 8

Constraints:
    * 1 <= k <= 10^4
    * 0 <= nums.length <= 10^4
    * -10^4 <= nums[i] <= 10^4
    * -10^4 <= val <= 10^4
    * At most 10^4 calls will be made to add.
    * Guaranteed that there will be at least k elements in the array when search for kth element.
"""

import heapq
from typing import List


# Algorithm(s) Used: Min Heap
# Time Complexity: O(log(k))
# Space Complexity: O(k)
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums

        heapq.heapify(self.minHeap)   # In Python, heapq always implements a min-heap
        while len(self.minHeap) > k:  # Remove smallest elements until only k elements remain
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)  # Remove TOP of min heap if more than k elements

        return self.minHeap[0]           # TOP of min heap is always the kth largest element


if __name__ == "__main__":
    Solution = KthLargest(3, [4, 5, 8, 2])

    assert Solution.add(3) == 4
    assert Solution.add(5) == 5
    assert Solution.add(10) == 5
    assert Solution.add(9) == 8
    assert Solution.add(4) == 8
