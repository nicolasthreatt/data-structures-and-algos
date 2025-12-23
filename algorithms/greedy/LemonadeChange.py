"""
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
"""

from typing import List


class LemonadeChange:

    # Algorithm(s) Used: Greedy, Hash Map
    # Time Complexity: O(n)
    # Space Complexity: O()
    def lemonadeChangeI(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0, 20: 0}  # NOTE: Can't Giveaway $20 Bill (Only $5s and $10s)

        for bill in bills:
            change[bill] = change.get(bill, 0) + 1    # Local Solution - Count Change

            if bill == 10:         # Local Choice - Given $10 Bill (Need to Give $5)
                if change[5] == 0: # Greedy Choice - Can't Provide Change for $10 Bill
                    return False
                change[5] -= 1                        # Local Solution - Count Change (Give Away $5)
            elif bill == 20:       # Local Choice - Given $20 Bill (Need to Give $15)
                if change[10] > 0 and change[5] > 0:  # Local Solution - Count Change (Give Away $15)
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] >= 3:                  # Local Solution - Count Change (Give Away $15)
                    change[5] -= 3
                else:
                    return False   # Greedy Choice - Can't Provide Change for $20 Bill

        # Greedy Solution - Can Provide Sufficent Change
        return True


if __name__ == "__main__":
    Solution = LemonadeChange()

    test_cases = [
        # (bills, expected)
        ([5], True),
        ([5, 5, 5], True),
        ([5, 10], True),
        ([5, 5, 10], True),
        ([5, 5, 5, 10, 20], True),
        ([5, 5, 10, 10, 20], False),
        ([10], False),
        ([20], False),
        ([5, 20], False),
        ([5, 5, 5, 20, 20], False),
        ([5, 10, 5, 20, 5, 5, 10, 20], True),
    ]

    funcs = [
        Solution.lemonadeChangeI,
    ]

    for func in funcs:
        for bills, expected in test_cases:
            result = func(bills)
            assert result == expected
