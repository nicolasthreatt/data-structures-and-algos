/*
Maximize Sum Of Array After K Negations
https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/

Given an integer array nums and an integer k, modify the array in the following way:
    - Choose an index i and replace nums[i] with -nums[i].

You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.

Example 1:
    Input: nums = [4,2,3], k = 1
    Output: 5
    Explanation: Choose index 1 and nums becomes [4,-2,3].

Example 2:
    Input: nums = [3,-1,0,2], k = 3
    Output: 6
    Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].

Example 3:
    Input: nums = [2,-3,-1,5,-4], k = 2
    Output: 13
    Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].

Constraints:
    * 1 <= nums.length <= 10^4
    * -100 <= nums[i] <= 100
    * 1 <= k <= 10^4
*/

package algorithms.greedy;

import java.util.Arrays;

public class MaxSumAfterKNegations {

    // Algorithm(s) Used: Greedy, Sorting
    // Time Complexity: O(n*log(n))
    // Space Complexity: O(1)
    public int largestSumAfterKNegationsI(int[] nums, int k) {
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            // Greedy Choice - Flip negatives to increase sum
            if (nums[i] < 0 && k > 0) {
                nums[i] = -nums[i];
                k -= 1;
            }
        }

        // If k is still odd, flip smallest absolute value
        // Represents the remaining k flips since any index can be chosen multiple times
        if (k % 2 == 1) {
            Arrays.sort(nums);
            nums[0] = -nums[0];
        }

        int solution = 0;
        for (int num : nums) {
            solution += num;
        }

        // Global Solution - Max sum possible
        return solution;
    }
    
}
