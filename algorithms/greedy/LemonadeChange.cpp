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

#include <cassert>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class LemonadeChange {
public:

    // Algorithm(s) Used: Greedy, Hash Map
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    bool lemonadeChangeI(vector<int>& bills) {
        // Can't Giveaway $20 Bill (Only $5s and $10s)
        unordered_map<int, int> change = {{5, 0}, {10, 0}, {20, 0}};

        for (int bill : bills) {
            change[bill] += 1;                          // Local Solution - Count Change


            if (bill == 10) {                           // Local Choice - Given $10 Bill (Need to Give $5)
                if (change[5] == 0) {                   // Greedy Choice - Can't Provide Change for $10 Bill
                    return false;
                }
                change[5] -= 1;                         // Local Solution - Count Change (Give Away $5)
            }
            else if (bill == 20) {                      // Local Choice - Given $20 Bill (Need to Give $15)
                if (change[10] > 0 && change[5] > 0) {  // Local Solution - Count Change (Give Away $15)
                    change[10] -= 1;
                    change[5] -= 1;
                } else if (change[5] >= 3) {            // Local Solution - Count Change (Give Away $15)
                    change[5] -= 3;
                }
                else {                                  // Greedy Choice - Can't Provide Change for $20 Bill
                    return false;
                }
            }
        }

        return true;                                    // Global Solution - Enough Change
    }
};

int main() {
    LemonadeChange sol;

    // (bills, expected)
    vector<tuple<vector<int>, bool>> test_cases = {
        {{5}, true},
        {{5, 5, 5}, true},
        {{5, 10}, true},
        {{5, 5, 10}, true},
        {{5, 5, 5, 10, 20}, true},
        {{5, 5, 10, 10, 20}, false},
        {{10}, false},
        {{20}, false},
        {{5, 20}, false},
        {{5, 5, 5, 20, 20}, false},
        {{5, 10, 5, 20, 5, 5, 10, 20}, true},
    };

    vector<bool (LemonadeChange::*)(vector<int>&)> funcs = {
        &LemonadeChange::lemonadeChangeI,
    };

    for (auto func : funcs) {
        for (auto& tc : test_cases) {
            vector<int> bills;
            bool expected;
            tie(bills, expected) = tc;

            bool result = (sol.*func)(bills);
            assert(result == expected);
        }
    }

    return 0;
}
