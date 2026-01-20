/*
Reorder List
https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list.

The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes.
Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
    * The number of nodes in the list is in the range [1, 5 * 10^4].
    * 1 <= Node.val <= 1000
*/

package algorithms.linked_lists;

public class ReorderList {

    // Algorithm(s) Used: Two Pointers, Two Passes, Reverse, Floyd's Tortoise & Hare
    // Time Complexity: O(3n) = O(n)
    // Space Complexity: O(1)
    public void reorderListI(ListNode head) {
        if (head == null || head.next == null) return;

        // Find Middle Node To Get Second Half of List
        ListNode mid = find_middle(head);

        // Reverse Second Half of List
        ListNode second = reverse(mid.next);  // Second half only
        mid.next = null;                      // End Second Half

        // Merge Two Halves
        merge(head, second);
    }

    // Algorithm(s) Used: Floyd's Tortoise & Hare
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    private ListNode find_middle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head.next;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow;
    }

    // Algorithm(s) Used: Reverse Linked List, Iteration
    // Time Complexity: O(n)
    // Space Complexity: O(1)
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

    // Algorithm(s) Used: Merge Linked List, Iteration
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    private void merge(ListNode first, ListNode second) {
        while (second != null) {
            ListNode nxt1 = first.next;
            ListNode nxt2 = second.next;

            first.next = second;  // Swap Nodes
            second.next = nxt1;   // Swap Nodes

            first = nxt1;         // Move Foward Nodes
            second = nxt2;        // Move Foward Nodes
        }
    }
}
