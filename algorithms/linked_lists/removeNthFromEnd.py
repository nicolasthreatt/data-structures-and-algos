"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list

Given the head of a linked list, remove the nth node from the end of the list and return its head

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

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Algorithm Used: Iteration, Two Passes
# Time Complexity: O(2n) ≈ O(n)
# Space Complexity: O(1)
def removeNthFromEndI(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # Base Case: If list is empty or has one node, return None
    if not head or not head.next:
        return None

    curr = head

    # Find total length of list
    length = 0
    while curr:
        length += 1
        curr = curr.next

    # If removing the last node
    if n == length:
        return head.next

    # Find node before the one to remove
    curr = head
    for _ in range(length - n - 1):
        curr = curr.next

    # Remove target node
    curr.next = curr.next.next
    return head


# Algorithm Used: Reverse Linked List
# Time Complexity: O(n)
# Space Complexity: O(1)
def removeNthFromEndII(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # Base Case: If list is empty or has one node, return None
    if not head or not head.next:
        return None

    # Helper to reverse a list
    def reverse(node: ListNode) -> ListNode:
        prev = None
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        return prev

    # Reverse list
    head = reverse(head)

    # After linked list is reversed, remove nth node from start
    if n == 1:
        head = head.next
    else:
        curr = head
        for _ in range(n - 2):  # n - 2 because we stop one node before the one to remove
            curr = curr.next
        curr.next = curr.next.next

    # Reverse back to original order
    return reverse(head)


# Algorithm Used: Dummy Node, Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n)
def removeNthFromEndIII(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # Base Case: If list is empty or has one node, return None
    if not head or not head.next:
        return None

    # Create a dummy node that points to head (helps handle edge cases)
    dummy = ListNode()
    dummy.next = head

    # Initialize two pointers starting from dummy
    slow = fast = dummy

    # Move fast n+1 steps ahead so slow ends up right before the node to remove
    for _ in range(n + 1):
        fast = fast.next

    # Move both until fast reaches the end
    # Slow will be just before the node to remove
    while fast:
        slow = slow.next
        fast = fast.next

    # Remove the target node
    slow.next = slow.next.next

    return dummy.next


if __name__ == "__main__":
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
        # (input_list, n, expected_output)
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([10, 20, 30, 40], 3, [10, 30, 40]),
    ]

    for func in [removeNthFromEndI, removeNthFromEndII, removeNthFromEndIII]:
        for nodes, n, expected in test_cases:
            head = build_linked_list(nodes)
            result = func(head, n)
            result_list = linked_list_to_list(result)
            assert result_list == expected
