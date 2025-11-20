/*
Approaching Fibonacci - Numerator Interview

Have the function approachingFibonacci(arr) take the arr parameter,
which will be a list of integers, and determine the smallest positive
integer (including zero) that can be added to the array so that the
sum becomes the next closest Fibonacci number.

Example:
    arr = [15, 1, 3] → sum = 19 → next Fibonacci = 21 → answer = 2
*/
package algorithms.dynamic_programming.one_dimensional;

public class ApproachingFibonacci {

    // Algorithm(s) Used: Dynammic Programming, Fibonacci Sequence
    // Time Complexity: O(log F), where F is the size of the next Fibonacci number
    // Space Complexity: O(1)
    public int approachingFibonacci(int[] arr) {
        int total_sum = 0;
        for (int x : arr) total_sum += x;

        int a = 0, b = 1;

        // Handle case where total_sum is 0 (the smallest Fibonacci >= 0 is 0)
        if (a >= total_sum) return a - total_sum;

        // Generate Fibonacci numbers until reach or exceed total_sum
        while (b < total_sum) {
            int tmp = a;
            a = b;
            b = tmp + b;
        }

        return b - total_sum;  // b is now smallest Fibonacci number ≥ total_sum
    }
}
