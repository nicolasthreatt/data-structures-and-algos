/*
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:
    * 2 <= nums.length <= 10^4
    * -10^9 <= nums[i] <= 10^9
    * -10^9 <= target <= 10^9
    * Only one valid answer exists.

Follow-up:
    Can you come up with an algorithm that is less than O(n2) time complexity?
*/
package algorithms.arrays;

import java.util.HashMap;

class TwoSum {

    // Algorithm Used: Iteration
    // Time Complexity: O(n^2)
    // Space Complexity: O(1)
    public int[] twoSumI(int[] nums, int target) {
 
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] { i, j };
                }
            }
        }

        return new int[] {};
    }

    // Algorithm Used: Hash Map
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public int[] twoSumII(int[] nums, int target) {
 
        HashMap<Integer, Integer> differences = new HashMap<>();  // number -> index
 
        for (int i = 0; i < nums.length; i++) {
 
            if (differences.containsKey(target - nums[i])) {
                return new int[] { differences.get(target - nums[i]), i };
            } else {
                differences.put(nums[i], i);
            }
        }

        return new int[] {};
    }
}
 