class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Cracking the Coding Interview: 2.1 - Remove Duplicates

Write code to remove duplicates from an unsorted linked list.

Follow Up - How would you solve this problem if a temporary buffer is not allowed?
"""
# Algorithm: Hash Set
# Time Complexity: O(n)
# Space Complexiity: O(n)
def remove_duplicatesI(head: ListNode) -> ListNode:
    buffer = set()

    prev = None
    while head:
        if head.val not in buffer:
            buffer.add(head)
            prev = head
        else:
            prev.next = head.next
        head = head.next
    return head

# Algorithm: Two Passes
# Time Complexity: O(n^2)
# Space Complexiity: O(1)
def remove_duplicatesII(head: ListNode) -> ListNode:
    current = head
    while current:
        fast = current  # Removes all future nodes that have the same value
        while fast.next:
            if fast.next.data == current.data:
                fast.next = fast.next.next
            else:
                fast = fast.next
        current = current.next


"""
Cracking the Coding Interview: 2.2 - Return Kth to Last

Implement an algorithm to find the kth to last element of a singly linked list.
"""
# Algorithm: Two Passes
# Time Complexity: O(n)
# Space Complexity: O(1)
def return_kth_to_lastI(head: ListNode, k: int) -> ListNode:
    nodes = 0

    current = head
    while current:
        nodes += 1
        current = current.next
    
    current = head
    current_node = 0
    while current:
        current_node += 1
        if current_node == nodes - k + 1:
            return current
        current = current.next

# Algorithm: Two Passes
# Time Complexity: O(n)
# Space Complexity: O(1)
def return_kth_to_lastII(head: ListNode, k: int) -> ListNode:
    p1, p2 = head, head

    for _ in range(k):
        if p1 == None: return p1
        p1 = p1.next
    
    while p1:
        p1 = p1.next
        p2 = p2.next

    return p2

# Algorithm: Dummy Node
# Time Complexity: O(n)
# Space Complexity: O(1)
def return_kth_to_lastIII():
    dummy = ListNode(0)
    dummy.next = head

    fast = slow = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next


"""
Cracking the Coding Interview: 2.3 - Delete Middle Node - Version 1

Implement an algorithm to delete a node in the middle given the head node.
"""
# Algorithm: Floyd's Tortoise & Hare
# Time Complexity: O(n)
# Space Complexity: O(1)
def delete_middle_node(head: ListNode) -> ListNode:
    if not head or not head.next:
        return None

    prev = None
    slow, fast = head, head

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next  # Remove the middle node by updating the previous node's next pointer.

    return head


"""
Cracking the Coding Interview: 2.3 - Delete Middle Node - Version 2

Implement an algorithm to delete a node in the middle
(i.e., any node but the fist and last node, not necessarily the exact middle)
of a singly linked list, given only access to that node.

Input: the node c from the linked list a -> b -> c -> d -> e -> f
Output: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f
"""
# Algorithm: Node Deletion
# Time Complexity: O(n)
# Space Complexity: O(1)
def delete_middle_nodeII(n: ListNode) -> ListNode:
    if not n or not n.next:
        return None
    
    next_node = n.next

    n.data = next_node.data
    n.next = next_node.next
    return True


"""
Cracking the Coding Interview: 2.4 - Partition

Write code to partition a linked list around a value x, such that all nodes less than x
comes before all nodes greater than or equal to x.

IMPORTANT: The partition element x can appear anywhere in the "right partition".
           It does not need to appear between the left and right partitions.
           The additional spacing in the example below indicates the partition.

The output below is one of many valid inputs.

Examples
    - Input:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1, partition = 5
    - Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""
# Algorithm: Dummy Node
# Time Complexity: O(n)
# Space Complexity: O(1)
def partition(head: ListNode, partition: int) -> ListNode:
    if head is None:
        return None

    left_dummy, right_dummy = ListNode(), ListNode()
    left = left_dummy
    right = right_dummy

    while head:
        if head.data < partition:
            left.next = head
            left = left.next
        else:
            right.next = head
            right = right.next
        head = head.next

    left.next = right_dummy.next  # Connect two lists (end of left and start of right)
    right.next = None  # Reset end of linked list

    return left_dummy.next


"""
Cracking the Coding Interview: 2.5 - Sum Lists

You have two numbers represented by a linked list, where each node contains a digit.
The digits are stored in reverse order, such that that the 1's digit is at the head.
Writie a function that adds the two numbers and return the sum as a linked list.

You are not allowed to convert the linked list to an integer.

Examples:
    - Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is 617 + 295.
    - Output: 2 -> 1 -> 9. That is, 912.

    - Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is 716 + 592.
    - Output: 9 -> 1 -> 2
"""
# Algorithm: Dummy Node
# Time Complexity: O(max(m, n))
# Space Compleixty: O(max(m, n))
def sum_lists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 and not l2:
        return None

    dummy = ListNode()
    head = dummy

    while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        carry = 0

        node_sum = val1 + val2 + carry
        if node_sum >= 10:
            carry = 1
            node_sum -= 10

        head.next = ListNode(node_sum)
        head = head.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next

    if carry:
        head.next = ListNode(carry)
        head = head.next

    return dummy.next



"""
Cracking the Coding Interview: 2.6 - Palindrome.

Implement a function to check if a linked list is a palindrome.
"""
# Algorithm: Floyd's Tortoise & Hare, Reverse Linked List
# Time Complexity: O(n)
# Space Complexity: O(1)
def palindrome(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return True

    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    while slow:
        nxt = slow.next
        prev = slow
        slow = nxt

    left, right = head, prev  # Compare the first half and the reversed second half
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


"""
Cracking the Coding Interview: 2.7 - Intersection

Given two (singly) linked lists, determine if the two lists intersect.

Return the intersecting node.

Note that the intersection is defined based on reference, not value.
That is, if the kth node of the first linked list in the exact same node
(by reference) as the jth node of the second linked list, then they intersect.
"""
# Algorithm: Intersecting Nodes
# Time Complexity: O(n + m)
# Space Complexity: O(1)
def intersecting_node(headA: ListNode, headB: ListNode) -> ListNode:
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a


"""
Cracking the Coding Interview: 2.8 - Loop Detection

Given a linked list which might contain a loop, implement an algorithm that
returns the node at the begnning of the loop (if one exists).
"""
# Algorithm: Floyd's Tortoise & Hare
# Time Complexity: O(n)
# Space Complexity: O(1)
def loop_detection(head: ListNode) -> ListNode:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow

    return None
