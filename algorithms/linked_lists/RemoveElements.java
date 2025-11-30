/*
Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/

Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val, and return the new head

Example 1:
    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]

Example 2:
    Input: head = [], val = 1
    Output: []

Example 3:
    Input: head = [7,7,7,7], val = 7
    Output: []

Constraints:
    * The number of nodes in the list is in the range [0, 10^4]
    * 1 <= Node.val <= 50
    * 0 <= val <= 50
*/
package algorithms.linked_lists;

public class RemoveElements {

    // Algorithm(s) Used: Dummy Node, Two Pointers
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public ListNode removeElementsI(ListNode head, int val) {
        ListNode dummy = new ListNode();
        dummy.next = head;

        ListNode curr = dummy;
        while (curr.next != null) {
            if (curr.next.val == val) {
                curr.next = curr.next.next;
            } else {
                curr = curr.next;
            }
        }

        return dummy.next;
    }

    // Algorithm(s) Used: Dummy Node
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public ListNode removeElementII(ListNode head, int val) {
        ListNode dummy = new ListNode(0, head);

        head = dummy;
        while (head.next != null) {
            if (head.next.val == val) {
                head.next = head.next.next;
            } else {
                head = head.next;
            }
        }

        return dummy.next;
    }
}
