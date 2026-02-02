/*
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
*/
package algorithms.heap;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class TopKFrequentElements {

    private static class Pair {
        int freq;
        int num;

        Pair(int freq, int num) {
            this.freq = freq;
            this.num = num;
        }
    }

    // Algorithm(s) Used: Max Heap
    // Time Complexity: O(nlog(k))
    // Space Complexity: O(n)
    public int[] topKFrequentI(int[] nums, int k) {
        Map<Integer, Integer> freqs = new HashMap<>();  // {num: freq}

        for (int num : nums) {
            freqs.put(num, freqs.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<Pair> maxHeap =
            new PriorityQueue<>(
                (a, b) -> Integer.compare(b.freq, a.freq)
            );

        for (Map.Entry<Integer, Integer> entry : freqs.entrySet()) {
            maxHeap.offer(new Pair(entry.getValue(), entry.getKey()));
        }

        int[] result = new int[k];

        for (int i = 0; i < k; i++) {
            result[i] = maxHeap.poll().num;
        }

        return result;
    }

    // Algorithm(s) Used: Min Heap
    // Time Complexity: O(nlog(k))
    // Space Complexity: O(n)
    public int[] topKFrequentII(int[] nums, int k) {
        Map<Integer, Integer> freqs = new HashMap<>();  // {num: freq}

        for (int num : nums) {
            freqs.put(num, freqs.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<Pair> minHeap =
            new PriorityQueue<>((a, b) -> Integer.compare(a.freq, b.freq));

        for (Map.Entry<Integer, Integer> entry : freqs.entrySet()) {
            minHeap.offer(new Pair(entry.getValue(), entry.getKey()));
            if (minHeap.size() > k) {
                minHeap.poll();  // Remove smallest frequency to keep top k
            }
        }

        int[] result = new int[k];
        for (int i = k - 1; i >= 0; i--) {  // Reverse order
            result[i] = minHeap.poll().num;
        }

        return result;
    }   
}
