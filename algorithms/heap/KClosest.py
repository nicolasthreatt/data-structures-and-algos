"""
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
"""

import heapq
from typing import List


class KClosest:
    # Algorithm(s) Used: Sorting
    # Time Complexity: O(nlog(n))
    # Space Complexity: O(1)
    def kClosestI(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: (p[0]**2 + p[1]**2) ** 0.5)
        return points[:k]

    # Algorithm(s) Used: Min Heap, Two Passes
    # Time Complexity: O(n + klog(n))
    # Space Complexity: O(n)
    def kClosestII(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_points = []
        min_heap = []  # In Python, heapq always implements a min-heap

        for x, y in points:
            dist = (x**2 + y**2) ** 0.5
            min_heap.append((dist, x, y))  # Add distance, x, and y coords to heap

        heapq.heapify(min_heap)
        while k > 0:
            x, y = heapq.heappop(min_heap)[1:]
            closest_points.append([x, y])
            k -= 1

        return closest_points

    # Algorithm(s) Used: Max Heap, Single Pass
    # Time Complexity: O(nlog(k))
    # Space Complexity: O(k)
    def kClosestIII(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []  # heap of (-dist, x, y)

        for x, y in points:
            dist = (x**2 + y**2) ** 0.5
            heapq.heappush(max_heap, (-dist, x, y))
            if len(max_heap) > k:
                heapq.heappop(max_heap)  # Removes farthest distance

        return [[x, y] for (_, x, y) in max_heap]


if __name__ == "__main__":
    Solution = KClosest()

    test_cases = [
        ([[1, 3], [-2, 2]], 1),
        ([[3, 3], [5, -1], [-2, 4]], 2),
        ([[0, 1], [1, 0]], 1),
        ([[1, 1], [2, 2], [3, 3]], 2),
        ([[5, 5]], 1),
    ]

    funcs = [
        Solution.kClosestI,
        Solution.kClosestII,
        Solution.kClosestIII,
    ]

    for func in funcs:
        for points, k in test_cases:
            result = func(points.copy(), k)
            assert len(result) == k
            for p in result:
                assert p in [[x, y] for x, y in points]
