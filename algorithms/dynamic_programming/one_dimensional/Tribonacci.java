/*
N-th Tribonacci Number
https://leetcode.com/problems/n-th-tribonacci-number/

The Tribonacci sequence Tn is defined as follows:
    T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:
    Input: n = 4
    Output: 4
    Explanation:
        T_3 = 0 + 1 + 1 = 2
        T_4 = 1 + 1 + 2 = 4

Example 2:
    Input: n = 25
    Output: 1389537

Constraints:
    * 0 <= n <= 37
    * The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
 */
package algorithms.dynamic_programming.one_dimensional;

public class Tribonacci {

    // Algorithm(s) Used: Dynamic Prgramming (1-D), Bottom-Up
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public int tribonacciI(int n) {
        int[] tribonacci_seq = {0, 1, 1};

        if (n <= 2) return tribonacci_seq[n];

        for (int i = 3; i < n + 1; i ++) {
            int a = tribonacci_seq[0], b = tribonacci_seq[1], c = tribonacci_seq[2];
            int d = a + b + c;

            tribonacci_seq = new int[] {a, b, d};
        }

        return tribonacci_seq[2];
    }

    // Algorithm(s) Used: Dynamic Prgramming (1-D), Bottom-Up
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public int tribonacciII(int n) {
        if (n == 0) return 0;
        if (n <= 2) return 1;

        int a = 0, b = 1, c = 1;
        
        for (int i = 3; i < n + 1; i++) {
            int aTmp = a;
            int bTmp = b;
            int cTmp = c;

            a = b;
            b = c;
            c = aTmp + bTmp + cTmp;
        }

        return c;
    }
}
