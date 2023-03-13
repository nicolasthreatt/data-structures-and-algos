"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself. 

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
    * The number of nodes in each linked list is in the range [1, 100].
    * 0 <= Node.val <= 9
    * It is guaranteed that the list represents a number that does not have leading zeros.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time Complexity: O(n)
# Memory Complexity: O(n)
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    # Create a dummy to store the result of the sum from 
    dummy = ListNode()
    result = dummy
    
    # Incase the sum of the nodes from l1 and l2 are greater than 10,
    # initialize a variable that carried over to the next's nodes sum.
    carry = 0

    # Iterate though both input lists and while there is nothing to carry over.
    # Create sum from the first list's node, second list's node, and the carry
    # Since a number in the list cannot be greater than 9, seperate the carry from sum.
    # Assign the dummy's next value to the sum
    # Update l1, l2, and the dummy to their next pointer
    while l1 or l2 or carry:
        firstNum = l1.val if l1 else 0
        secondNum = l2.val if l2 else 0

        sum = firstNum + secondNum + carry
        num = sum % 10
        carry = sum // 10

        dummy.next = ListNode(num)
        dummy = dummy.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    # Note at the beginning result's dummy was assigned to a dummy node
    return result.next