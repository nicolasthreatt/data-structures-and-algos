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

package algorithms.dynamic_programming;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class PascalTriangle {

    private List<List<Integer>> memo = new ArrayList<>();

    // Algorithm(s) Used: Recursion
    // Time Complexity: O(n^3)
    // Space Complexity: O(n^2) + O(n) (Recursive Stack)
    public List<List<Integer>> generateI(int numRows) {
        // Base Case
        if (numRows == 1) {
            List<List<Integer>> dp = new ArrayList<>();
            dp.add(new ArrayList<>(Arrays.asList(1)));
            return dp;
        }

        List<List<Integer>> prevs = generateI(numRows - 1);  // Previous Rows (Recursive)
        List<Integer> last = prevs.get(prevs.size() - 1);    // Last Row Created

        // Build Current Row
        List<Integer> curr = new ArrayList<>();
        curr.add(1);
        for (int i = 0; i < last.size(); ++i) {
            curr.add(last.get(i) + last.get(i + 1));
        }
        curr.add(1);

        prevs.add(curr);  // Add Current Row to Previously Generated Rows
        return prevs;
    }

    // Algorithm(s) Used: Dynammic Programming (1-D), Top-Down, Recursion, Memoization
    // Time Complexity: O(n^2)
    // Space Complexity: O(n^2) + O(n) (Recursive Stack)
    public List<List<Integer>> generateII(int numRows) {
        if (numRows == 0) {
            return memo;
        }

        if (memo.size() == numRows) {
            return memo;
        }

        generateII(numRows - 1);

        // Build Current Row
        List<Integer> curr = new ArrayList<>();

        curr.add(1);
        if (memo.size() > 0) {
            List<Integer> last = memo.get(memo.size() - 1);    // Last Row Created
            for (int i = 0; i < last.size() - 1; ++i) {
                curr.add(last.get(i) + last.get(i + 1));
            }
            curr.add(1);
        }

        memo.add(curr);  // Add Current Row
        return memo;
    }

    // Algorithm(s) Used: Dynammic Programming (1-D), Bottom-Down, Tabulation
    // Time Complexity: O(n^2)
    // Space Complexity: O(n^2)
    public List<List<Integer>> generateIII(int numRows) {
        List<List<Integer>> dp = new ArrayList<>();
        dp.add(new ArrayList<>(Arrays.asList(1)));

        for (int i = 0; i < numRows - 1; ++i) {
            List<Integer> prev = dp.get(i);

            List<Integer> curr = new ArrayList<>();
            curr.add(1);
            for (int j = 0; j < i; j += 1) {
                curr.add(prev.get(j) + prev.get(j + 1));
            }
            curr.add(1);

            dp.add(curr);
        }

        return dp;
    }
}
