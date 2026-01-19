"""
Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.

Example 2:
    Input: head = [1,2,3,4,5,6]
    Output: [4,5,6]
    Explanation: Since list has two middle nodes values 3 and 4, return the second one.

Constraints:
    * The number of nodes in the list is in the range [1, 100].
    * 1 <= Node.val <= 100
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MiddleNode:

    # Algorithm(s) Used: Floyd's Tortoise & Hare
    # Time Complexity: O(n)
    # Space Complexity: O(1) 
    def middleNodeI(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


def build_linked_list(values: List) -> Optional[ListNode]:
    dummy = tail = ListNode()
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


if __name__ == "__main__":
    Solution = MiddleNode()

    # (input_list, output_list)
    test_cases = [
        ([1, 2, 3, 4, 5], [3, 4, 5]),
        ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
        ([1], [1]),
        ([10, 20], [20]),
        ([7, 8, 9, 10], [9, 10]),
        ([6, 1, 4], [1, 4]),
    ]

    funcs = [
        Solution.middleNodeI
    ]

    for func in funcs:
        for nums, expected in test_cases:
            head = build_linked_list(nums)

            result = func(head)
            result_list = linked_list_to_list(result)

            assert result_list == expected
