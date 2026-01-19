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


class Partition:

    # Algorithms Used: Dummy Nodes
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def partitionI(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
            dummy_lesser = tail_lesser = ListNode()
            dummy_greater = tail_greater = ListNode()

            while head:
                if head.val < x:
                    tail_lesser.next = head
                    tail_lesser = tail_lesser.next
                else:
                    tail_greater.next = head
                    tail_greater = tail_greater.next

                head = head.next

            # End the 'greater' list to avoid potential cycles
            tail_greater.next = None

            # Link the 'lesser' list with the 'greater' list
            tail_lesser.next = dummy_greater.next

            return dummy_lesser.next


if __name__ == "__main__":
    Solution = Partition()

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

    funcs = [
        Solution.partitionI
    ]

    for func in funcs:
        for nums, x, expected in test_cases:
            head = build_linked_list(nums)
            result = func(head, x)

            result_list = linked_list_to_list(result)
            assert result_list == expected
