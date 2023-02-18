"""
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
    * n == height.length
    * 2 <= n <= 105
    * 0 <= height[i] <= 104
"""

from typing import List


# Algorithm Used: Two Pointers
# Time Complexity: O(n)
def maxArea(height: List[int]) -> int:
    # Initialize the result varaible to 0
    res = 0

    # Create a left and right pointers for Two Pointer Technique
    l, r = 0, len(height) - 1

    # Iterate through list
    while l < r:
        # Compute area and find max for each iteration
        area = (r - l) * min(height[l], height[r])

        res = max(res, area)

        # IF the height of the left pointer is less than the height of the right pointer,
        # then incremement the left pointer
        # ELSE incremement the right pointer (when right height is greater than left height)
        # These ensure in the next iteration of the area will be the largest possible
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    # Return result
    return res


# Time Complexity: O(n^2)
def maxArea_BruteForce(self, height: List[int]) -> int:
    res = 0

    for l in range(len(height)):
        for r in range(l + 1, len(height)):
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
    return res
