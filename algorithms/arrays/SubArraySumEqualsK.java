/*
Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k,
return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [1,1,1], k = 2
    Output: 2

Example 2:
    Input: nums = [1,2,3], k = 3
    Output: 2

Constraints:
    * 1 <= nums.length <= 2 * 10^4
    * -1000 <= nums[i] <= 1000
    * -10^7 <= k <= 10^7
*/

package algorithms.arrays;

import java.util.HashMap;
import java.util.Map;

public class SubArraySumEqualsK {

    // Algorithm Used: Prefix Sum
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public int subarraySumI(int[] nums, int k) {
        int subarrays = 0;  // Number of subarrays equal to k
        int currSum = 0;    // Current prefix sum

        Map<Integer, Integer> prefixSums = new HashMap<>();  // { sum : # of times sum has appeared }
        prefixSums.put(0, 1);                     // Allows subarrays starting at index 0

        for (int num : nums) {
            // Count current prefix
            currSum += num;

            // If curr_sum - k exists, the current subarray sums must be equal to k
            subarrays += prefixSums.getOrDefault(currSum - k, 0);  // diff = curr_sum - k

            // Update the frequency of the current prefix sum
            prefixSums.put(currSum, prefixSums.getOrDefault(currSum, 0) + 1);
        }

        return subarrays;
    }
}
