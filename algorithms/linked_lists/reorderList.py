"""
https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes.
Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
    * The number of nodes in the list is in the range [1, 5 * 104].
    * 1 <= Node.val <= 1000
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Algorithm Used: Two Pointers, Floyd's Tortoise & Hare
# Time Complexity: O(n)
# Memory Complexity: O(1)
def reorderList(head: Optional[ListNode]) -> None:
    # Find Middle Node of Linked List
    # This will be obtained from the slow pointer
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the nodes from the second half of linked list.
    # Note from above that the second half of the linked list
    # is obtained from the slow pointer.
    second = slow.next
    prev = slow.next = None
    while second:
        next = second.next
        second.next = prev
        prev = second

        second = next

    # Merge the two halves (first and second) together but alternate nodes
    first, second = head, prev
    while second:
        tmp1, temp2 = first.next, second.next

        first.next = second
        second.next = tmp1

        first, second = tmp1, temp2
