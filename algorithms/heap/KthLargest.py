"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
    * KthLargest(int k, int[] nums)
        - Initializes the object with the integer k and the stream of integers nums.
    * int add(int val)
        - Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Example 1:
    * Input
        - ["KthLargest", "add", "add", "add", "add", "add"]
        - [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    * Output
        - [null, 4, 5, 5, 8, 8]
    * Explanation
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
    * It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""

import heapq
from typing import List


# Algorithm Used: Min Heap of size k
class KthLargest:
    """KthLargest class which represents the kth largest element in a stream using a min heap.

    Attributes:
        minHeap: A min heap of size k.
        k: An integer representing the kth largest element to be searched.

    Args:
        k: An integer representing the kth largest element to be searched.
        nums: A list of integers representing the input array.
    """

    def __init__(self, k: int, nums: List[int]):
        """Initializes the attributes for KthLargest class.

        Time Complexity:
            O(klog(k))

        Space Complexity:
            O(k)
        """

        # Create a min heap for the input array
        self.minHeap = nums
        heapq.heapify(self.minHeap)

        # Record the kth largest element to be searched
        self.k = k

        # Remove the smallest elements from the min heap until the size of the min heap is k
        # This will leave the k largest elements in the min heap and the kth largest element at the top of the min heap
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        """Adds a value to the min heap and returns the kth largest element.

        Args:
            val: An integer representing the value to be added to the min heap.

        Returns:
            An integer representing the kth largest element in the min heap.

        Time Complexity:
            O(log(k))

        Space Complexity:
            O(k)
        """
        # Add the value to the min heap, regardless if the value is smaller or larger than the smallest element in the min heap
        heapq.heappush(self.minHeap, val)

        # Pop the smallest value from the heap if the size of the heap is greater than k
        # This will ensure that the size of the min heap is always k and the kth largest element is always at the top of the min heap
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # Return the kth largest element in the min heap
        # This will always be the top element in the min heap
        return self.minHeap[0]
