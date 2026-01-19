"""
Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

Given the heads of two singly linked-lists headA and headB,
return the node at which the two lists intersect.

If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:
The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

The inputs to the judge are given as follows (your program is not given these inputs):
    * intersectVal - The value of the node where the intersection occurs.
                    This is 0 if there is no intersected node.
    * listA - First linked list.
    * listB - Second linked list.
    * skipA - Number of nodes to skip ahead in listA (starting from head) to get to intersected node.
    * skipB - Number of nodes to skip ahead in listB (starting from head) to get to intersected node.
    * The judge will then create the linked structure based on these inputs and pass the two heads,
      headA and headB to your program.
    * If you correctly return the intersected node, then your solution will be accepted.

Example 1:
    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    Output: Intersected at '8'

Example 2:
    Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    Output: Intersected at '2'

Example 3:
    Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
    Output: No intersection

Constraints:
    * The number of nodes of listA is in the m.
    * The number of nodes of listB is in the n.
    * 1 <= m, n <= 3 * 104
    * 1 <= Node.val <= 105
    * 0 <= skipA <= m
    * 0 <= skipB <= n
    * intersectVal is 0 if listA and listB do not intersect.
    * intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

Follow up:
    Could you write a solution that runs in O(m + n) time and use only O(1) memory?
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class GetIntersectionNode:

    # Algorithm Used: Linked List Traversal
    # Time Complexity: O(n + m)
    # Space Complexity: O(1)
    def getIntersectionNodeI(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        a, b = headA, headB
        while a or b:
            if a == b:
                return a

            a = a.next if a else headB
            b = b.next if b else headA

        return None

    # Algorithm Used: Linked List Traversal
    # Time Complexity: O(n + m)
    # Space Complexity: O(1)
    def getIntersectionNodeII(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        a, b = headA, headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a


# Helper function to build a plain linked list (no cycle)
def build_list(values, pos=-1):
    if not values:
        return None, []

    nodes = [ListNode(v) for v in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    return nodes[0], nodes


# Helper function to convert linked list to Python list
def list_to_array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


# Build two lists with an intersection (same style as build_list)
def build_intersecting_lists(listA, listB, skipA, skipB):
    headA, nodesA = build_list(listA)
    headB, nodesB = build_list(listB)

    # No intersection
    if skipA == -1 or skipB == -1:
        return headA, headB, None

    nodesB[skipB].next = nodesA[skipA] # Create intersection

    return headA, headB, nodesA[skipA]


if __name__ == "__main__":
    Solution = GetIntersectionNode()

    # (listA, listB, skipA, skipB, expected_intersection_value)
    test_cases = [
        ([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3, 8),
        ([1, 9, 1, 2, 4], [3, 2, 4], 3, 1, 2),
        ([2, 6, 4], [1, 5], -1, -1, None),
        ([1], [1], -1, -1, None),
        ([1, 2, 3], [4, 5], -1, -1, None),
    ]

    funcs = [
        Solution.getIntersectionNodeI,
        Solution.getIntersectionNodeII
    ]

    for func in funcs:
        for listA, listB, skipA, skipB, expected_val in test_cases:
            headA, headB, expected_node = build_intersecting_lists(listA, listB, skipA, skipB)

            result = func(headA, headB)

            if expected_node is None:
                assert result is None
            else:
                assert result is expected_node
