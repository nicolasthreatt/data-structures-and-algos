/*
Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Example 2:
    Input: head = [1,2]
    Output: [2,1]

Example 3:
    Input: head = []
    Output: []
 
Constraints:
    * The number of nodes in the list is the range [0, 5000].
    * -5000 <= Node.val <= 5000
 
Follow up:
    - A linked list can be reversed either iteratively or recursively.
    - Could you implement both?
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

// Algorithm(s) Used: Recursion
// Time Complexity: O(n)
// Space Complexity: O(n)
ListNode* reverseListI(ListNode* head) {
    if (head == nullptr) return nullptr;

    ListNode *reverse = head;

    if (head->next != nullptr) {
        reverse = reverseListI(head->next);
        head->next->next = head;
    }
    head->next = nullptr; // End new reversed list 

    return reverse;
}

// Algorithm(s) Used: Two Pointers
// Time Complexity: O(n)
// Space Complexity: O(1)
ListNode* reverseListII(ListNode* head) {
    if (head == nullptr) return nullptr;

    ListNode *prev = nullptr;

    while (head != nullptr) {
        ListNode *tmp = head->next;

        head->next = prev;
        prev = head;

        head = tmp;
    }

    return prev;
}

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
    vector<pair<vector<int>, vector<int>>> test_cases = {
        {{1, 2, 3, 4, 5}, {5, 4, 3, 2, 1}},
        {{1, 2}, {2, 1}},
        {{}, {}},
        {{1}, {1}},
        {{3, 2, 0, -4}, {-4, 0, 2, 3}}
    };

    for (auto func : {reverseListI, reverseListII}) {
        for (auto& [input, expected] : test_cases) {
            ListNode* head = build_list(input);
            ListNode* reversed = func(head);
            vector<int> output = list_to_vector(reversed);
            assert(output == expected);
            free_list(reversed);
        }
    }

    return 0;
}
