"""
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
"""

from typing import List


# Algorithm(s) Used: Binary Search
# Time Complexity: O(nlog(n)) + O(n^2) = O(n^2)
# Space Complexity: O(n)
def threeSumI(nums: List[int]) -> List[List[int]]:
    triplets = list()

    nums.sort() # Time Complexity: O(nlog(n))
    for i in range(len(nums) - 1):

        if i > 0 and nums[i - 1] == nums[i]:  # Skip duplicate elements
            continue

        # Perform Binary Search
        j, k = i + i, len(nums) - 1
        while j < k:
            current_sum = nums[i] + nums[j] + nums[k]
            if current_sum > 0:
                k -= 1
            elif current_sum < 0:
                j += 1
            else:
                triplets.append([nums[i], nums[j], nums[k]])
                j += 1
                while j < k and nums[j - 1] == nums[j]:  # Skip duplicate elements
                    j += 1

    return triplets


# Helper function to normalize output order for comparison
def sort_triplets(result):
    return sorted([sorted(t) for t in result])


if __name__ == "__main__":
    test_cases = [
        ([-1,0,1,2,-1,-4], [[-1,-1,2], [-1,0,1]]),
        ([0,1,1], []),
        ([0,0,0], [[0,0,0]]),
        ([1,2,-2,-1], []),
        ([3,-2,1,0], []),
        ([0,0,0,0], [[0,0,0]]),
        ([-2,0,1,1,2], [[-2,0,2], [-2,1,1]]),
        ([], []),
        ([1,2,3], []),
        ([-1,0,1], [[-1,0,1]]),
        ([-4,-2,-2,-2,0,1,2,2,2], [[-4,2,2], [-2,0,2]]),
    ]

    for nums, expected in test_cases:
        result = threeSumI(nums)
        assert sort_triplets(result) == sort_triplets(expected)
