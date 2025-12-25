"""
Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

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


class RemoveNthFromEnd:

    # Algorithm Used: Iteration, Two Passes
    # Time Complexity: O(2n) ≈ O(n)
    # Space Complexity: O(1)
    def removeNthFromEndI(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Base Case: If list is empty or has one node, return None
        if not head or not head.next:
            return None

        curr = head

        # Find total length of list (1st Pass)
        length = 0
        while curr:
            length += 1
            curr = curr.next

        # If removing the last node
        if n == length:
            return head.next

        # Find node BEFORE the one to remove (2nd Pass)
        curr = head
        for _ in range(length - n - 1):
            curr = curr.next

        # Remove target node
        curr.next = curr.next.next
        return head

    # Algorithm Used: Reverse Linked List
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def removeNthFromEndII(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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
            for _ in range(n - 2):  # Stop one node before the one to remove
                curr = curr.next
            curr.next = curr.next.next

        # Reverse back to original order
        return reverse(head)

    # Algorithm Used: Dummy Node, Two Pointers
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def removeNthFromEndIII(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Base Case: If list is empty or has one node, return None
        if not head or not head.next:
            return None

        dummy = ListNode()
        dummy.next = head

        slow = fast = dummy  # Two Pointers

        # Move FAST n+1 steps ahead so SLOW ends up one node before the one to remove
        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        # Remove the target node
        slow.next = slow.next.next

        return dummy.next


if __name__ == "__main__":
    Solution = RemoveNthFromEnd()

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

    funcs = [
        Solution.removeNthFromEndI,
        Solution.removeNthFromEndII,
        Solution.removeNthFromEndIII
    ]

    for func in funcs:
        for nodes, n, expected in test_cases:
            head = build_linked_list(nodes)
            result = func(head, n)
            result_list = linked_list_to_list(result)
            assert result_list == expected
