package algorithms.arrays;
/*
3Sum
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
        * nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0
        * nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0
        * nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0
        * The distinct triplets are [-1,0,1] and [-1,-1,2]

Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.

Constraints:
    * 3 <= nums.length <= 3000
    * -10^5 <= nums[i] <= 10^5
*/
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum {

    // Algorithm(s) Used: Binary Search, Sort
    // Time Complexity: O(nlog(n)) + O(n^2) = O(n^2)
    // Space Complexity: O(n)
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;
        List<List<Integer>> triplets = new ArrayList<>();

        Arrays.sort(nums);  // Time Complexity; O(log(n))

        for (int i = 0; i < n; i++) {
            if (i > 0 && nums[i - 1] == nums[i]) continue;  // Skip duplicates

            // Perform Binary Search
            int j = i + 1, k = n - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum > 0) {
                    k -= 1;
                } else if (sum < 0) {
                    j += 1;
                } else {
                    List<Integer> triplet = new ArrayList<>(3);
                    triplet.add(nums[i]);
                    triplet.add(nums[j]);
                    triplet.add(nums[k]);

                    triplets.add(triplet);

                    j += 1;
                    while (j < k && nums[j] == nums[j + 1]) { j += 1; }  // Skip duplicates
                }
            }
        }

        return triplets;
    }
}
