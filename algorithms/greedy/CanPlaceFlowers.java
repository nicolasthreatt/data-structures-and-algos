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

package algorithms.greedy;

public class CanPlaceFlowers {

    // Algorithm(s) Used: Greedy, Padding
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public boolean canPlaceFlowersI(int[] flowerbed, int n) {
        // Pad Flowerbed At Start and End With 0
        int[] flowers = new int[flowerbed.length + 2];  // {0, flowerbed, 0}
        for (int i = 0; i < flowerbed.length; i++) {
            flowers[i + 1] = flowerbed[i];
        }

        // Skip First and Last Elements (Modified 0's)
        for (int i = 1; i < flowers.length - 1; i++) {
            boolean left_pot_empty = flowers[i - 1] == 0;
            boolean curr_pot_empty = flowers[i] == 0;
            boolean right_pot_empty = flowers[i + 1] == 0;
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
    public boolean canPlaceFlowersII(int[] flowerbed, int n) {
        for (int i = 0; i < flowerbed.length; i++) {
            boolean left_pot_empty = (i == 0) || (flowerbed[i - 1] == 0);
            boolean curr_pot_empty = flowerbed[i] == 0;
            boolean right_pot_empty = (i == flowerbed.length - 1) || (flowerbed[i + 1] == 0);
            if (left_pot_empty && curr_pot_empty && right_pot_empty) {  // Greedy Choice - Plant Flower
                n -= 1;  // Local Optimal Choice
                flowerbed[i] = 1;
            }
        }

        return n <= 0;  // Global Optimal Solution
    }
    
}
