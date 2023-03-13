"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
    * The number of nodes in the list is sz.
    * 1 <= sz <= 30
    * 0 <= Node.val <= 100
    * 1 <= n <= sz

Follow up: Could you do this in one pass?
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Algorithm Used: Iteration with count
# Time Complexity: 
# Memory Complexity: 
def removeNthFromEndI(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    pass


# Algorithm Used: Reverse linked list
# Time Complexity: 
# Memory Complexity: 
def removeNthFromEndII(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    pass


# Algorithm Used: Dummy Node, Two Pointers
# Time Complexity: O(n)
# Memory Complexity: O(n)
def removeNthFromEndIII(head: Optional[ListNode], n: int) -> Optional[ListNode]:

    # Create a dummy node and assign it's next pointer to the head of the linked list
    dummy = ListNode(0, head)

    # Since this is a two pointer algorithm there must be a left and right node
    # Assign the left node to the dummy
    # Assign the right node n next positions after the head of the linked list
    left = dummy
    right = head
    while n > 0 and right:
        right = right.next
        n -= 1

    # Iterate through the linked list until the right pointer is null
    # Through each iteration update the left and right pointers.
    # Once the right node is null, the right node is at the nth position from the end
    # of the lined list. Thus can delete the specified node.
    while right:
        left = left.next
        right = right.next

    # Delete specified node by skipping over its link
    left.next = left.next.next

    # Remember from above that the head of the linked list was assigned to dummy's next node
    return dummy.next
