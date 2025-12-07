/*
Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
    Input: head = [1,2,2,1]
    Output: true

Example 2:
    Input: head = [1,2]
    Output: false

Constraints:
    * The number of nodes in the list is in the range [1, 10^5].
    * 0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
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

class PalindromeLinkedList {
private:
    // Algorithm(s) Used: Linked List Iteration
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    vector<int> converToList(ListNode* head) {
        vector<int> nodes;

        while (head) {
            nodes.push_back(head->val);
            head = head->next;
        }

        return nodes;
    }

    // Algorithm(s) Used: Floyd's Tortoise & Hare
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    ListNode* findMiddleNode(ListNode* head) {
        ListNode *slow = head, *fast = head;
        while (fast && fast-> next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }

    // Algorithm(s) Used: Reverse Linked List
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    ListNode* reverse(ListNode* head) {
        ListNode *prev = nullptr;

        while (head) {
            ListNode* nxt = head->next;
            head->next = prev;
            prev = head;
            head = nxt;
        }

        return prev;
    }

public:
    // Algorithm(s) Used: List, Binary Search
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    bool isPalindromeI(ListNode* head) {
        if (!head) return true;

        vector<int> nodes = converToList(head);

        int left = 0, right = nodes.size() - 1;
        while (left < right) {
            if (nodes[left] != nodes[right]) {
                return false;
            }
            left += 1;
            right -= 1;
        }

        return true;
    }

    // Algorithm(s) Used: Floyd's Tortoise & Hare, Reverse Linked List
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    bool isPalindromeII(ListNode* head) {
        if (!head) return true; 

        ListNode *middle = findMiddleNode(head);
        ListNode *reversed = reverse(middle);

        while (reversed) {
            if (reversed->val != head-> val) {
                return false;
            }
            reversed = reversed->next;
            head = head->next;
        }

        return true;
    }
};

int main() {
    auto build_list = [](const vector<int>& values) {
        ListNode* dummy = new ListNode();
        ListNode* tail = dummy;
        for (int v : values) {
            tail->next = new ListNode(v);
            tail = tail->next;
        }
        return dummy->next;
    };

    auto list_to_vector = [](ListNode* head) {
        vector<int> result;
        while (head) {
            result.push_back(head->val);
            head = head->next;
        }
        return result;
    };

    auto free_list = [](ListNode* head) {
        while (head) {
            ListNode* tmp = head;
            head = head->next;
            delete tmp;
        }
    };

    // <input_list, expected_output>
    vector<tuple<vector<int>, bool>> test_cases = {
        {{1, 2, 2, 1}, true},
        {{1, 2}, false},
        {{1, 2, 3, 2, 1}, true},
        {{7}, true},
        {{}, true},
        {{1, 0, 1, 2}, false},
        {{3, 3}, true},
        {{3, 3, 3, 3}, true}
    };

    PalindromeLinkedList Solution;

    for (auto func : {
            &PalindromeLinkedList::isPalindromeI,
            &PalindromeLinkedList::isPalindromeII
        })
    {
        for (auto& [input_list, expected] : test_cases) {
            ListNode* head = build_list(input_list);

            bool result = (Solution.*func)(head);
            assert(result == expected);

            free_list(head);
        }
    }

    return 0;
}
