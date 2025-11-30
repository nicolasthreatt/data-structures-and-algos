/*
Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

Given the heads of two singly linked-lists headA and headB,
return the node at which the two lists intersect.

If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:
The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

The inputs to the judge are given as follows (your program is not given these inputs):
    * intersectVal - The value of the node where the intersection occurs.
                    This is 0 if there is no intersected node.
    * listA - First linked list.
    * listB - Second linked list.
    * skipA - Number of nodes to skip ahead in listA (starting from head) to get to intersected node.
    * skipB - Number of nodes to skip ahead in listB (starting from head) to get to intersected node.
    * The judge will then create the linked structure based on these inputs and pass the two heads,
      headA and headB to your program.
    * If you correctly return the intersected node, then your solution will be accepted.

Example 1:
    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    Output: Intersected at '8'

Example 2:
    Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    Output: Intersected at '2'

Example 3:
    Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
    Output: No intersection

Constraints:
    * The number of nodes of listA is in the m.
    * The number of nodes of listB is in the n.
    * 1 <= m, n <= 3 * 104
    * 1 <= Node.val <= 105
    * 0 <= skipA <= m
    * 0 <= skipB <= n
    * intersectVal is 0 if listA and listB do not intersect.
    * intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

Follow up:
    Could you write a solution that runs in O(m + n) time and use only O(1) memory?
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

class GetIntersectionNode {
public:

    // Algorithm(s) Used: Linked List Traversal
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    ListNode *getIntersectionNodeI(ListNode *headA, ListNode *headB) {
        if (headA == nullptr || headB == nullptr) return nullptr;

        ListNode *a = headA, *b = headB;
        while (a != nullptr || b != nullptr) {
            if (a == b) return a;
            if (a != nullptr) a = a->next; else a = headB;
            if (b != nullptr) b = b->next; else b = headA;
        }
        return nullptr;
        
    }

        // Algorithm(s) Used: Linked List Traversal
        // Time Complexity: O(n)
        // Space Complexity: O(n)
    ListNode *getIntersectionNodeII(ListNode *headA, ListNode *headB) {
        if (headA == nullptr || headB == nullptr) return nullptr;

        ListNode *a = headA, *b = headB;
        while (a != b) {
            if (a != nullptr) a = a->next; else a = headB;
            if (b != nullptr) b = b->next; else b = headA;
        }
        return a;
    }
};

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

// Helper to build two lists with intersection
tuple<ListNode*, ListNode*, ListNode*> build_intersecting_lists(
    const vector<int>& A,
    const vector<int>& B,
    int skipA,
    int skipB
) {
    auto [headA, nodesA] = build_list(A);
    auto [headB, nodesB] = build_list(B);

    if (skipA == -1 || skipB == -1)
        return {headA, headB, nullptr};

    nodesB[skipB]->next = nodesA[skipA];
    return {headA, headB, nodesA[skipA]};
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
    // <listA, listB, skipA, skipB, intersectionVal>
    vector<tuple<vector<int>, vector<int>, int, int, int>> test_cases = {
        {{4,1,8,4,5}, {5,6,1,8,4,5}, 2, 3, 8},
        {{1,9,1,2,4}, {3,2,4},       3, 1, 2},
        {{2,6,4},     {1,5},        -1, -1, -1},
        {{1},         {1},          -1, -1, -1},
        {{1,2,3},     {4,5},        -1, -1, -1}
    };

    GetIntersectionNode solultion;

    for (auto func : { &GetIntersectionNode::getIntersectionNodeI,
                    &GetIntersectionNode::getIntersectionNodeII }) {
        for (auto& [listA, listB, skipA, skipB, expectedVal] : test_cases) {

            auto [headA, headB, expectedNode] =
                build_intersecting_lists(listA, listB, skipA, skipB);

            ListNode* result = (solultion.*func)(headA, headB);

            if (expectedNode == nullptr) {
                assert(result == nullptr);
            } else {
                assert(result == expectedNode);
                assert(result->val == expectedVal);
            }

            // Free memory without double-free on intersection
            free_list(headB, expectedNode);
            free_list(headA);
        }
    }

    return 0;
}
