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

package algorithms.dynamic_programming.one_dimensional;

import java.util.ArrayList;
import java.util.List;

public class PascalTriangle {

    // Algorithm(s) Used: Recursion, Top-Down
    // Time Complexity: O(n^2)
    // Space Complexity: O(n^2)
    public List<List<Integer>> generateI(int numRows) {
        // Base Case
        if (numRows == 1) {
            List<List<Integer>> base = new ArrayList<>();
            base.add(List.of(1));
            return base;
        }

        List<List<Integer>> memo = generateI(numRows - 1);  // Previous Rows (Recursive)
        List<Integer> last = memo.get(memo.size() - 1);  // Last Row

        // Curr Row
        List<Integer> curr = new ArrayList<>();
        curr.add(1);
        for (int i = 0; i < last.size(); i += 1) {
            curr.add(last.get(i) + last.get(i + 1));
        }
        curr.add(1);

        memo.add(curr);
        return memo;
    }

    // Algorithm(s) Used: Dynammic Programming (1-D), Bottom-Down
    // Time Complexity: O(n^2)
    // Space Complexity: O(n^2)
    public List<List<Integer>> generateII(int numRows) {
        List<List<Integer>> dp = new ArrayList<>();

        List<Integer> prev = new ArrayList<>();
        prev.add(1);

        for (int i = 0; i < numRows; i += 1) {
            dp.add(prev);
            List<Integer> curr = new ArrayList<>();
            curr.add(1);
            for (int j = 0; j < i; j += 1) {
                curr.add(prev.get(j) + prev.get(j + 1));
            }
            curr.add(1);
            prev = curr;
        }

        return dp;
    }

    // Algorithm(s) Used: Dynammic Programming (1-D), Bottom-Down
    // Time Complexity: O(n^2)
    // Space Complexity: O(n^2)
    public List<List<Integer>> generateIII(int numRows) {
        List<List<Integer>> dp = new ArrayList<>();
        dp.add(List.of(1));

        for (int i = 0; i < numRows - 1; i += 1) {
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
