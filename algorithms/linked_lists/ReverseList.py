"""
Reverse Linked List
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

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ReverseList:

    # Algorithm Used: Recursive
    # Time Complexity: O(n)
    # Memory Complexity: O(n)
    def reverseListI(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case: End of List
        if not head:
            return None
        
        reverse = head
        if head.next:
            reverse = self.reverseListI(head.next)
            head.next.next = head  # Reverse pointer - Next node now points to current node

        head.next = None  # End new reversed list 

        return reverse

    # Algorithm Used: Two Pointers
    # Time Complexity: O(n)
    # Memory Complexity: O(1)
    def reverseListII(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case: End of List
        if not head:
            return None

        previous = None  # Pointer 1

        # Iterate through the linked list and swap previous and curent pointers
        while head:
            tmp = head.next  # Pointer 2

            # Reverse Linked List
            head.next = previous
            previous = head

            head = tmp  # Move list forward

        return previous


if __name__ == "__main__":
    Solution = ReverseList()

    def build_linked_list(values: List[int]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        for v in values:
            tail.next = ListNode(v)
            tail = tail.next
        return dummy.next

    def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
        ([1], [1]),
        ([3, 2, 0, -4], [-4, 0, 2, 3]),
    ]

    funcs = [Solution.reverseListI, Solution.reverseListII]

    for func in funcs:
        for values, expected in test_cases:
            head = build_linked_list(values)
            reversed_head = func(head)
            output = linked_list_to_list(reversed_head)
            assert output == expected
