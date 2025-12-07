"""
Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
    Input: head = [1,2,2,1]
    Output: true

Example 2:
    Input: head = [1,2]
    Output: false

Constraints:
    * The number of nodes in the list is in the range [1, 10^5].
    * 0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""

from collections import defaultdict
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class PalindromeLinkedList:

    # Algorithm(s) Used: Reverse Linked List, Previous Node
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self, node: Optional[ListNode]) -> Optional[ListNode]:
        if not node:
            return None

        prev = None
        while node:
            nxt_node = node.next
            node.next = prev
            prev = node
            node = nxt_node

        return prev

    # Algorithm(s) Used: List, Binary Search
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isPalindromeI(self, head: Optional[ListNode]) -> bool:
        nodes = []

        while head:
            nodes.append(head.val)
            head = head.next
        
        left, right = 0, len(nodes) - 1
        while left < right:
            if nodes[left] != nodes[right]:
                return False
            left += 1
            right -= 1

        return True

    # Algorithm(s) Used: Floyd's Tortoise & Hare, Reverse Linked List
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isPalindromeII(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow = self.reverse(slow)  # Middle Node
        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next

        return True


if __name__ == "__main__":
    def build_linked_list(values: List[int]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        for v in values:
            tail.next = ListNode(v)
            tail = tail.next
        return dummy.next

    test_cases = [
        # (input_list, expected_output)
        ([1, 2, 2, 1], True),
        ([1, 2], False),
        ([1, 2, 3, 2, 1], True),
        ([7], True),
        ([], True),
        ([1, 0, 1, 2], False),
        ([3, 3], True),
        ([3, 3, 3, 3], True),
    ]

    Solution = PalindromeLinkedList()

    funcs = [
        Solution.isPalindromeI,
        Solution.isPalindromeII
    ]

    for func in funcs:
        for nodes, expected in test_cases:
            head = build_linked_list(nodes)
            result = func(head)
            assert result == expected
