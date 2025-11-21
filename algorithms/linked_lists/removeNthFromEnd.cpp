/*
Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head

Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]

Constraints:
    * The number of nodes in the list is sz.
    * 1 <= sz <= 30
    * 0 <= Node.val <= 100
    * 1 <= n <= sz

Follow up: Could you do this in one pass?
*/

#include <cassert>
#include <set>
#include <vector>

using namespace std;

//  Definition for singly-linked list
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// Algorithm(s) Used: Iteration, Two Passes
// Time Complexity: O(2n) ≈ O(n)
// Space Complexity: O(1)
ListNode* removeNthFromEndI(ListNode* head, int n) {
    if (head == nullptr) return nullptr;

    int length = 0;
    ListNode *curr;

    // First Pass - Find total length of the list
    curr = head;
    while (curr != nullptr) {
        length += 1;
        curr = curr->next;
    }

    if (length == n) return head->next; // Remove first node if needed

    // Second Pass - Find node before the one to remove
    curr = head;
    for (int i = 0; i < length - n - 1; i++) {
        curr = curr->next;
    }

    curr->next = curr->next->next; // Remove target node

    return head;
}

// Algorithm(s) Used: Reverse Linked List (Helper)
// Time Complexity: O(n)
// Space Complexity: O(1)
ListNode* reverse(ListNode* node) {
    ListNode* prev = nullptr;

    while (node != nullptr) {
        ListNode *nxt = node->next;

        // Reverse Nodes
        node->next = prev;
        prev = node;

        // Move List Forward
        node = nxt;
    }

    return prev;
}

// Algorithm(s) Used: Reverse Linked List
// Time Complexity: O(n)
// Space Complexity: O(1)
ListNode* removeNthFromEndII(ListNode* head, int n) {
    if (head == nullptr) return nullptr;

    head = reverse(head); // Reverse the linked list

    if (n == 1) {
        head = head->next;
    } else {
        ListNode* curr = head;

        // Iterate until reach the node before the one to remove
        for (int i = 0; i < n - 2; i++) curr = curr->next;

        curr->next = curr->next->next; // Remove target node
    }

    return reverse(head); // Reverse back to original order
}

// Algorithm(s) Used: Dummy Node, Two Pointers
// Time Complexity: O(n)
// Space Complexity: O(1)
ListNode* removeNthFromEndIII(ListNode* head, int n) {
    if (head == nullptr) return nullptr;

    ListNode *dummy = new ListNode(0);
    dummy->next = head;

    ListNode *slow = dummy, *fast = dummy;

    // iterate n + 1 steps so slow ends one node before the target when fast ends
    for (int i = 0 ; i < n + 1; i++) fast = fast->next;

    while (fast != nullptr) {
        slow = slow->next;
        fast = fast->next;
    }

    slow->next = slow->next->next;

    return dummy->next;
}

int main() {
    auto buildLinkedList = [&](const vector<int>& values) {
        ListNode* dummy = new ListNode();
        ListNode* tail = dummy;
        for (int v : values) {
            tail->next = new ListNode(v);
            tail = tail->next;
        }
        return dummy->next;
    };

    auto linkedListToVector = [&](ListNode* head) {
        vector<int> result;
        while (head != nullptr) {
            result.push_back(head->val);
            head = head->next;
        }
        return result;
    };

    vector<tuple<vector<int>, int, vector<int>>> test_cases = {
        {{1, 2, 3, 4, 5}, 2, {1, 2, 3, 5}},
        {{1}, 1, {}},
        {{1, 2}, 1, {1}},
        {{1, 2}, 2, {2}},
        {{10, 20, 30, 40}, 3, {10, 30, 40}},
    };

    vector<function<ListNode*(ListNode*, int)>> funcs = {
        removeNthFromEndI,
        removeNthFromEndII,
        removeNthFromEndIII
    };

    for (auto& func : funcs) {
        for (auto& test : test_cases) {
            vector<int> nodes, expected;
            int n;

            tie(nodes, n, expected) = test;

            ListNode* head = buildLinkedList(nodes);
            ListNode* result = func(head, n);
            vector<int> result_vec = linkedListToVector(result);

            assert(result_vec == expected);
        }
    }

    return 0;
}
