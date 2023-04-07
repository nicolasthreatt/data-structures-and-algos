'''
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 
Constraints:
    * 1 <= nums.length <= 104
    * -10^4 <= nums[i] <= 10^4
    * nums is sorted in a strictly increasing order.
'''

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Two Pointers, Recursion
# Time Complexity: O(n)
# Space Complexity: O(log(n)) = O(log(h))
def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    
    # Create a helper function that will use two-pointers (left and right) along with recursion
    def helper(l, r):
        # If the left pointer is greater than the right pointer then its known
        # that the subarray have finished traversing so return null (Base Case)
        if l > r:
            return None
        
        # Each recursive call, find the midpoint of the array and create a TreeNode
        m = (l + r) // 2
        root = TreeNode(nums[m])

        # Recursively set the left and right nodes:
        #   - For the left node:
        #       * Keep its LOWER bound but its UPPER bound should be before the new midpoint
        #   - For the right node:
        #       * Keep its UPPER bound but its LOWER bound should be after the new midpoint
        root.left = helper(l, m - 1)
        root.right = helper(m + 1, r)

        # Return the new tree
        return root
    
    # Initially call the helper function with the
    # left pointer as 0 and the right pointer as the array's size
    return helper(0, len(nums) - 1)
