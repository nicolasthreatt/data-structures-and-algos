/*
Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list.
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input: list1 = [], list2 = []
    Output: []

Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

Constraints:
    * The number of nodes in both lists is in the range [0, 50].
    * -100 <= Node.val <= 100
    * Both list1 and list2 are sorted in non-decreasing order.
*/

#include <iostream>
#include <vector>
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

class MergeTwoLists {
public:
    // Algorithm Used: Dummy Node
    // Time Complexity: O(n + m)
    // Space Complexity: O(1)
    ListNode* mergeTwoListsI(ListNode* list1, ListNode* list2) {
        ListNode* dummy = new ListNode();
        ListNode* tail = dummy;

        // Merge the two lists together while both are non-empty
        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val < list2->val) {
                tail->next = list1;
                list1 = list1->next;
            } else {
                tail->next = list2;
                list2 = list2->next;
            }
            tail = tail->next;
        }

        // Append the remaining nodes (only one of these will be non-null)
        if (list1 != nullptr) {
            tail->next = list1;
        } else if (list2 != nullptr) {
            tail->next = list2;
        }

        return dummy->next;
    }
};

// Helper function that creates a linked list from an initializer list of integers
ListNode* createList(initializer_list<int> vals) {
    ListNode dummy;
    ListNode* tail = &dummy;
    for (int v : vals) {
        tail->next = new ListNode(v);
        tail = tail->next;
    }
    return dummy.next;
}

// Helper function that compares two linked lists for equality
bool listsEqual(ListNode* a, ListNode* b) {
    while (a && b) {
        if (a->val != b->val) return false;
        a = a->next;
        b = b->next;
    }
    return a == nullptr && b == nullptr;
}

// Helper function that frees all nodes in a linked list to prevent memory leaks
void freeList(ListNode* head) {
    while (head) {
        ListNode* tmp = head;
        head = head->next;
        delete tmp;
    }
}

int main() {
    MergeTwoLists Solution;

    auto build = [&](const vector<int>& vals) -> ListNode* {
        ListNode dummy;
        ListNode* tail = &dummy;
        for (int v : vals) {
            tail->next = new ListNode(v);
            tail = tail->next;
        }
        return dummy.next;
    };

    auto to_vec = [&](ListNode* head) -> vector<int> {
        vector<int> out;
        while (head) {
            out.push_back(head->val);
            head = head->next;
        }
        return out;
    };

    vector<tuple<vector<int>, vector<int>, vector<int>>> tests = {
        {{1,2,4}, {1,3,4}, {1,1,2,3,4,4}},
        {{},      {},      {}},
        {{},      {0},     {0}},
        {{1,3,5}, {2,4,6,8}, {1,2,3,4,5,6,8}},
        {{1,2,3}, {10,11}, {1,2,3,10,11}},
    };

    vector<ListNode* (MergeTwoLists::*)(ListNode*, ListNode*)> funcs = {
        &MergeTwoLists::mergeTwoListsI,
    };

    for (auto& func : funcs) {
        for (auto& [v1, v2, expected] : tests) {
            ListNode* l1 = build(v1);
            ListNode* l2 = build(v2);

            ListNode* result = (Solution.*func)(l1, l2);
            vector<int> output = to_vec(result);

            assert(output == expected);
        }
    }

    return 0;
}
