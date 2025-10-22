"""
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list.
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
    * The number of nodes in both lists is in the range [0, 50].
    * -100 <= Node.val <= 100
    * Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Algorithm Used: Dummy Node
# Time Complexity: O(list1 + list2) = O(n + m)
# Memory Complexity: O(1)
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

    # Create a dummy node to avoid the error of inserting into an empty linked list
    dummy = ListNode()
    tail = dummy

    # Iterate through both list while they both have values
    # Whichever node contains the lesser value add it to the tail and update tail's next pointer
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Remember the while loop above only iterates while both linked list have nodes.
    # There is a possibility that one of the nodes still has data.
    # Attach the additional data from the node to the end of the tail pointer
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next
