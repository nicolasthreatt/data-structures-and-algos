"""
Reorder List
https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list.

The list can be represented as:
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
    * The number of nodes in the list is in the range [1, 5 * 10^4].
    * 1 <= Node.val <= 1000
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ReorderList:

    # Algorithm Used: Two Pointers, Two Passes, Reverse, Floyd's Tortoise & Hare
    # Time Complexity: O(3n) = O(n)
    # Memory Complexity: O(1)
    def reorderListI(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Find Middle Node To Get Second Half of List
        mid = self._find_middle(head)

        # Reverse Second Half of List
        second = self._reverse(mid.next)  # Second half only
        mid.next = None                   # End Second Half

        # Merge Two Halves
        self._merge(head, second)

    # Algorithm Used: Two Pointers, Floyd's Tortoise & Hare
    # Time Complexity: O(n)
    # Memory Complexity: O(1)
    def _find_middle(self, head: ListNode) -> ListNode:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Algorithm Used: Two Pointers, Reverse List, Iterative
    # Time Complexity: O(n)
    # Memory Complexity: O(1)
    def _reverse(self, node: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while node:
            nxt = node.next

            node.next = prev
            prev = node

            node = nxt

        return prev

    # Algorithm Used: Two Pointers, Merge Two Lists, Iterative
    # Time Complexity: O(n)
    # Memory Complexity: O(1)
    def _merge(self, first: ListNode, second: Optional[ListNode]) -> None:
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second  # Swap Nodes
            second.next = tmp1   # Swap Nodes

            first = tmp1         # Move Foward Nodes
            second = tmp2        # Move Foward Nodes


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


if __name__ == "__main__":
    Solution = ReorderList()

    # (input, expected)
    test_cases = [
        ([1, 2, 3, 4],     [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5],  [1, 5, 2, 4, 3]),
        ([1],              [1]),
        ([1, 2],           [1, 2]),
        ([1, 2, 3],        [1, 3, 2]),
        ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
    ]

    funcs = [
        Solution.reorderListI,
    ]

    for func in funcs:
        for nums, expected in test_cases:
            head = build_linked_list(nums)

            func(head)
            result = linked_list_to_list(head)

            assert result == expected
