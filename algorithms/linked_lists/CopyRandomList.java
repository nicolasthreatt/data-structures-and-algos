/*
Copy List With Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list of length n is given such that each node contains an additional random pointer,
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value of its corresponding original node.

Both the next and random pointer of the new nodes should point to new nodes in the copied list
such that the pointers in the original list and copied list represent the same list state.

None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, 
then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes.

Each node is represented as a pair of [val, random_index] where:
    * val: an integer representing Node.val
    * random_index: the index of the node (range from 0 to n-1)
      that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

Example 1:
    Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
    Input: head = [[1,1],[2,1]]
    Output: [[1,1],[2,1]]

Example 3:
    Input: head = [[3,null],[3,0],[3,null]]
    Output: [[3,null],[3,0],[3,null]]

Constraints:
    * 0 <= n <= 1000
    * -10^4 <= Node.val <= 10^4
    * Node.random is null or is pointing to some node in the linked list.
*/

package algorithms.linked_lists;

import java.util.HashMap;

// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
};

public class CopyRandomList {

    // Algorithm(s) Used: Hash Map, Two Passes
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public Node copyRandomListI(Node head) {

        HashMap<Node, Node> mapper = new HashMap<>();
        mapper.put(null, null);  // {old: new}

        // Map the old node to the copy node (1st Pass)
        Node first = head;
        while (first != null) {
            mapper.put(first, new Node(first.val));

            first = first.next;
        }

        // Connect nodes (2nd Pass)
        Node second = head;
        while (second != null) {
            Node copy = mapper.get(second);

            copy.next = mapper.get(second.next);
            copy.random = mapper.get(second.random);

            second = second.next;
        }

        return mapper.get(head);
    }
}
