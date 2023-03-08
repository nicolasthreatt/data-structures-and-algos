"""
https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by
continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 
Constraints:
    * The number of the nodes in the list is in the range [0, 104].
    * -105 <= Node.val <= 105
    * pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
    - https://www.geeksforgeeks.org/floyds-cycle-finding-algorithm/
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Algorithm Used: Hashmap
# Time Complexity: O(n)
# Memory Complexity: O(n)
def hasCycleI(head: Optional[ListNode]) -> bool:

    # Initialize a hash map
    hashMap = set()

    # Iterate through the linked list
    # Check to see if the current node is in the hash map
    #   - If so, there is a loop and return True
    #   - If not, add node to hash map and update current pointer
    current = head
    while current:
        if current in hashMap:
            return True
        
        hashMap.add(current)
        current = current.next
    
    return False


# Algorithm Used: Two Pointers, Floyd's Tortoise & Hare
# Time Complexity: O(n)
# Memory Complexity: O(1)
def hasCycleII(head: Optional[ListNode]) -> bool:

    # Initialize the slow and fast pointers to the head
    slow, fast = head, head

    # Iterate through linked list with fast pointer
    # Through each iteration:
    #   - Update slow pointer 1 position
    #   - Update next pointer 2 poisitions
    # If there is a loop slow and next pointers will be equal
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
