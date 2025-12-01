/*
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
*/
package algorithms.arrays;

public class ContainerWithMostWater {

    // Algorithm(s) Used: Brute Force, Nested Iteration
    // Time Complexity: O(n^2)
    // Space Complexity: O(1)
    public int maxAreaI(int[] height) {
        int max_area_container = 0;

        for (int l = 0; l < height.length; l++) {
            for (int r = l + 1; r < height.length; r++) {
                int area = Math.min(height[l], height[r]) * (r - l);
                max_area_container = Math.max(max_area_container, area);
            }
        }

        return max_area_container;
    }

    // Algorithm(s) Used: Two Pointers
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public int maxAreaII(int[] height) {
        int max_area_container = 0;

        int l = 0, r = height.length - 1;
        while (l < r) {
            int area = Math.min(height[l], height[r]) * (r - l);
            max_area_container = Math.max(max_area_container, area);

            if (height[l] < height[r]) {
                l += 1;
            } else {
                r -= 1;
            }
        }

        return max_area_container;
    }
}
