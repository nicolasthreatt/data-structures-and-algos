/*
Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

Constraints:
    * The number of nodes in each linked list is in the range [1, 100].
    * 0 <= Node.val <= 9
    * It is guaranteed that the list represents a number that does not have leading zeros.
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

class AddTwoNumbers {
public:
    // Algorithm(s) Used: Dummy Node
    // Time Complexity: O(l1 + l2)
    // Space Complexity: O(1)
    ListNode* addTwoNumbersI(ListNode* l1, ListNode* l2) {
        ListNode *dummy = new ListNode();
        ListNode* result = dummy;

        int carry = 0;
        while (l1 || l2 || carry) {
            int a = (l1 != nullptr) ? l1->val : 0;
            int b = (l2 != nullptr) ? l2->val : 0;
            int sum = a + b + carry;

            carry = sum / 10;
            
            int digit = sum % 10;
            dummy->next = new ListNode(digit);
            dummy = dummy->next;

            l1 = (l1 != nullptr) ? l1->next : nullptr;
            l2 = (l2 != nullptr) ? l2->next : nullptr;
        }

        return result->next;
    }
};

// Helper function to build and construct linked list
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
    AddTwoNumbers Solution;

    // (l1, l2, expected)
    vector<tuple<vector<int>, vector<int>, vector<int>>> test_cases = {
        {{2,4,3}, {5,6,4}, {7,0,8}},
        {{0}, {0}, {0}},
        {{9,9,9,9,9,9,9}, {9,9,9,9}, {8,9,9,9,0,0,0,1}},
        {{1}, {9}, {0,1}},
        {{5,5}, {5,5}, {0,1,1}},
        {{1,8}, {0}, {1,8}},
    };

    vector<ListNode* (AddTwoNumbers::*)(ListNode*, ListNode*)> functions = {
        &AddTwoNumbers::addTwoNumbersI,
    };

    for (auto func : functions) {
        for (auto& [v1, v2, expected] : test_cases) {
            ListNode* l1 = build_list(v1);
            ListNode* l2 = build_list(v2);

            ListNode* result = (Solution.*func)(l1, l2);
            vector<int> output = to_vector(result);

            assert(output == expected);
        }
    }

    return 0;
}
