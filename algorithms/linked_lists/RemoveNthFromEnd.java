/*
https://leetcode.com/problems/remove-nth-node-from-end-of-list

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

        // Find total length of the list
        int length = 0;
        ListNode curr = head;
        while (curr != null) {
            length++;
            curr = curr.next;
        }

        // Remove first node if needed
        if (length == n) return head.next;

        // Find node before the one to remove
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
            for (int i = 0; i < n - 2; i++) { // n-2 because we stop one node before the one to remove
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

        // Create dummy node
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        // Initialize two pointers
        ListNode slow = dummy;
        ListNode fast = dummy;

        // Move fast pointer n+1 steps ahead
        for (int i = 0; i < n + 1; i++) {
            fast = fast.next;
        }

        // Move both pointers until fast reaches the end
        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }

        // Remove target node
        slow.next = slow.next.next;

        return dummy.next;
    }
}
