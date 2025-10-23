/*
Customer Placing the Largest Number of Orders
https://leetcode.com/problems/customer-placing-the-largest-number-of-orders

Table: Orders
    +-----------------+----------+
    | Column Name     | Type     |
    +-----------------+----------+
    | order_number    | int      |
    | customer_number | int      |
    +-----------------+----------+
- order_number is the primary key
- Table contains information about the order ID and the customer ID

Write a solution to find the customer_number for the customer who has placed the largest number of orders

The test cases are generated so that exactly one customer will have placed more orders than any other customer

Input: 
    Orders table:
    +--------------+-----------------+
    | order_number | customer_number |
    +--------------+-----------------+
    | 1            | 1               |
    | 2            | 2               |
    | 3            | 3               |
    | 4            | 3               |
    +--------------+-----------------+

Output: 
    +-----------------+
    | customer_number |
    +-----------------+
    | 3               |
    +-----------------+

Explanation: 
    - The customer with number 3 has two orders,
      which is greater than either customer 1 or 2 because each of them only has one order
    - So the result is customer_number 3.

Follow up: What if more than one customer has the largest number of orders?
*/


SELECT TOP 1 customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC;  -- DB Engine: MSSQL
-- LIMIT 1;              -- DB Engine: MySQL
