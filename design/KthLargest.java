/*
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
*/
package design;

import java.util.PriorityQueue;

public class KthLargest {
    private int k;
    private PriorityQueue<Integer> minHeap;
    // PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

    // Algorithm(s) Used: Min Heap
    // Time Complexity: O(klog(k))
    // Space Complexity: O(k)
    public KthLargest(int k, int[] nums) {
        this.k = k;
        minHeap = new PriorityQueue<>(k);

        for (int num : nums) add(num);  // Iterate through "stream"
    }

    // Algorithm(s) Used: Min Heap
    // Time Complexity: O(log(k))
    // Space Complexity: O(k)
    public int add(int val) {
        minHeap.add(val);      // Add new value to heap

        if (minHeap.size() > k) {
            minHeap.poll();    // If heap became too large, remove top/smallest element
        }

        return minHeap.peek(); // NOTE: peek() = Only Retrieves head of queue
    }
}
