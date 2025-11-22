/*
Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

Example 1:
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5

Example 2:
    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4

Constraints:
    * 1 <= k <= nums.length <= 10^5
    * -10^4 <= nums[i] <= 10^4 
*/

#include <cassert>
#include <functional>
#include <queue>
#include <vector>

using namespace std;

// Algorithm(s) Used: Min Heap
// Time Complexity: O(nlog(k))
// Space Complexity: O(k)
int findKthLargest(vector<int>& nums, int k) {
    priority_queue<int, vector<int>, greater<int>> minHeap;
    // priority_queue<int> max_heap;

    for (int num : nums) {
        if (minHeap.size() < k || minHeap.top() < num) {
            minHeap.push(num);
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
    }

    return minHeap.top();
}

int main() {
    vector<tuple<vector<int>, int, int>> test_cases = {
        {{3,2,1,5,6,4}, 2, 5},
        {{3,2,3,1,2,4,5,5,6}, 4, 4},
        {{1}, 1, 1},
        {{2,1}, 1, 2},
        {{2,1}, 2, 1},
        {{7,10,4,3,20,15}, 3, 10},
    };

    for (auto &tc : test_cases) {
        vector<int> nums;
        int k, expected;
        tie(nums, k, expected) = tc;
        assert(findKthLargest(nums, k) == expected);
    }

    return 0;
}
