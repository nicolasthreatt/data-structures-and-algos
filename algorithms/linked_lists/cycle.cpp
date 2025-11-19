/*
Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by
continuously following the next pointer.

Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 1st node.

Example 2:
    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.
 
Constraints:
    * The number of the nodes in the list is in the range [0, 104].
    * -10^5 <= Node.val <= 10^5
    * pos is -1 or a valid index in the linked-list.

Follow up:
    * Can you solve it using O(1) (i.e. constant) memory?
*/

#include <cassert>
#include <set>
#include <vector>

using namespace std;

//  Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// Algorithm(s) Used: Hashmap
// Time Complexity: O(n)
// Space Complexity: O(n)
bool hasCycleI(ListNode *head) {
    set<ListNode*> nodes;

    ListNode *curr = head;
    while (curr != nullptr) {
        if (nodes.contains(curr)) return true;
        nodes.insert(curr);
        curr = curr->next;
    }

    return false;
}

// Algorithm(s) Used: Two Pointers, Floyd's Tortoise & Hare
// Time Complexity: O(n)
// Space Complexity: O(n)
bool hasCycleII(ListNode *head) {
    ListNode *slow = head, *fast = head;

    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }

    return false;
}

// Helper function to build and construct linked list
ListNode* build_list(const vector<int>& values, int pos) {
    if (values.empty()) return nullptr;

    vector<ListNode*> nodes;
    for (int v : values) nodes.push_back(new ListNode(v));

    for (int i = 0; i < (int)nodes.size() - 1; i++)
        nodes[i]->next = nodes[i + 1];

    if (pos != -1)
        nodes.back()->next = nodes[pos];

    return nodes[0];
}

int main() {
    vector<tuple<vector<int>, int, bool>> test_cases = {
        {{3,2,0,-4}, 1, true},
        {{1,2}, 0, true},
        {{1}, -1, false},
        {{}, -1, false},
        {{1,2,3,4,5}, -1, false},
        {{1,2,3}, 2, true},
    };

    vector<bool(*)(ListNode*)> functions = {
        hasCycleI,
        hasCycleII,
    };

    for (auto func : functions) {
        for (auto& tc : test_cases) {
            const vector<int>& values = get<0>(tc);
            int pos = get<1>(tc);
            bool expected = get<2>(tc);

            ListNode* head = build_list(values, pos);
            assert(func(head) == expected);
        }
    }

    return 0; // All tests passed
}