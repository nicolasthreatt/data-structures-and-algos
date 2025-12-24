/*
Largest Perimeter Triangle
https://leetcode.com/problems/largest-perimeter-triangle/

Given an integer array nums,
return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths.

If it is impossible to form any triangle of a non-zero area, return 0.

Example 1:
    Input: nums = [2,1,2]
    Output: 5
    Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
Example 2:
    Input: nums = [1,2,1,10]
    Output: 0
    Explanation: 
        - You cannot use the side lengths 1, 1, and 2 to form a triangle.
        - You cannot use the side lengths 1, 1, and 10 to form a triangle.
        - You cannot use the side lengths 1, 2, and 10 to form a triangle.
        - As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.

Constraints:
    - 3 <= nums.length <= 10^4
    - 1 <= nums[i] <= 10^6
*/

#include <cassert>
#include <vector>

using namespace std;

class LargestPerimeterTriangle {
public:

    // Algorithm(s) Used: Greedy
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    int largestPerimeterI(vector<int>& nums) {
        sort(nums.begin(), nums.end(), greater<int>());

        for (int i = 2; i < nums.size(); i++) {
            int a = nums[i], b = nums[i - 1], c = nums[i - 2];
            if (c < a + b) {       // Greedy Choice - Valid Triangle (a <= b <= c)
                return a + b + c;  // Local Solution - Perimeter (a + b + c)
            }
        }

        // Greedy Solution - No Valid Triangle Found
        return 0;
    }
};

int main() {
    LargestPerimeterTriangle Solution;

    // (nums, expected)
    vector<pair<vector<int>, int>> test_cases = {
        {{2, 1, 2}, 5},
        {{1, 2, 1, 10}, 0},
        {{3, 6, 2, 3}, 8},
        {{1, 2, 3}, 0},
        {{10, 15, 7, 5, 8}, 33},
        {{1, 1, 1, 3, 3}, 7},
        {{2, 2, 1}, 5},
        {{1, 1, 2, 2, 3, 4}, 9},
    };

    for (auto& tc : test_cases) {
        vector<int> nums = tc.first;
        int expected = tc.second;
        int result = Solution.largestPerimeterI(nums);
        assert(result == expected);
    }

    return 0;
}
