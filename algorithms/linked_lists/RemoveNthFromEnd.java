/*
Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head

Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]

Constraints:
    * The number of nodes in the list is sz.
    * 1 <= sz <= 30
    * 0 <= Node.val <= 100
    * 1 <= n <= sz

Follow up: Could you do this in one pass?
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


public class RemoveNthFromEnd {

    // Helper to reverse a list
    private ListNode reverse(ListNode node) {
        ListNode prev = null;
        while (node != null) {
            ListNode nxt = node.next;
            node.next = prev;
            prev = node;
            node = nxt;
        }
        return prev;
    }

    // Algorithm Used: Two Passes
    // Time Complexity: O(2n) = O(n)
    // Space Complexity: O(1)
    public ListNode removeNthFromEndI(ListNode head, int n) {
        // Base Case: If list is empty or has one node, return None
        if (head == null) return null;

        // Find total length of the list (1st Pass)
        int length = 0;
        ListNode curr = head;
        while (curr != null) {
            length++;
            curr = curr.next;
        }

        // Remove first node if needed
        if (length == n) return head.next;

        // Find node before the one to remove (2nd Pass)
        curr = head;
        for (int i = 0; i < length - n - 1; i++) {
            curr = curr.next;
        }

        // Remove target node
        curr.next = curr.next.next;

        return head;
    }

    // Algorithm Used: Reverse Linked List
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public ListNode removeNthFromEndII(ListNode head, int n) {
        // Base Case: If list is empty or has one node, return None
        if (head == null) return null;

        // Reverse the linked list
        head = reverse(head);

        // Remove nth node from start (originally nth from end)
        if (n == 1) {
            head = head.next;
        } else {
            ListNode curr = head;
            for (int i = 0; i < n - 2; i++) { // Stop one node before the one to remove
                curr = curr.next;
            }
            curr.next = curr.next.next;
        }

        // Reverse back to original order
        return reverse(head);
    }

    // Algorithm Used: Dummy Node, Two Pointers
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public ListNode removeNthFromEndIII(ListNode head, int n) {
        // Base Case: If list is empty or has one node, return None
        if (head == null) return null;

        // Dummy node
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        // Two Pointers
        ListNode slow = dummy;
        ListNode fast = dummy;

        // Move FAST n+1 steps ahead so SLOW ends up one node before the one to remove
        for (int i = 0; i < n + 1; i++) {
            fast = fast.next;
        }

        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }

        // Remove target node
        slow.next = slow.next.next;

        return dummy.next;
    }
}
