"""
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
 
Constraints:
    * 1 <= nums.length <= 105
    * -104 <= nums[i] <= 104
    * k is in the range [1, the number of unique elements in the array].
    * It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from typing import List


# Algorithm Used: Bucket Sort
# Time Complexity: O(n)
def topKFrequent(nums: List[int], k: int) -> List[int]:
    # Create a hash map to count the occurances of each value in the input list
    count = {}

    # Iterate through input list and count the number of occurances for each element
    for n in nums:
        count[n] = count.get(n, 0) + 1
    
    # Create an array the size of the input list to map the number of occurances
    # for each element in the input list
    freq = [[] for i in range(len(nums) + 1)]
    for n, c in count.items():  # .items() -> key, value
        freq[c].append(n)
    
    # Initialize an empty list to return results
    res = []

    # Iterate through the most frequence occurence list in reverse
    # This ensures that the most frequent elements are visited first
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)

            # Return the result array once it reaches the target size
            if len(res) == k:
                return res
