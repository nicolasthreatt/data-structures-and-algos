"""
Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/description/

Given an integer array nums and an integer k, return true if there are
two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k

Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true

Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: true

Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false
 
Constraints:
    * 1 <= nums.length <= 10^5
    * -10^9 <= nums[i] <= 10^9
    * 0 <= k <= 10^5
"""

from typing import List


# Algorithm Used: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(k)
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    window = set()

    left = 0
    for right in range(len(nums)):
        if nums[right] in window:
            return True
        
        window.add(nums[right])

        if right - left >= k:  # Dynamically keep search window the max allowed size (k)
            window.remove(nums[left])
            left += 1
    
    return False


if __name__ == "__main__":
    assert containsNearbyDuplicate([1, 2, 3, 1], 3) == True      # duplicate 1 within distance 3
    assert containsNearbyDuplicate([1, 0, 1, 1], 1) == True      # duplicate 1 within distance 1
    assert containsNearbyDuplicate([1, 2, 3, 4, 5], 3) == False  # no duplicates
    assert containsNearbyDuplicate([1, 2, 3, 1], 2) == False     # duplicate 1, but too far apart
    assert containsNearbyDuplicate([], 1) == False               # empty input
    assert containsNearbyDuplicate([1], 1) == False              # single element
    assert containsNearbyDuplicate([1, 1, 1, 1], 1) == True      # duplicates all within 1 distance
    assert containsNearbyDuplicate([1, 2, 3, 1], 0) == False     # k = 0, window can't include other elements
