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

#include <cassert>
#include <tuple>
#include <unordered_map>
#include <vector>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class CopyRandomList {
public:

    // Algorithm(s) Used: Hash Map, Two Passes
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    Node* copyRandomListI(Node* head) {

        unordered_map<Node*, Node*> mapper = {};
        mapper[nullptr] = nullptr;  // {old: new}

        // Map the old node to the copy node (1st Pass)
        Node* first = head;
        while (first) {
            mapper[first] = new Node(first->val); 

            first = first->next;
        }

        // Connect nodes (2nd Pass)
        Node* second = head;
        while (second) {
            Node *copy = mapper.at(second);
            copy->next = mapper.at(second->next);
            copy->random = mapper.at(second->random);

            second = second->next;
        }

        return mapper.at(head);
    }
};

// Helper function build random list
Node* build_random_list(const vector<pair<int, int>>& data) {
    if (data.empty()) return nullptr;

    vector<Node*> nodes;
    for (auto& [val, _] : data)
        nodes.push_back(new Node(val));

    for (int i = 0; i < (int)nodes.size() - 1; i++)
        nodes[i]->next = nodes[i + 1];

    for (int i = 0; i < (int)data.size(); i++) {
        int rand_idx = data[i].second;
        if (rand_idx != -1)
            nodes[i]->random = nodes[rand_idx];
    }

    return nodes[0];
}

// Helper function convert random list to representation
vector<pair<int, int>> random_list_to_repr(Node* head) {
    vector<Node*> nodes;
    unordered_map<Node*, int> index;

    Node* second = head;
    int i = 0;
    while (second) {
        nodes.push_back(second);
        index[second] = i++;
        second = second->next;
    }

    vector<pair<int, int>> result;
    for (Node* node : nodes) {
        int rand_idx = node->random ? index[node->random] : -1;
        result.push_back({node->val, rand_idx});
    }

    return result;
}

// Helper function verify deep copy
void assert_deep_copy(Node* original, Node* copy) {
    while (original && copy) {
        assert(original != copy);
        assert(original->val == copy->val);
        original = original->next;
        copy = copy->next;
    }
}

int main() {
    CopyRandomList Solution;

    // random_index == -1 == null
    vector<tuple<vector<pair<int,int>>, vector<pair<int,int>>>> test_cases = {
        {
            {{7,-1},{13,0},{11,4},{10,2},{1,0}},
            {{7,-1},{13,0},{11,4},{10,2},{1,0}}
        },
        {
            {{1,1},{2,1}},
            {{1,1},{2,1}}
        },
        {
            {{3,-1},{3,0},{3,-1}},
            {{3,-1},{3,0},{3,-1}}
        },
        {
            {},
            {}
        },
        {
            {{1,-1}},
            {{1,-1}}
        }
    };

    vector<Node* (CopyRandomList::*)(Node*)> funcs = {
        &CopyRandomList::copyRandomListI,
    };

    for (auto func : funcs) {
        for (auto& [input, expected] : test_cases) {
            Node* head = build_random_list(input);
            Node* copied = (Solution.*func)(head);

            assert(random_list_to_repr(copied) == expected);
            assert_deep_copy(head, copied);
        }
    }

    return 0;
}
