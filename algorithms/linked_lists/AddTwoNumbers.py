"""
Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

Constraints:
    * The number of nodes in each linked list is in the range [1, 100].
    * 0 <= Node.val <= 9
    * It is guaranteed that the list represents a number that does not have leading zeros.
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class AddTwoNumbers:

    # Algorithm(s) Used: Dummy Node
    # Time Complexity: O(l1 + l2)
    # Space Complexity: O(1)
    def addTwoNumbersI(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        result = dummy

        carry = 0  # In case sum of nodes l1 and l2 is greater than 10

        # Iterate though both input lists and while there is nothing to carry over:
        #   1. Create sum from the first list's node, second list's node, and the carry
        #      Since a number in the list cannot be greater than 9, seperate the carry from sum.
        #   2. Assign the dummy's next value to the sum
        #   3. Update l1, l2, and the dummy to their next pointer
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            total = a + b + carry
            digit = total % 10
            carry = total // 10

            dummy.next = ListNode(digit)
            dummy = dummy.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next


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
    Solution = AddTwoNumbers()

    # (l1, l2, expected)
    test_cases = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([1], [9], [0, 1]),
        ([5, 5], [5, 5], [0, 1, 1]),
        ([1, 8], [0], [1, 8]),
    ]

    funcs = [
        Solution.addTwoNumbersI,
    ]

    for func in funcs:
        for l1_vals, l2_vals, expected in test_cases:
            l1 = build_linked_list(l1_vals)
            l2 = build_linked_list(l2_vals)

            result = func(l1, l2)
            result_list = linked_list_to_list(result)

            assert result_list == expected
