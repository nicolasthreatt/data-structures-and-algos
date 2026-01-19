/*
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
*/

package algorithms.linked_lists;

public class MiddleNode {
    
    // Algorithm(s) Used: Floyd's Tortoise & Hare
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public ListNode middleNodeI(ListNode head) {
        ListNode slow = head, fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        return slow;
    }
};
