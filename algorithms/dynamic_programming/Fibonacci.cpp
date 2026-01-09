/*
Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
      
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1.

That is,
    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Example 1:
    Input: n = 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
    Input: n = 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
    Input: n = 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:
    * 0 <= n <= 30
*/

#include <iostream>
#include <cassert>
#include <vector>

using namespace std;

class Fibonacci {

private:
    unordered_map<int, int> memo = {};

public:
    // Algorithm(s) Used: Recursiion
    // Time Complexity: O(2^n)
    // Space Complexity: O(n)
    int fibonacciI(int n) {
        if (n <= 1) return n;  // Base Case

        return fibonacciI(n - 1) + fibonacciI(n - 2);
    }

    // Algorithm(s) Used: Recursiion, Memoization
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    int fibonacciII(int n) {
        if (n <= 1) return n;  // Base Case
        if (memo.contains(n)) return memo[n];  // Base Case

        int fib = fibonacciII(n - 1) + fibonacciII(n - 2);

        memo[n] = fib;
        return fib;
    }

    // Algorithm(s) Used: Dynamic Programming (1-D), Bottom-Up, Tabulation
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    int fibonacciIII(int n) {
        if (n <= 1) return n;

        vector<int> fib = {0, 1};  // Base Cases
        
        for (int i = 2; i <= n; i++) {
            fib.push_back(fib.at(i - 1) + fib.at(i - 2));
        }

        return fib[n];
    }

    // Algorithm(s) Used: Dynamic Programming (1-D), Bottom-Up, Tabulation
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    int fibonacciIV(int n) {
        if (n <= 1) return n;

        int prev = 0, curr = 1;  // Base Cases

        for (int i = 2; i <= n; i++) {
            int tmp = prev;
            prev = curr;
            curr = tmp + curr;
        }

        return curr;
    }
};

int main() {
    Fibonacci Solution;

    vector<pair<int, int>> test_cases = {
        {0, 0},
        {1, 1},
        {2, 1},
        {3, 2},
        {4, 3},
        {5, 5},
        {6, 8},
        {7, 13},
        {10, 55},
        {15, 610},
        {20, 6765},
        {30, 832040},
    };

    vector<int (Fibonacci::*)(int)> funcs = {
        &Fibonacci::fibonacciI,
        &Fibonacci::fibonacciII,
        &Fibonacci::fibonacciIII,
        &Fibonacci::fibonacciIV
    };

    for (auto func : funcs) {
        for (auto [n, expected] : test_cases) {
            int result = (Solution.*func)(n);
            assert(result == expected);
        }
    }

    return 0;
}
