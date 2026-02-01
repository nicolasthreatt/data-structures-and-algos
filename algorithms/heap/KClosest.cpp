/*
K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).

You may return the answer in any order.
The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
    Input: points = [[1,3],[-2,2]], k = 1
    Output: [[-2,2]]
    Explanation:
        The distance between (1, 3) and the origin is sqrt(10).
        The distance between (-2, 2) and the origin is sqrt(8).
        Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
        We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
    Input: points = [[3,3],[5,-1],[-2,4]], k = 2
    Output: [[3,3],[-2,4]]
    Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:
    * 1 <= k <= points.length <= 10^4
    * -10^4 < xi, yi < 10^4
*/

#include <cassert>
#include <functional>
#include <queue>
#include <vector>

using namespace std;

class KClosest {
private:
    int dist(const vector<int>& coords) {
        int x = coords[0];
        int y = coords[1];

        return x * x + y * y;
    }

public:

    // Algorithm(s) Used: Sorting
    // Time Complexity: O(nlog(n))
    // Space Complexity: O(1)
    vector<vector<int>> kClosestI(vector<vector<int>>& points, int k) {
        sort(
            points.begin(),
            points.end(),
            [this](const vector<int>& a, const vector<int>& b) {
                return dist(a) < dist(b);
            }
        );

        return vector<vector<int>>(points.begin(), points.begin() + k);
    }

    // Algorithm Used: Min Heap, Two Passes
    // Time Complexity: O(n + klog(n))
    // Space Complexity: O(k)
    vector<vector<int>> kClosestII(vector<vector<int>>& points, int k) {
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> min_heap;

        for(vector<int>& p : points) {
            min_heap.push(p);
        }

        vector<vector<int>> closest_points;
        for (int i = 0; i < k; i++) {
            closest_points.push_back(min_heap.top());
            min_heap.pop();
        }

        return closest_points;
    }

    // Algorithm Used: Max Heap, Single Passes
    // Time Complexity: O(klog(n))
    // Space Complexity: O(k)
    vector<vector<int>> kClosestIII(vector<vector<int>>& points, int k) {
        priority_queue<vector<int>, vector<vector<int>>> max_heap;

        for (vector<int>& p : points) {
            max_heap.push(p);
            if (max_heap.size() > k) {
                max_heap.pop();  // Removes farthest distance
            }
        }

        vector<vector<int>> closest_points;
        for (int i = 0; i < k; i++) {
            closest_points.push_back(max_heap.top());
            max_heap.pop();
        }

        return closest_points;
    }
};

int main() {
    KClosest Solution;

    // (points, k)
    vector<tuple<vector<vector<int>>, int>> test_cases = {
        { {{1, 3}, {-2, 2}}, 1 },
        { {{3, 3}, {5, -1}, {-2, 4}}, 2 },
        { {{0, 1}, {1, 0}}, 1 },
        { {{1, 1}, {2, 2}, {3, 3}}, 2 },
        { {{5, 5}}, 1 },
    };

    vector<vector<vector<int>>(KClosest::*)(vector<vector<int>>&, int)> funcs = {
        &KClosest::kClosestI,
        &KClosest::kClosestII,
        &KClosest::kClosestIII,
    };

    for (auto &tc : test_cases) {
        vector<vector<int>> points;
        int k;
        tie(points, k) = tc;

        for (auto &func : funcs) {
            auto result = (Solution.*func)(points, k);

            assert((int)result.size() == k);

            for (auto &p : result) {
                bool found = false;
                for (auto &q : points) {
                    if (p == q) {
                        found = true;
                        break;
                    }
                }
                assert(found);
            }
        }
    }

    return 0;
}
