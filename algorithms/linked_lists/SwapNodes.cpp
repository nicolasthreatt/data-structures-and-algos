/*
Swapping Nodes in a Linked List
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the
kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [1,4,3,2,5]

Example 2:
    Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
    Output: [7,9,6,6,8,7,3,0,9,5]

Constraints:
    * The number of nodes in the list is n.
    * 1 <= k <= n <= 10^5
    * 0 <= Node.val <= 100
*/

#include <cassert>
#include <vector>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class SwapNodes {
public:

    // Algorithm(s) Used: Single Pass, Two Pointers
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    ListNode* swapNodesI(ListNode* head, int k) {
        if (!head->next) {
            return head;
        }

        // Find the kth node to be removed from the START
        ListNode* curr = head;
        for (int i = 1; i < k; i++) {  // 1-indexed based
            curr = curr->next;
        }

        // Set LEFT pointer at CURR to store kth node from the START
        ListNode* left = curr;

        // Find the kth node to be removed from the END
        // When loop terminates, RIGHT will be kth node from the END
        ListNode* right = head;
        while (curr->next) {
            curr = curr->next;
            right = right->next;
        }

        // Swap values of the two pointer nodes
        int tmp = left->val;
        left->val = right->val;
        right->val = tmp;

        return head;
    }
};

// Helper to build linked list from vector
ListNode* build_list(const vector<int>& values) {
    if (values.empty()) return nullptr;

    ListNode* head = new ListNode(values[0]);
    ListNode* tail = head;
    for (size_t i = 1; i < values.size(); ++i) {
        tail->next = new ListNode(values[i]);
        tail = tail->next;
    }
    return head;
}

// Helper to convert linked list back to vector
vector<int> list_to_vector(ListNode* head) {
    vector<int> result;
    while (head) {
        result.push_back(head->val);
        head = head->next;
    }
    return result;
}

// Helper to free linked list memory
void free_list(ListNode* head) {
    while (head) {
        ListNode* tmp = head;
        head = head->next;
        delete tmp;
    }
}

int main() {
    SwapNodes Solution;

    // (input list, k, expected list)
    vector<tuple<vector<int>, int, vector<int>>> test_cases = {
        {{1, 2, 3, 4, 5}, 2, {1, 4, 3, 2, 5}},
        {{7, 9, 6, 6, 7, 8, 3, 0, 9, 5}, 5, {7, 9, 6, 6, 8, 7, 3, 0, 9, 5}},
        {{1}, 1, {1}},
        {{1, 2}, 1, {2, 1}},
        {{1, 2}, 2, {2, 1}},
        {{1, 2, 3}, 2, {1, 2, 3}},
        {{10, 20, 30, 40}, 1, {40, 20, 30, 10}},
    };

    vector<ListNode* (SwapNodes::*)(ListNode*, int)> funcs = {
        &SwapNodes::swapNodesI
    };

    for (auto func : funcs) {
        for (auto& tc : test_cases) {
            vector<int> input, expected;
            int k;
            tie(input, k, expected) = tc;

            ListNode* head = build_list(input);
            ListNode* result = (Solution.*func)(head, k);

            vector<int> output = list_to_vector(result);
            assert(output == expected);

            free_list(result);
        }
    }

    return 0;
}
