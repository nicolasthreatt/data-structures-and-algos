/*
Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
    Input: nums = [1,2,3,1]
    Output: true

Example 2:
    Input: nums = [1,2,3,4]
    Output: false

Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

Constraints:
    * 1 <= nums.length <= 10^5
    * -10^9 <= nums[i] <= 10^9 
*/

package algorithms.arrays;

import java.util.HashSet;
import java.util.Set;

public class ContainsDuplicate {

    // Algorithm(s) Used: Brute Force
    // Time Complexity: O(n^2)
    // Space Complexity: O(1)
    public boolean containsDuplicateI(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (i != j && nums[i] != nums[j])  {
                    return true;
                }
            }
        }

        return false;
    }

    // Algorithm(s) Used: Hash Map
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public boolean containsDuplicateII(int[] nums) {
        Set<Integer> seen = new HashSet<>();

        for (int num : nums) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }

        return false;
    }
}
