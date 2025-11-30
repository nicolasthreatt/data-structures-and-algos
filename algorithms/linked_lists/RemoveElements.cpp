/*
Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/

Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]

Example 2:
    Input: head = [], val = 1
    Output: []

Example 3:
    Input: head = [7,7,7,7], val = 7
    Output: []

Constraints:
    * The number of nodes in the list is in the range [0, 10^4]
    * 1 <= Node.val <= 50
    * 0 <= val <= 50
*/

#include <cassert>
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

class RemoveElements {
public:

    // Algorithm(s) Used: Dummy Node, Two Pointers
    // Time Complexity: O(n)
    // Time Complexity: O(1)
    ListNode* removeElementsI(ListNode* head, int val) {
        ListNode* dummy = new ListNode();
        dummy->next = head;

        ListNode* curr = dummy;
        while (curr->next != nullptr) {
            if (curr->next->val == val) {
                curr->next = curr->next->next;
            } else {
                curr = curr->next;
            }
        }

        return dummy->next;
    }

    // Algorithm(s) Used: Dummy Node
    // Time Complexity: O(n)
    // Time Complexity: O(1)
    ListNode* removeElementsII(ListNode* head, int val) {
        ListNode* dummy = new ListNode(0, head);

        head = dummy;
        while (head->next != nullptr) {
            if (head->next->val == val) {
                head->next = head->next->next;
            } else {
                head = head->next;
            }
        }

        return dummy->next;
    }
};

// Helper to convert linked list back to vector
vector<int> list_to_vector(ListNode* head) {
    vector<int> result;
    while (head) {
        result.push_back(head->val);
        head = head->next;
    }
    return result;
}

// Helper to build a linked list from vector
pair<ListNode*, vector<ListNode*>> build_list(const vector<int>& values) {
    if (values.empty()) return {nullptr, {}};

    vector<ListNode*> nodes;
    nodes.reserve(values.size());
    for (int v : values) nodes.push_back(new ListNode(v));

    for (size_t i = 0; i < nodes.size() - 1; ++i)
        nodes[i]->next = nodes[i + 1];

    return {nodes[0], nodes};
}

// Helper to free linked list memory (safe for intersected lists)
void free_list(ListNode* head, ListNode* stop = nullptr) {
    while (head && head != stop) {
        ListNode* tmp = head;
        head = head->next;
        delete tmp;
    }
}

int main() {
    // <input_list, val_to_remove, expected_output_list>
    vector<tuple<vector<int>, int, vector<int>>> test_cases = {
        {{1,2,6,3,4,5,6}, 6, {1,2,3,4,5}},
        {{},              1, {}},
        {{7,7,7,7},        7, {}},
        {{1,2,3},          4, {1,2,3}},
        {{4,1,4,2,4},      4, {1,2}}
    };

    RemoveElements solution;

    for (auto func : {
            &RemoveElements::removeElementsI,
            &RemoveElements::removeElementsII
        })
    {
        for (auto& [input_list, val, expected_list] : test_cases) {

            auto [head, nodes] = build_list(input_list);

            ListNode* result = (solution.*func)(head, val);
            vector<int> result_vec = list_to_vector(result);

            assert(result_vec == expected_list);

            free_list(result);
        }
    }

    return 0;
}
