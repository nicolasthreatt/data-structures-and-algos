/*
Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.

Example 2:
    Input: head = [1,2,3,4,5,6]
    Output: [4,5,6]
    Explanation: Since list has two middle nodes values 3 and 4, return the second one.

Constraints:
    * The number of nodes in the list is in the range [1, 100].
    * 1 <= Node.val <= 100
*/

#include <cassert>
#include <tuple>
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

class MiddleNode {

public:
    // Algorithm(s) Used: Floyd's Tortoise & Hare
    // Time Complexity: O(n)
    // Space Complexity: O(1) 
    ListNode* middleNodeI(ListNode* head) {
        ListNode *slow = head;
        ListNode *fast = head;

        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }

        return slow;
    }
};

int main() {
    MiddleNode Solution;

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

    vector<pair<vector<int>, vector<int>>> tests = {
        {{1,2,3,4,5},     {3,4,5}},   // Example 1
        {{1,2,3,4,5,6},   {4,5,6}},   // Example 2
        {{1},             {1}},       // Single element
        {{10,20},         {20}},      // Two elements
        {{7,8,9,10},      {9,10}},    // Even count
        {{6,1,4},         {1,4}},     // Odd count
    };

    vector<ListNode* (MiddleNode::*)(ListNode*)> funcs = {
        &MiddleNode::middleNodeI,
    };

    for (auto& func : funcs) {
        for (auto& [input, expected] : tests) {
            ListNode* head = build(input);
            ListNode* mid = (Solution.*func)(head);

            vector<int> output = to_vec(mid);
            assert(output == expected);
        }
    }

    return 0;
}
