"""
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
"""


# Definition for doubly-linked list.
class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev = None
        self.next = None


# Algorithm Used: Hash Map, Two Pointers, Double-Linked List
# Time Complexity: O(1)
# Memory Complexity: O(1)
class LRUCacheI:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # {key: node}

        # Double (Left, Right) Linked List
        self.left = Node(0, 0)   # Least Recently Used
        self.right = Node(0, 0)  # Most Recently Used

        # Establish bi-connection between the nodes
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node: Node):
        """Remove current node from a double linked list, O(1)."""
        prv = node.prev
        nxt = node.next

        prv.next = nxt
        nxt.prev = prv

    def _insert(self, node: Node):
        """Insert nodes on the right side of a double linked list, O(1)."""
        prv = self.right.prev
        nxt = self.right

        prv.next = node
        nxt.prev = node
        
        node.prev = prv
        node.next = nxt

    def get(self, key: int) -> int:
        """Returns value key if key exists, otherwise -1."""
        if key in self.cache:
            self._remove(self.cache[key])  # Update with most recent key
            self._insert(self.cache[key])  # Update with most recent key

            return self.cache[key].val

        return -1

    def put(self, key: int, value: int):
        """Update value of key if key exists."""
        if key in self.cache:
            self._remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        # If cache size is greater than capcity then delete least recently used node
        if len(self.cache) > self.capacity:
            lru = self.left.next

            self._remove(lru)
            del self.cache[lru.key]


if __name__ == "__main__":

    cache = LRUCacheI(2)

    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1

    cache.put(3, 3)
    assert cache.get(2) == -1

    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    cache = LRUCacheI(1)

    cache.put(1, 10)
    assert cache.get(1) == 10

    cache.put(2, 20)
    assert cache.get(1) == -1
    assert cache.get(2) == 20

    cache = LRUCacheI(2)

    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)

    assert cache.get(1) == 10

    cache.put(3, 3)
    assert cache.get(2) == -1
    assert cache.get(3) == 3

    cache = LRUCacheI(2)

    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)

    assert cache.get(2) == -1
    assert cache.get(1) == 1
    assert cache.get(3) == 3
