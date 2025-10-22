"""
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 
Constraints:
    * The number of nodes in the list is the range [0, 5000].
    * -5000 <= Node.val <= 5000
 
Follow up:
    - A linked list can be reversed either iteratively or recursively.
    - Could you implement both?
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Algorithm Used: Two Pointers
# Time Complexity: O(n)
# Memory Complexity: O(1)
def reverseListI(self, head: Optional[ListNode]) -> Optional[ListNode]:

    # Initialize a previous and current ListNode
    previous = None
    current = head

    # Iterate through the linked list
    #   - Store the next ListNode in a temporary varaible
    #   - Swap the next pointer with previous pointer
    #   - Swap the previous and curent pointers
    #   - Update the current pointer
    while current:
        next = current.next
        current.next = previous
        previous = current

        current = next

    return previous


# Algorithm Used: Recursive
# Time Complexity: O(n)
# Memory Complexity: O(n)
def reverseListII(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # Base Case:
    #   - Return nothing if there is no head
    if not head:
        return None
    
    # Recursive Case
    #   - Check if the the head has a next node
    #   - If there is a next node, and if so recursively swap links
    #   - After set the head's next node to none.
    #     This marks the end of the reversed linked list
    newHead = head
    if head.next:
        newHead = reverseListII(head.next)
        head.next.next = head
    head.next = None

    # Return the reversed linked list
    return newHead
