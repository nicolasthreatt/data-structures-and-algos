"""
Container With Most Water
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n.

There are n vertical lines drawn
such that two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis that forms a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

You may not slant the container.

Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49

Example 2:
    Input: height = [1,1]
    Output: 1

Constraints:
    * n == height.length
    * 2 <= n <= 10^5
    * 0 <= height[i] <= 10^4
"""

from typing import List


# Algorithm(s) Used: Brute Force, Nested Iteration
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def maxAreaI(height: List[int]) -> int:
    max_area = 0

    for l in range(len(height)):
        for r in range(l + 1, len(height)):
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)

    return max_area


# Algorithm(s) Used: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
def maxAreaII(height: List[int]) -> int:
        max_area = 0

        # Start pointers at both ends to consider the maximum area possible
        l, r = 0, len(height) - 1

        while l < r:
            # Compute area and find max for each iteration
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)

            # Move the pointer with the smaller height to try and find a larger area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area


if __name__ == "__main__":
    test_cases = [
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1,1], 1),
        ([4,3,2,1,4], 16),
        ([1,2,1], 2),
        ([1,2,4,3], 4),
        ([1,3,2,5,25,24,5], 24),
    ]

    for func in [maxAreaI, maxAreaII]:
        for heights, expected_area in test_cases:
            result = func(heights)
            assert result == expected_area
