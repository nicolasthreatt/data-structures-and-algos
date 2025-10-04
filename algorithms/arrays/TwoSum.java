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
 