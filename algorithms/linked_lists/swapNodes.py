"""
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the
kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Constraints:
    * The number of nodes in the list is n.
    * 1 <= k <= n <= 105
    * 0 <= Node.val <= 100
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Algorithm Used: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
def swapNodesI(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # Set the current node to the head of the linked list to iterate through the linked list.
    cur = head

    # Iterate through the linked list to find the kth node from the beginning and 
    # update the current node to the kth node from the beginning.
    # This will be the left node.
    # Note: k - 1 is used because the linked list is 1-indexed.
    for i in range(k - 1):
        cur = cur.next
    
    # Set the left node to the current node.
    # This will be swapped with the kth (right) node from the end later
    left = cur

    # Set the right node to the head of the linked list to iterate through the linked list
    # from the beginning to find the kth node from the end.
    right = head

    # Iterate until the current node is the last node in the linked list
    while cur.next:
        # Update the current and right nodes to their next node
        # to eventually find the kth node from the end.
        cur = cur.next
        right = right.next

    # Now that the left and right nodes have been found, swap their values (TWO POINTERS).
    left.val, right.val = right.val, left.val

    # Return the head of the linked list
    return head


# Algorithm Used: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
def swapNodesII(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    pass
