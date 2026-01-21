/*
Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

Given the heads of two singly linked-lists headA and headB,
return the node at which the two lists intersect.

If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:
The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

The inputs to the judge are given as follows (your program is not given these inputs):
    * intersectVal - The value of the node where the intersection occurs.
                    This is 0 if there is no intersected node.
    * listA - First linked list.
    * listB - Second linked list.
    * skipA - Number of nodes to skip ahead in listA (starting from head) to get to intersected node.
    * skipB - Number of nodes to skip ahead in listB (starting from head) to get to intersected node.
    * The judge will then create the linked structure based on these inputs and pass the two heads,
      headA and headB to your program.
    * If you correctly return the intersected node, then your solution will be accepted.

Example 1:
    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    Output: Intersected at '8'

Example 2:
    Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    Output: Intersected at '2'

Example 3:
    Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
    Output: No intersection

Constraints:
    * The number of nodes of listA is in the m.
    * The number of nodes of listB is in the n.
    * 1 <= m, n <= 3 * 104
    * 1 <= Node.val <= 105
    * 0 <= skipA <= m
    * 0 <= skipB <= n
    * intersectVal is 0 if listA and listB do not intersect.
    * intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

Follow up:
    Could you write a solution that runs in O(m + n) time and use only O(1) memory?
*/

package algorithms.linked_lists;

public class GetIntersectionNode {

    // Algorithm(s) Used: Linked List Traversal
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public ListNode getIntersectionNodeI(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;
        
        ListNode a = headA;
        ListNode b = headB;

        while (a != null || b != null) {
            if (a == b) return a;
            if (a != null) a = a.next; else  a = headB;
            if (b != null) b = b.next; else  b = headA;
        }

        return null;
    }

    // Algorithm(s) Used: Linked List Traversal
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public ListNode getIntersectionNodeII(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;
        
        ListNode a = headA;
        ListNode b = headB;

        while (a != b) {
            if (a != null) a = a.next; else  a = headB;
            if (b != null) b = b.next; else  b = headA;
        }

        return a;
    }
};
