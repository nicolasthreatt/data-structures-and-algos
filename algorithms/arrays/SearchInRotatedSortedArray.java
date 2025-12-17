/*
Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an
unknown pivot index k (1 <= k < nums.length) such that the resulting array is
    [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

Example 3:
    Input: nums = [1], target = 0
    Output: -1

Constraints:
    * 1 <= nums.length <= 5000
    * -10^4 <= nums[i] <= 10^4
    * All values of nums are unique.
    * nums is an ascending array that is possibly rotated.
    * -10^4 <= target <= 10^4
*/
package algorithms.arrays;

public class SearchInRotatedSortedArray {

    // Algorithm(s) Used: Binary Search
    // Time Complexity: O(log(n))
    // Space Complexity: O(1)
    public int searchI(int[] nums, int target) {
        int l = 0, r = nums.length - 1;

        // Perform Binary Search
        while (l <= r) {
            int m = (l + r) / 2;

            // Found Target
            if (nums[m] == target) {
                return m;
            }

            // Left Half Sorted - [4,5,6,7,0,1,2]
            if (nums[l] <= nums[m]) {
                if (nums[m] < target || nums[l] > target) {  // Target is SMALLER than SMALLEST value in LEFT half
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }

            // Right Half Sorted - [6,7,0,1,2,3,4]
            else {
                if (nums[m] > target || nums[r] < target) {  // Target is LARGER than LARGEST value in RIGHT half
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            }
        }

        return -1;
    }

    // Algorithm(s) Used: Binary Search
    // Time Complexity: O(log(n))
    // Space Complexity: O(1)
    public int searchII(int[] nums, int target) {
        int l = 0, r = nums.length - 1;

        // Perform Binary Search
        while (l <= r) {
            int m = (l + r) / 2;

            // Found Target
            if (nums[m] == target) {
                return m;
            }

            // Left Half Sorted - [4,5,6,7,0,1,2]
            if (nums[l] <= nums[m]) {
                if (nums[m] > target && nums[l] <= target) {  // Target is LARGER than SMALLEST value in LEFT half
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            }

            // Right Half Sorted - [6,7,0,1,2,3,4]
            else {
                if (nums[m] < target && nums[r] >= target) {  // Target is SMALLER than LARGEST value in RIGHT half
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
        }

        return -1;
    }

    // Algorithm(s) Used: Binary Search
    // Time Complexity: O(log(n))
    // Space Complexity: O(1)
    public int searchIII(int[] nums, int target) {
        int l = 0, r = nums.length - 1;

        // Perform Binary Search
        while (l <= r) {
            int m = (l + r) / 2;

            // Found Target
            if (nums[m] == target) {
                return m;
            }

            // Left Half Sorted - [4,5,6,7,0,1,2]
            if (nums[l] <= nums[m]) {
                if (nums[m] < target || nums[l] > target) {  // Target is SMALLER than SMALLEST value in LEFT half
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }

            // Right Half Sorted - [6,7,0,1,2,3,4]
            else {
                if (nums[m] < target && nums[r] >= target) {  // Target is SMALLER than LARGEST value in RIGHT half
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
        }

        return -1;
    }
}
