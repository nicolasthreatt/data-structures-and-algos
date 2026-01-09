"""
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
"""


class Tribonacci:

    # Algorithm(s) Used: Dynamic Prgramming (1-D), Bottom-Up, Tabulation
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def tribonacciI(self, n: int) -> int:
        tribonacci_seq = [0, 1, 1]

        # If n is less than 3, return the nth number of the Tribonacci sequence.
        if n < 3:
            return tribonacci_seq[n]

        # Calculate the next number of the Tribonacci sequence until we reach the nth number.
        for _ in range(3, n + 1):
            tribonacci_seq = [tribonacci_seq[1], tribonacci_seq[2], sum(tribonacci_seq)]

        return tribonacci_seq[-1]

    # Algorithm(s) Used: Dynamic Prgramming (1-D), Fibonacci Sequence
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def tribonacciII(self, n: int) -> int:
        if n == 0:
            return 0

        if n <= 2:
            return 1

        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c

        return c


if __name__ == "__main__":
    Solution = Tribonacci()

    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 4),
        (10, 149),
        (25, 1389537),
        (37, 2082876103),
    ]

    functions = [
        Solution.tribonacciI,
        Solution.tribonacciII,
    ]

    for func in functions:
        for n, expected in test_cases:
            assert func(n) == expected
