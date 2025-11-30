"""
Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/

Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val, and return the new head

Example 1:
    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]

Example 2:
    Input: head = [], val = 1
    Output: []

Example 3:
    Input: head = [7,7,7,7], val = 7
    Output: []

Constraints:
    * The number of nodes in the list is in the range [0, 10^4]
    * 1 <= Node.val <= 50
    * 0 <= val <= 50
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Algorithm(s) Used: Dummy Node, Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
def removeElementsI(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if not head:
        return None

    dummy = ListNode()
    dummy.next = head

    curr = dummy

    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return dummy.next


# Algorithm(s) Used: Dummy Node
# Time Complexity: O(n)
# Space Complexity: O(1)
def removeElementsII(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if not head:
        return None

    dummy = ListNode(0, head)

    head = dummy
    while head.next:
        if head.next.val == val:
            head.next = head.next.next
        else:
            head = head.next

    return dummy.next


# Helper function to build linked list from array
def build_list(values):
    if not values:
        return None

    dummy = ListNode()
    curr = dummy

    for v in values:
        curr.next = ListNode(v)
        curr = curr.next

    return dummy.next


# Helper function to convert linked list to Python list
def list_to_array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


if __name__ == "__main__":
    # (input_list, val_to_remove, expected_output_list)
    test_cases = [
        ([1,2,6,3,4,5,6], 6, [1,2,3,4,5]),
        ([], 1, []),
        ([7,7,7,7], 7, []),
        ([1,2,3], 4, [1,2,3]),
        ([4,1,4,2,4], 4, [1,2]),
    ]

    functions = [removeElementsI, removeElementsII]

    for func in functions:
        for input_list, val, expected in test_cases:
            head = build_list(input_list)
            result = func(head, val)
            result_arr = list_to_array(result)
            assert result_arr == expected
