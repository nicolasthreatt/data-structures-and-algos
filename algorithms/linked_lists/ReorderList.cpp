/*
Reorder List
https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list.

The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes.
Only nodes themselves may be changed.

Example 1:
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]

Example 2:
    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]

Constraints:
    * The number of nodes in the list is in the range [1, 5 * 10^4].
    * 1 <= Node.val <= 1000
*/

#include <vector>
#include <tuple>
#include <cassert>

using namespace std;

//  Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class ReorderList {

public:
    // Algorithm(s) Used: Two Pointers, Two Passes, Reverse, Floyd's Tortoise & Hare
    // Time Complexity: O(3n) = O(n)
    // Space Complexity: O(1)
    void reorderListI(ListNode* head) {
        if (!head || !head->next) {
            return;
        }

        // Find Middle Node To Get Second Half of List
        ListNode* mid = find_middle(head);

        // Reverse Second Half of List
        ListNode* second = reverse(mid->next);  // Second half only
        mid->next = nullptr;                    // End Second Half

        // Merge Two Halves
        merge(head, second);
    }

private:
    // Algorithm(s) Used: Floyd's Tortoise & Hare
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    ListNode* find_middle(ListNode* head) {
        ListNode *slow = head;
        ListNode *fast = head->next;

        while (fast &&  fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        return slow;
    }

    // Algorithm(s) Used: Reverse Linked List, Iteration
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    ListNode* reverse(ListNode* node) {
        ListNode* prev = nullptr;

        while (node) {
            ListNode* nxt = node->next;

            node->next = prev;
            prev = node;

            node = nxt;
        }

        return prev;
    }

    // Algorithm(s) Used: Merge Linked List, Iteration
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    void merge(ListNode* first, ListNode* second) {
        while (second) {
            ListNode* nxt1 = first->next;
            ListNode* nxt2 = second->next;

            first->next = second;  // Swap Nodes
            second->next = nxt1;    // Swap Nodes

            first = nxt1;
            second = nxt2;
        }
    }
};

// Helper function to build linked list from vector
ListNode* build_list(const vector<int>& values) {
    ListNode dummy;
    ListNode* tail = &dummy;

    for (int v : values) {
        tail->next = new ListNode(v);
        tail = tail->next;
    }
    return dummy.next;
}

// Helper function to convert linked list to vector
vector<int> to_vector(ListNode* head) {
    vector<int> result;
    while (head) {
        result.push_back(head->val);
        head = head->next;
    }
    return result;
}

int main() {
    ReorderList Solution;

    // (input, expected)
    vector<tuple<vector<int>, vector<int>>> test_cases = {
        {{1,2,3,4},     {1,4,2,3}},
        {{1,2,3,4,5},   {1,5,2,4,3}},
        {{1},           {1}},
        {{1,2},         {1,2}},
        {{1,2,3},       {1,3,2}},
        {{1,2,3,4,5,6}, {1,6,2,5,3,4}},
    };

    vector<void (ReorderList::*)(ListNode*)> functions = {
        &ReorderList::reorderListI,
    };

    for (auto func : functions) {
        for (auto& [input, expected] : test_cases) {
            ListNode* head = build_list(input);

            (Solution.*func)(head);
            vector<int> output = to_vector(head);

            assert(output == expected);
        }
    }

    return 0;
}
