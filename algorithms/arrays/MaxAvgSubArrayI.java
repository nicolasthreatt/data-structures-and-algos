/*
Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/

You are given an integer array nums consisting of n elements,
and an integer k.

Find a contiguous subarray whose length is equal to k
that has the maximum average value and return this value.

Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
    - Input: nums = [1,12,-5,-6,50,3], k = 4
    - Output: 12.75000
              Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
    - Input: nums = [5], k = 1
    - Output: 5.00000

Constraints:
    * n == nums.length
    * 1 <= k <= n <= 10^5
    * -10^4 <= nums[i] <= 10^4
*/

package algorithms.arrays;

public class MaxAvgSubArrayI {

    // Algorithm(s) Used: Sliding Window, Two Pointers
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public double findMaxAverageI(int[] nums, int k) {
        double max_sum = Double.NEGATIVE_INFINITY;
        double window_sum = 0.0;

        int left = 0;
        for (int right = 0; right < nums.length; ++right) {
            window_sum += nums[right];

            int window_length = right - left + 1;
            if (window_length == k) {
                max_sum = Math.max(max_sum, window_sum);
                window_sum -= nums[left];
                left++;
            }
        }

        return max_sum / k;
    }

    // Algorithm(s) Used: Fixed Sliding Window
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public double findMaxAverageII(int[] nums, int k) {
        double windowSum = 0;
        for (int i = 0; i < k; i++) {
            windowSum += nums[i];
        }

        double maxSum = windowSum;

        for (int i = k; i < nums.length; i++) {
            windowSum += nums[i] - nums[i - k];
            maxSum = Math.max(maxSum, windowSum);
        }

        return maxSum / k;
    }
}
