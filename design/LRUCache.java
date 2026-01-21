/*
LRC Cache
https://leetcode.com/problems/lru-cache/
https://www.youtube.com/watch?v=R5ON3iwx78M

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
    * LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    * int get(int key) Return the value of the key if the key exists, otherwise return -1.
    * void put(int key, int value) Update the value of the key if the key exists.
      Otherwise, add the key-value pair to the cache.
      If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Input:
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

Output:
    [null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation:
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 1); // cache is {1=1}
    lRUCache.put(2, 2); // cache is {1=1, 2=2}
    lRUCache.get(1);    // return 1
    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    lRUCache.get(2);    // returns -1 (not found)
    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lRUCache.get(1);    // return -1 (not found)
    lRUCache.get(3);    // return 3
    lRUCache.get(4);    // return 4
 
Constraints:
    * 1 <= capacity <= 3000
    * 0 <= key <= 10^4
    * 0 <= value <= 10^5
    * At most 2 * 10^5 calls will be made to get and put.
*/

package design;

import java.util.HashMap;
import java.util.Map;

public class LRUCache {
    // Definition for doubly-linked list.
    private class Node {
        int key;
        int val;

        Node prev;
        Node next;

        Node(int key, int value) {
            this.key = key;
            this.val = value;
        }
    }

    private int capacity;
    private Map<Integer, Node> cache;

    private Node left;   // Least Recently Used
    private Node right;  // Most Recently Used

    // Remove current node from a double linked list, O(1).
    private void remove(Node node) {
        Node prv = node.prev;
        Node nxt = node.next;

        prv.next = nxt;
        nxt.prev = prv;
    }

    // Insert nodes on the right side of a double linked list, O(1).
    private void insert(Node node) {
        Node prv = this.right.prev;
        Node nxt = this.right;

        prv.next = node;
        nxt.prev = node;

        node.prev = prv;
        node.next = nxt;
    }

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();

        this.left = new Node(0, 0);
        this.right = new Node(0, 0);

        this.left.next = this.right;
        this.right.prev = this.left;
    }

    // Returns value key if key exists, otherwise -1.
    public int get(int key) {
        if (this.cache.containsKey(key)) {
            remove(this.cache.get(key));  // Update ccache with most recent key
            insert(this.cache.get(key));  // Update ccache with most recent key

            return this.cache.get(key).val;
        }

        return -1;
    }

    // Update value of key if key exists.
    public void put(int key, int value) {
        if (this.cache.containsKey(key)) {
            remove(this.cache.get(key));
        }

        this.cache.put(key, new Node(key, value));
        insert(this.cache.get(key));

        // If cache size is greater than capcity then delete least recently used node
        if (this.cache.size() > this.capacity) {
            Node lru = this.left.next;

            remove(lru);
            cache.remove(lru.key);
        }
    }
}
