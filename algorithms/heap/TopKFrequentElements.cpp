/*
Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Example 2:
    Input: nums = [1], k = 1
    Output: [1]
 
Constraints:
    * 1 <= nums.length <= 10^5
    * -10^4 <= nums[i] <= 10^4
    * k is in the range [1, the number of unique elements in the array].
    * It is guaranteed that the answer is unique.

Follow up:
    * Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
*/

#include <algorithm>
#include <cassert>
#include <queue>
#include <tuple>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class TopKFrequentElements {
public:
    // Algorithm(s) Used: Max Heap
    // Time Complexity: O(n*log(k))
    // Space Complexity: O(n)
    vector<int> topKFrequentI(vector<int>& nums, int k) {
        unordered_map<int, int> freqs;
        for (int num : nums) {
            freqs[num] += 1;
        }

        priority_queue<pair<int, int>> max_heap;
        for (const auto& [num, freq] : freqs) {
            max_heap.push({freq, num});
        }

        vector<int> result(k);
        for (int i = 0; i < k; i++) {
            result.push_back(max_heap.top().second);
            max_heap.pop();
        }

        return result;
    }

    // Algorithm(s) Used: Min Heap
    // Time Complexity: O(n*log(k))
    // Space Complexity: O(n)
    vector<int> topKFrequentII(vector<int>& nums, int k) {
        unordered_map<int, int> freqs;
        for (int num : nums) {
            freqs[num] += 1;
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> min_heap;
        for (const auto& [num, freq] : freqs) {
            min_heap.push({freq, num});
            if (min_heap.size() > k) {
                min_heap.pop();
            }
        }

        vector<int> result(k);
        for (int i = k - 1; i >= 0; i--) {
            result[i] = min_heap.top().second;
            min_heap.pop();
        }

        return result;
    }
};

int main() {
    TopKFrequentElements Solution;

    vector<tuple<vector<int>, int, unordered_set<int>>> test_cases = {
        {{1, 1, 1, 2, 2, 3}, 2, {1, 2}},
        {{1}, 1, {1}},
        {{4, 4, 4, 5, 5, 6}, 2, {4, 5}},
        {{7, 7, 8, 8, 9}, 1, {7, 8}},
        {{10, 10, 10, 20, 20, 30}, 3, {10, 20, 30}},
        {{-1, -1, -2, -2, -2, 3}, 2, {-2, -1}},
    };

    vector<vector<int>(TopKFrequentElements::*)(vector<int>&, int)> funcs = {
        &TopKFrequentElements::topKFrequentI,
        &TopKFrequentElements::topKFrequentII,
    };

    for (auto& tc : test_cases) {
        vector<int> nums;
        int k;

        unordered_set<int> expected;
        tie(nums, k, expected) = tc;

        for (auto& func : funcs) {
            vector<int> nums_copy = nums;
            vector<int> result = (Solution.*func)(nums_copy, k);

            assert(static_cast<int>(result.size()) == k);
            for (int num : result) {
                assert(expected.count(num) == 1);
            }
        }
    }

    return 0;
}
