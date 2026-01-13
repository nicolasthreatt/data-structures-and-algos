/*
Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/

You are given an integer array nums consisting of n elements,
and an integer k.

Find a contiguous subarray whose length is equal to k
that has the maximum average value and return this value.

Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
    - Input: nums = [1,12,-5,-6,50,3], k = 4
    - Output: 12.75000
              Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
    - Input: nums = [5], k = 1
    - Output: 5.00000

Constraints:
    * n == nums.length
    * 1 <= k <= n <= 10^5
    * -10^4 <= nums[i] <= 10^4
*/

#include <cassert>
#include <cmath>
#include <tuple>
#include <vector>

using namespace std;

class MaxAvgSubArrayI {
public:

    // Algorithm(s) Used: Sliding Window, Two Pointers
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    double findMaxAverageI(vector<int>& nums, int k) {
        double window_sum = 0.0;
        double max_sum = -INFINITY;  // cmath

        int left = 0;
        for (int right = 0; right < nums.size(); ++right) {
            window_sum += nums[right];

            int window_length = right - left + 1;
            if (window_length == k) {
                max_sum = max(max_sum, window_sum);
                window_sum -= nums[left];
                left++;
            }
        }

        return max_sum / k;
    }

    // Algorithm(s) Used: Fixed Sliding Window
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    double findMaxAverageII(vector<int>& nums, int k) {
        double window_sum = 0;
        for (int i = 0; i < k; ++i) {
            window_sum += nums[i];
        }

        double max_sum = window_sum;

        for (int i = k; i < nums.size(); ++i) {
            window_sum += nums[i] - nums[i - k];
            max_sum = max(max_sum, window_sum);
        }

        return max_sum / k;
    }
};

int main() {
    MaxAvgSubArrayI Solution;

    // (nums, k, expected)
    vector<tuple<vector<int>, int, double>> test_cases = {
        {{1, 12, -5, -6, 50, 3}, 4, 12.75},
        {{5}, 1, 5.0},
        {{0, 0, 0, 0}, 2, 0.0},
        {{4, 2, 1, 3, 3}, 2, 3.0},
        {{-1, -12, -5, -6, -50, -3}, 3, -6.0},
        {{7, 4, 5, 6, 1}, 1, 7.0},
        {{7, 4, 5, 6, 1}, 5, 4.6},
    };

    vector<double (MaxAvgSubArrayI::*)(vector<int>&, int)> funcs = {
        &MaxAvgSubArrayI::findMaxAverageI,
        &MaxAvgSubArrayI::findMaxAverageII,
    };

    const double EPS = 1e-5;

    for (auto func : funcs) {
        for (auto& tc : test_cases) {
            vector<int> nums;
            int k;
            double expected;

            tie(nums, k, expected) = tc;

            double result = (Solution.*func)(nums, k);
            assert(fabs(result - expected) < EPS);  // cmath - abs of a double/floating number
        }
    }

    return 0;
}
