/*
K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).

You may return the answer in any order.
The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
    Input: points = [[1,3],[-2,2]], k = 1
    Output: [[-2,2]]
    Explanation:
        The distance between (1, 3) and the origin is sqrt(10).
        The distance between (-2, 2) and the origin is sqrt(8).
        Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
        We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
    Input: points = [[3,3],[5,-1],[-2,4]], k = 2
    Output: [[3,3],[-2,4]]
    Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:
    * 1 <= k <= points.length <= 10^4
    * -10^4 < xi, yi < 10^4
*/
package algorithms.heap;

import java.util.Arrays;
import java.util.PriorityQueue;

public class KClosest {

    private int dist(int[] coords) {
        int x = coords[0];
        int y = coords[1];

        return x * x + y * y;
    }

    // Algorithm(s) Used: Sorting
    // Time Complexity: O(nlog(n))
    // Space Complexity: O(1)
    public int[][] kClosestI(int[][] points, int k) {
        Arrays.sort(points, (a, b) -> {
            return Integer.compare(dist(a), dist(b));
        });

        return Arrays.copyOfRange(points, 0, k);
    }

    // Algorithm Used: Min Heap, Two Passes
    // Time Complexity: O(n + klog(n))
    // Space Complexity: O(n)
    public int[][] kClosestII(int[][] points, int k) {
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(
            (a, b) -> Integer.compare(dist(a), dist(b))
        );

        for (int[] p : points) {
            minHeap.offer(p);
        }

        int[][] closestPoints = new int[k][];
        for (int i = 0; i < k; i++) {
            closestPoints[i] = minHeap.poll();  // Retrieves AND removes head of queue
        }

        return closestPoints;
    }

    // Algorithm Used: Max Heap, Single Passes
    // Time Complexity: O(klog(n))
    // Space Complexity: O(k)
    public int[][] kClosestIII(int[][] points, int k) {
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
            (a, b) -> Integer.compare(dist(b), dist(a)) 
        );

        for (int[] p : points) {
            maxHeap.offer(p);
            if (maxHeap.size() > k) {
                maxHeap.poll();  // Removes farthest distance
            }
        }

        int[][] closestPoints = new int[k][];
        for (int i = 0; i < k; i++) {
            closestPoints[i] = maxHeap.poll();  // Retrieves AND removes head of queue
        }

        return closestPoints;
    }   
}
