/*
Kth Largest Element in a Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Design a class to find the kth largest element in a stream.
NOTE: The kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
    * KthLargest(int k, int[] nums)
        - Initializes the object with the integer k and the stream of integers nums.
    * int add(int val)
        - Appends the integer val to the stream and
          returns the element representing the kth largest element in the stream.

Input
    - ["KthLargest", "add", "add", "add", "add", "add"]
    - [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

Output
    - [null, 4, 5, 5, 8, 8]
    
Explanation
    - KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
    - kthLargest.add(3);   // return 4
    - kthLargest.add(5);   // return 5
    - kthLargest.add(10);  // return 5
    - kthLargest.add(9);   // return 8
    - kthLargest.add(4);   // return 8

Constraints:
    * 1 <= k <= 10^4
    * 0 <= nums.length <= 10^4
    * -10^4 <= nums[i] <= 10^4
    * -10^4 <= val <= 10^4
    * At most 10^4 calls will be made to add.
    * Guaranteed that there will be at least k elements in the array when search for the element.
*/

#include <cassert>
#include <functional>
#include <queue>
#include <vector>

using namespace std;

class KthLargest {
private:
    int k;
    priority_queue<int, vector<int>, greater<int>> min_heap;
    // priority_queue<int> max_heap;

public:
    // Algorithm(s) Used: Heap
    // Time Complexity: (klog(k))
    // Space Complexity: O(k)
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (int num : nums) add(num);  // Iterate through "stream"
    }

    // Algorithm(s) Used: Heap
    // Time Complexity: (log(k))
    // Space Complexity: O(k)
    int add(int val) {

        // Add to heap if under k items or val exceeds current kth-largest
        if (min_heap.size() < k || min_heap.top() < val) {
            min_heap.push(val);
            if (min_heap.size() > k) min_heap.pop();  // If heap became too large, remove top element
        }

        return min_heap.top();
    }
};

int main() {
    vector<int> nums = {4, 5, 8, 2};
    KthLargest kthLargest(3, nums);

    assert(kthLargest.add(3)  == 4);
    assert(kthLargest.add(5)  == 5);
    assert(kthLargest.add(10) == 5);
    assert(kthLargest.add(9)  == 8);
    assert(kthLargest.add(4)  == 8);

    return 0;
}
