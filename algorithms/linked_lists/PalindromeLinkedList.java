/*
Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
    Input: head = [1,2,2,1]
    Output: true

Example 2:
    Input: head = [1,2]
    Output: false

Constraints:
    * The number of nodes in the list is in the range [1, 10^5].
    * 0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
*/
package algorithms.linked_lists;

import java.util.ArrayList;
import java.util.List;

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class PalindromeLinkedList {

    // Algorithm(s) Used: Reverse Linked List
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    private ListNode reverse(ListNode node) {
        if (node == null) {
            return null;
        }

        ListNode prev = null;

        while (node != null) {
            ListNode nxt = node.next;
            node.next = prev;
            prev = node;
            node = nxt;
        }

        return prev;
    }

    // Algorithm(s) Used: List, Binary Search
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public boolean isPalindromeI(ListNode head) {
        List<Integer> nodes = new ArrayList<>();

        while (head != null) {
            nodes.add(head.val);
            head = head.next;
        }

        int left = 0, right = nodes.size() - 1;
        while (left < right) {
            if (nodes.get(left) != nodes.get(right)) {
                return false;
            }
            left += 1;
            right -= 1;
        }
        
        return true;
    }


    // Algorithm(s) Used: Floyd's Tortoise & Hare, Reverse Linked List
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public boolean isPalindromeII(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        slow = reverse(slow);  // Middle Node

        while (slow != null) {
            if (slow.val != head.val) {
                return false;
            }
            slow = slow.next;
            head = head.next;
        }

        return true;
    }

}
