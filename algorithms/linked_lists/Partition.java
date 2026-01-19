/*
Partition List
https://leetcode.com/problems/partition-list

Given the head of a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
    Input: head = [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]

Example 2:
    Input: head = [2,1], x = 2
    Output: [1,2]

Constraints:
    * The number of nodes in the list is in the range [0, 200].
    * -100 <= Node.val <= 100
    * -200 <= x <= 200
 */

package algorithms.linked_lists;

public class Partition {

    // Algorithm Used: Dummy Node
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public ListNode partitionI(ListNode head, int x) {
        ListNode dummyLesser = new ListNode();
        ListNode dummyGreater = new ListNode();

        ListNode tailLesser = dummyLesser;
        ListNode tailGreater = dummyGreater;

        while (head != null) {
            if (head.val < x) {
                tailLesser.next = head;
                tailLesser = tailLesser.next;

            } else {
                tailGreater.next = head;
                tailGreater = tailGreater.next;
            }
            head = head.next;
        }

        tailGreater.next = null;              // End the 'greater' list to avoid potential cycle
        tailLesser.next = dummyGreater.next;  // Link the 'lesser' list with the 'greater' list

        return dummyLesser.next;
    }
    
}
