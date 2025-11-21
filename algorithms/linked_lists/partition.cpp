/*
Partition List
https://leetcode.com/problems/partition-list

Given the head of a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
    Input: head = [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]

Example 2:
    Input: head = [2,1], x = 2
    Output: [1,2]

Constraints:
    * The number of nodes in the list is in the range [0, 200].
    * -100 <= Node.val <= 100
    * -200 <= x <= 200
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

// Algorithm(s) Used: Dummy Nodes
// Time Complexity: O(n)
// Space Complexity: O(1)
ListNode* partition(ListNode* head, int x) {
    ListNode *dummy_lesser = new ListNode();
    ListNode *dummy_greater = new ListNode();

    ListNode *tail_lesser = dummy_lesser;
    ListNode *tail_greater = dummy_greater;

    while (head != nullptr) {
        if (head->val < x) {
            tail_lesser->next = head;
            tail_lesser = tail_lesser->next;
        } else {
            tail_greater->next = head;
            tail_greater = tail_greater->next;
        }
        head = head->next;
    }

    tail_greater->next = nullptr;
    tail_lesser->next = dummy_greater->next;

    return dummy_lesser->next;
}

int main() {
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

    vector<tuple<vector<int>, int, vector<int>>> tests = {
        {{1,4,3,2,5,2}, 3, {1,2,2,4,3,5}},
        {{2,1},         2, {1,2}},
        {{1,2,3},       4, {1,2,3}},
        {{4,5,6},       3, {4,5,6}},
        {{},            3, {}},
        {{3,3,3},       3, {3,3,3}},
    };

    for (auto& [nums, x, expected] : tests) {
        ListNode* head = build(nums);
        ListNode* result = partition(head, x);
        vector<int> output = to_vec(result);
        assert(output == expected);
    }

    return 0;
}
