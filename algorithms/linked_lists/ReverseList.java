/*
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
*/
package algorithms.linked_lists;

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class ReverseList {

    // Algorithm(s) Used: Recursion
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public ListNode reverseListI(ListNode head) {
        if (head == null) return null;

        ListNode reverse = head;
        if (reverse.next != null) {
            reverse = reverseListI(head.next);
            head.next.next = head;
        }
        head.next = null; // End new reversed list 

        return reverse;
    }

    // Algorithm(s) Used: Two Pointers
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public ListNode reverseListII(ListNode head) {
        if (head == null) return null;

        ListNode prev = null;

        while (head != null) {
            ListNode tmp = head.next;

            head.next = prev;
            prev = head;

            head = tmp;
        }

        return prev;
    }
}
