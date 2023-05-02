"""
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
"""

import heapq
from typing import List


# Algorithm Used: Min Heap
# Time Complexity: O(klog(n)) where n is the number of points and k is the number of closest points to return
# Space Complexity: O(k)
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    # Create a min heap to store the k closest points
    # Note the heap is a list but will be heapified using heapq.heapify()
    minHeap = []

    # Iterate through the points and calculate the distance from the origin
    # Append the distance, x, and y coordinates to the heap list
    # Time Complexity: O(n), where n is the number of points
    for x, y in points:
        dist = (x**2 + y**2) ** 0.5
        minHeap.append([dist, x, y])

    # Heapify the heap list to create a min heap
    # Time Complexity: O(n), where n is the number of points
    heapq.heapify(minHeap)

    # Initialize an empty list to store the k closest points
    closest_points = []

    # Iterate through the heap list and pop the k closest points
    # Time Complexity: O(klog(n)), where n is the number of points and k is the number of closest points to return
    while k > 0:
        # dist, x, y = heapq.heappop(minHeap)
        closest_points.append(heapq.heappop(minHeap)[1:])
        k -= 1

    # Return the k closest points
    return closest_points
