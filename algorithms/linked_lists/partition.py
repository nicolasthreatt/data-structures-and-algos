"""
Partition List
https://leetcode.com/problems/partition-list

Given the head of a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
    Input: head = [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]

Example 2:
    Input: head = [2,1], x = 2
    Output: [1,2]

Constraints:
    * The number of nodes in the list is in the range [0, 200].
    * -100 <= Node.val <= 100
    * -200 <= x <= 200
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Algorithms Used: Dummy Nodes
# Time Complexity: O(n)
# Space Complexity: O(1)
def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_lesser = lesser_tail = ListNode()
        dummy_greater = greater_tail = ListNode()

        while head:
            if head.val < x:
                lesser_tail.next = head
                lesser_tail = lesser_tail.next
            else:
                greater_tail.next = head
                greater_tail = greater_tail.next
            head = head.next

        # End the 'greater' list to avoid potential cycles
        greater_tail.next = None

        # Link the 'lesser' list with the 'greater' list
        lesser_tail.next = dummy_greater.next

        return dummy_lesser.next


if __name__ == "__main__":
    def build_linked_list(values: List) -> Optional[ListNode]:
        dummy = tail = ListNode()
        for v in values:
            tail.next = ListNode(v)
            tail = tail.next
        return dummy.next

    def linked_list_to_list(head: ListNode) -> List:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    test_cases = [
        # (input_list, x, expected_output)
        ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),
        ([2, 1], 2, [1, 2]),
        ([1, 2, 3], 4, [1, 2, 3]),
        ([4, 5, 6], 3, [4, 5, 6]),
        ([], 3, []),
        ([3, 3, 3], 3, [3, 3, 3]),
    ]

    for nums, x, expected in test_cases:
        head = build_linked_list(nums)
        result = partition(head, x)
        result_list = linked_list_to_list(result)
        assert result_list == expected
