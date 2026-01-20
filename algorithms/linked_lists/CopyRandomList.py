"""
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
"""

from typing import List, Optional, Tuple


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class CopyRandomList:

    # Algorithm Used: Hash Map, Two Passes
    # Time Complexity: O(n)
    # Memory Complexity: O(n)
    def copyRandomListI(self, head: Optional[Node]) -> Optional[Node]:

        mapper = {None: None}  # {old: new}

        # Map the old node to the copy node (1st Pass)
        current = head
        while current:
            mapper[current] = Node(current.val)

            current = current.next

        # Connect nodes (2nd Pass)
        current = head
        while current:
            copy = mapper[current]

            copy.next = mapper[current.next]
            copy.random = mapper[current.random]

            current = current.next

        return mapper[head]


# Helper function to build random list
def build_random_list(data: List[Tuple[int, Optional[int]]]) -> Optional[Node]:
    if not data:
        return None

    nodes = [Node(val) for val, _ in data]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    for i, (_, rand_idx) in enumerate(data):
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]

    return nodes[0]


# Helper function to convert random list to representation
def random_list_to_repr(head: Optional[Node]) -> List[Tuple[int, Optional[int]]]:
    if not head:
        return []

    nodes = []
    index = {}
    curr = head
    i = 0

    while curr:
        nodes.append(curr)
        index[curr] = i
        curr = curr.next
        i += 1

    result = []
    for node in nodes:
        rand_idx = index[node.random] if node.random else None
        result.append((node.val, rand_idx))

    return result


# Helper function to verify deep copy
def assert_deep_copy(original: Optional[Node], copy: Optional[Node]) -> None:
    curr_o, curr_c = original, copy
    while curr_o and curr_c:
        assert curr_o is not curr_c
        assert curr_o.val == curr_c.val
        curr_o = curr_o.next
        curr_c = curr_c.next


if __name__ == "__main__":
    Solution = CopyRandomList()

    # (input, expected)
    test_cases = [
        ([(7,None),(13,0),(11,4),(10,2),(1,0)],
         [(7,None),(13,0),(11,4),(10,2),(1,0)]),

        ([(1,1),(2,1)],
         [(1,1),(2,1)]),

        ([(3,None),(3,0),(3,None)],
         [(3,None),(3,0),(3,None)]),

        ([], []),
        ([(1,None)], [(1,None)]),
    ]

    funcs = [
        Solution.copyRandomListI,
    ]

    for func in funcs:
        for data, expected in test_cases:
            head = build_random_list(data)
            copied = func(head)

            assert random_list_to_repr(copied) == expected
            assert_deep_copy(head, copied)
