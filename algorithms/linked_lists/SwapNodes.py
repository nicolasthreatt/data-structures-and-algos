"""
Swapping Nodes in a Linked List
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
    * 1 <= k <= n <= 10^5
    * 0 <= Node.val <= 100
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SwapNodes:

    # Algorithm Used: Two Pointers, Single Pass
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def swapNodesI(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr = head

        # Find the kth node to be removed from the START
        for _ in range(k - 1):  # 1-indexed based
            curr = curr.next

        # Set LEFT pointer at CURR to store kth node from the START
        left = curr

        # Find the kth node to be removed from the END
        # When loop terminates, RIGHT will be kth node from the END
        right = head
        while curr.next:
            curr = curr.next
            right = right.next

        # Swap values of the two pointer nodes
        left.val, right.val = right.val, left.val

        return head


if __name__ == "__main__":
    Solution = SwapNodes()

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
        # (input_list, k, expected_output)
        ([1, 2, 3, 4, 5], 2, [1, 4, 3, 2, 5]),
        ([1], 1, [1]),
        ([1, 2], 1, [2, 1]),
        ([1, 2], 2, [2, 1]),
        ([7, 9, 6, 6, 7, 8, 3, 0, 9, 5], 5, [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]),
        ([10, 20, 30, 40], 2, [10, 30, 20, 40]),
    ]

    funcs = [
        Solution.swapNodesI,
    ]

    for func in funcs:
        for nodes, k, expected in test_cases:
            head = build_linked_list(nodes)
            result = func(head, k)
            result_list = linked_list_to_list(result)
            assert result_list == expected
