/*
Lemonade Change
https://leetcode.com/problems/lemonade-change/

At a lemonade stand, each lemonade costs $5.

Customers are standing in a queue to buy from you and order one at a time
(in the order specified by bills).

Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.

You must provide the correct change to each customer
so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays,
return true if you can provide every customer with the correct change, or false otherwise.

Example 1:
    Input: bills = [5,5,5,10,20]
    Output: true
    Explanation:
        - From the first 3 customers, we collect three $5 bills in order.
        - From the fourth customer, we collect a $10 bill and give back a $5.
        - From the fifth customer, we give a $10 bill and a $5 bill.
        - Since all customers got correct change, we output true.

Example 2:
    Input: bills = [5,5,10,10,20]
    Output: false
    Explanation:
        - From the first two customers in order, we collect two $5 bills.
        - For the next two customers in order, we collect a $10 bill and give back a $5 bill.
        - For the last customer, we can not give the change of $15 back because we only have two $10 bills.
        - Since not every customer received the correct change, the answer is false.

Constraints:
    * 1 <= bills.length <= 10^5
    * bills[i] is either 5, 10, or 20
*/
package algorithms.greedy;

import java.util.HashMap;
import java.util.Map;

public class LemonadeChange {

    // Algorithm(s) Used: Greedy, Hash Map
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public boolean lemonadeChangeI(int[] bills) {
        Map<Integer, Integer> change = new HashMap<>();
        change.put(5, 0);
        change.put(10, 0);
        change.put(20, 0);  // Can't Giveaway $20 Bill (Only $5s and $10s)

        for (int bill : bills) {
            // Local Solution - Count Change
            change.put(bill, change.get(bill) + 1);

            // Local Choice - Given $10 Bill (Need to Give $5)
            if (bill == 10) {

                // Greedy Choice - Can't Provide Change for $10 Bill
                if (change.get(5) == 0) {
                    return false;
                }

                // Local Solution - Count Change (Give Away $5)
                change.put(5, change.get(5) - 1);
            }

            // Local Choice - Given $20 Bill (Need to Give $15)
            else if (bill == 20) {

                // Local Solution - Count Change (Give Away $15)
                if (change.get(10) > 0 && change.get(5) > 0) {  
                    change.put(10, change.get(10) - 1);
                    change.put(5, change.get(5) - 1);
                }

                // Local Solution - Count Change (Give Away $15)
                else if (change.get(5) >= 3) {                    
                    change.put(5, change.get(5) - 3);
                }

                // Greedy Choice - Can't Provide Change for $20 Bill
                else {
                    return false;
                }
            }
        }

        return true;
    }
}
