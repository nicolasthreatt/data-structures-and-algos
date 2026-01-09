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
package algorithms.dynamic_programming;

import java.util.HashMap;

public class Fibonacci {

    private HashMap<Integer, Integer> memo = new HashMap<>();

    // Algorithm(s) Used: Recursion
    // Time Complexity: O(2^n)
    // Space Complexity: O(n)
    public int fibonacciI(int n) {
        if (n <= 1) return n;

        return fibonacciI(n - 1) + fibonacciI(n - 2);
    }

    // Algorithm(s) Used: Dynamic Programming (1-D), Top-Down, Recursion, Memoization
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public int fibonacciII(int n) {
        if (n <= 1) return n;
        if (memo.containsKey(n)) return memo.get(n);

        int fib = fibonacciII(n - 1) + fibonacciI(n - 2);

        memo.put(n, fib);
        return fib;
    }

    // Algorithm(s) Used: Dynamic Programming (1-D), Bottom-Up, Tabulation
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public int fibonacciIII(int n) {
        if (n <= 1) return n;

        int[] fib = new int[n];

        for (int i = 0; i <= n; i++) {
            if (i <= 1) {
                fib[i] = 0;
            } else {
                fib[i] = fib[i - 1] + fib[i - 2];
            }
        }

        return fib[n];
    }

    // Algorithm(s) Used: Dynamic Programming (1-D), Bottom-Up, Tabulation
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public int fibonacciIV(int n) {
        if (n <= 1) return n;

        int prev = 0, curr = 0;

        for (int i = 2; i <= n; i++) {
            int tmp = prev;
            prev = curr;
            curr = tmp + curr;
        }

        return curr;
    }
}
