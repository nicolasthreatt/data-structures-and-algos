/*
Can Place Flowers
https://leetcode.com/problems/can-place-flowers/

You have a long flowerbed in which some of the plots are planted, and some are not.

However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's,
where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed
without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true

Example 2:
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false

Constraints:
    * 1 <= flowerbed.length <= 2 * 104
    * flowerbed[i] is 0 or 1.
    * There are no two adjacent flowers in flowerbed.
    * 0 <= n <= flowerbed.length
*/

#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class CanPlaceFlowers {
public:
    // Algorithm(s) Used: Greedy, Padding
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    bool canPlaceFlowersI(vector<int>& flowerbed, int n) {
        // Pad Flowerbed At Start and End With 0
        vector<int> flowers(flowerbed.size() + 2, 0);  // {0, flowerbed, 0}

        for (int i = 0; i < flowerbed.size(); ++i) {
            flowers[i + 1] = flowerbed[i];
        }

        // Skip First and Last Elements (Modified 0's)
        for (int i = 1; i < flowers.size() - 1; ++i) {
            bool left_pot_empty = flowers[i - 1] == 0;
            bool curr_pot_empty = flowers[i] == 0;
            bool right_pot_empty = flowers[i + 1] == 0;
            if (left_pot_empty && curr_pot_empty && right_pot_empty) {  // Greedy Choice - Plant Flower
                n -= 1;  // Local Optimal Choice
                flowers[i] = 1;
            }
        }

        return n <= 0;  // Global Optimal Solution
    }

    // Algorithm(s) Used: Greedy
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    bool canPlaceFlowersII(vector<int>& flowerbed, int n) {
        for (int i = 0; i < flowerbed.size(); ++i) {
            bool left_pot_empty = (i == 0) || (flowerbed[i - 1] == 0);
            bool curr_pot_empty = flowerbed[i] == 0;
            bool right_pot_empty = (i == flowerbed.size() - 1) || (flowerbed[i + 1] == 0);
            if (left_pot_empty && curr_pot_empty && right_pot_empty) {  // Greedy Choice - Plant Flower
                n -= 1;  // Local Optimal Choice
                flowerbed[i] = 1;
            }
        }

        return n <= 0;  // Global Optimal Solution
    }
};


int main() {
    CanPlaceFlowers Solution;

    // (flowerbed, n, expected)
    vector<tuple<vector<int>, int, bool>> test_cases = {
        {{1, 0, 0, 0, 1}, 1, true},
        {{1, 0, 0, 0, 1}, 2, false},
        {{0}, 1, true},
        {{0}, 0, true},
        {{1}, 1, false},
        {{0, 0, 0, 0, 0}, 3, true},
        {{0, 0, 1, 0, 0}, 2, true},
        {{0, 0, 1, 0, 0}, 3, false},
        {{1, 0, 0, 0, 0, 1}, 2, false},
        {{0, 0, 0}, 2, true},
    };

    vector<bool (CanPlaceFlowers::*)(vector<int>&, int)> funcs = {
        &CanPlaceFlowers::canPlaceFlowersI,
        &CanPlaceFlowers::canPlaceFlowersII
    };

    for (auto func : funcs) {
        for (auto& tc : test_cases) {
            vector<int> flowerbed;
            int n;
            bool expected;
            tie(flowerbed, n, expected) = tc;

            bool result = (Solution.*func)(flowerbed, n);
            assert(result == expected);
        }
    }

    return 0;
}
