/*
Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.

Example 1:
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
    Input: numRows = 1
    Output: [[1]]

Constraints:
    * 1 <= numRows <= 30
*/

#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

class PascalTriangle {

private:
    vector<vector<int>> memo = {};

public:
    // Algorithm(s) Used: Recursion
    // Time Complexity: O(n^3)
    // Space Complexity: O(n^2) + O(n) (Recursive Stack)
    vector<vector<int>> generateI(int numRows) {
        // Base Case
        if (numRows == 1) {
            return {{1}};
        }

        vector<vector<int>> dp = generateI(numRows - 1);  // Previous Rows (Recursive)
        vector<int> prev = dp.back();                     // Last Row Created

        // Current Row
        vector<int> curr = {1};
        for (int i = 0; i < prev.size() - 1; i += 1) {
            curr.push_back(prev[i] + prev[i + 1]);
        }
        curr.push_back(1);

        dp.push_back(curr);
        return dp;
    }

    // Algorithm(s) Used: Dynammic Programming (1-D), Top-Down, Recursion, Memoization
    // Time Complexity: O(n^2)
    // Space Complexity: O(n^2) + O(n) (Recursive Stack)
    vector<vector<int>> generateII(int numRows) {
        if (memo.size() == numRows) {
            return memo;
        }

        if (numRows == 0) {
            return memo;
        }

        generateII(numRows - 1);  // Previous Rows (Recursive)

        vector<int> curr = {};
        curr.push_back(1);

        // Build Current Row
        if (memo.size()) {
            vector<int> prev = memo.at(memo.size() - 1);

            for (int i = 0; i < prev.size() - 1; ++i) {
                curr.push_back(prev.at(i) + prev.at(i + 1));
            }
            curr.push_back(1);
        }

        memo.push_back(curr);
        return memo;
    }

    // Algorithm(s) Used: Dynammic Programming (1-D), Bottom-Down, Tabulation
    // Time Complexity: O(n^2)
    // Space Complexity: O(n^2)
    vector<vector<int>> generateIII(int numRows) {
        vector<vector<int>> dp = {{1}};

        for (int i = 0; i < numRows - 1; i += 1) {

            vector<int> prev = dp[i];
            vector<int> curr = {1};

            for (int j = 0; j < i; j += 1) {
                curr.push_back(prev[j] + prev[j + 1]);
            }
            curr.push_back(1);

            dp.push_back(curr);
        }

        return dp;
    }
};

int main() {
    PascalTriangle Solution;

    vector<pair<int, vector<vector<int>>>> test_cases = {
        {1, {{1}}},
        {2, {{1}, {1, 1}}},
        {3, {{1}, {1, 1}, {1, 2, 1}}},
        {4, {{1}, {1, 1}, {1, 2, 1}, {1, 3, 3, 1}}},
        {5, {{1}, {1, 1}, {1, 2, 1}, {1, 3, 3, 1}, {1, 4, 6, 4, 1}}},
        {6, {{1}, {1, 1}, {1, 2, 1}, {1, 3, 3, 1}, {1, 4, 6, 4, 1}, {1, 5, 10, 10, 5, 1}}}
    };

    vector<vector<vector<int>> (PascalTriangle::*)(int)> funcs = {
        &PascalTriangle::generateI,
        &PascalTriangle::generateII,
        &PascalTriangle::generateIII
    };

    for (auto func : funcs) {
        for (auto &[numRows, expected] : test_cases) {
            vector<vector<int>> result = (Solution.*func)(numRows);
            assert(result == expected);
        }
    }

    return 0;
}
