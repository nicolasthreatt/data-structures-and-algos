"""
Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Example 2:
    Input: head = [1,2]
    Output: [2,1]

Example 3:
    Input: head = []
    Output: []
 
Constraints:
    * The number of nodes in the list is the range [0, 5000].
    * -5000 <= Node.val <= 5000
 
Follow up:
    - A linked list can be reversed either iteratively or recursively.
    - Could you implement both?
"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Algorithm Used: Two Pointers
# Time Complexity: O(n)
# Memory Complexity: O(1)
def reverseListI(head: Optional[ListNode]) -> Optional[ListNode]:
    # Base Case: Return nothing if there is no head
    if not head:
        return None

    # Initialize a previous node
    previous = None

    # Iterate through the linked list
    #   - Store the next ListNode in a temporary varaible
    #   - Swap the next pointer with previous pointer
    #   - Swap the previous and curent pointers
    #   - Update the current pointer
    while head:
        tmp = head.next

        # Reverse Linked List
        head.next = previous
        previous = head

        # Move list forward
        head = tmp

    return previous


# Algorithm Used: Recursive
# Time Complexity: O(n)
# Memory Complexity: O(n)
def reverseListII(head: Optional[ListNode]) -> Optional[ListNode]:
    # Base Case: Return nothing if there is no head
    if not head:
        return None
    
    # Recursive Case
    #   - Check if the the head has a next node
    #   - If there is a next node, and if so recursively swap links
    #     
    newHead = head
    if head.next:
        newHead = reverseListII(head.next)
        head.next.next = head

    # Set the head's next node to none, which marks end of the reversed linked list
    head.next = None

    # Return the reversed linked list
    return newHead


# Helper function to build and construct linked list
def build_list(values: List[int], pos: int) -> ListNode:
    if not values:
        return None

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


# Helper function to convert linked list to list
def list_to_array(head: ListNode) -> List[int]:
    array = []
    while head:
        array.append(head.val)
        head = head.next
    return array

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
        ([1], [1]),
        ([3, 2, 0, -4], [-4, 0, 2, 3]),
    ]

    functions = [reverseListI, reverseListII]

    for func in functions:
        for values, expected in test_cases:
            head = build_list(values, -1)  # pos=-1 because no cycles
            reversed_head = func(head)
            output = list_to_array(reversed_head)
            assert output == expected
