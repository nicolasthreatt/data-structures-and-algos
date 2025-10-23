/*
Sales Person
https://leetcode.com/problems/sales-person

Table: SalesPerson
    +-----------------+---------+
    | Column Name     | Type    |
    +-----------------+---------+
    | sales_id        | int     |
    | name            | varchar |
    | salary          | int     |
    | commission_rate | int     |
    | hire_date       | date    |
    +-----------------+---------+
- sales_id is the primary key

Table: Company
    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | com_id      | int     |
    | name        | varchar |
    | city        | varchar |
    +-------------+---------+
- com_id is the primary key

Table: Orders
    +-------------+------+
    | Column Name | Type |
    +-------------+------+
    | order_id    | int  |
    | order_date  | date |
    | com_id      | int  |
    | sales_id    | int  |
    | amount      | int  |
    +-------------+------+
- order_id is the primary key
- com_id is a foreign key
- sales_id is a foreign key to sales_id from the SalesPerson table

Write a solution to find the names of all the salespersons
who did not have any orders related to the company with the name "RED".

Return the result table in any order.

Input: 
    SalesPerson table:
    +----------+------+--------+-----------------+------------+
    | sales_id | name | salary | commission_rate | hire_date  |
    +----------+------+--------+-----------------+------------+
    | 1        | John | 100000 | 6               | 4/1/2006   |
    | 2        | Amy  | 12000  | 5               | 5/1/2010   |
    | 3        | Mark | 65000  | 12              | 12/25/2008 |
    | 4        | Pam  | 25000  | 25              | 1/1/2005   |
    | 5        | Alex | 5000   | 10              | 2/3/2007   |
    +----------+------+--------+-----------------+------------+

    Company table:
    +--------+--------+----------+
    | com_id | name   | city     |
    +--------+--------+----------+
    | 1      | RED    | Boston   |
    | 2      | ORANGE | New York |
    | 3      | YELLOW | Boston   |
    | 4      | GREEN  | Austin   |
    +--------+--------+----------+

    Orders table:
    +----------+------------+--------+----------+--------+
    | order_id | order_date | com_id | sales_id | amount |
    +----------+------------+--------+----------+--------+
    | 1        | 1/1/2014   | 3      | 4        | 10000  |
    | 2        | 2/1/2014   | 4      | 5        | 5000   |
    | 3        | 3/1/2014   | 1      | 1        | 50000  |
    | 4        | 4/1/2014   | 1      | 4        | 25000  |
    +----------+------------+--------+----------+--------+

Output: 
    +------+
    | name |
    +------+
    | Amy  |
    | Mark |
    | Alex |
    +------+

Explanation: 
    According to orders 3 and 4 in the Orders table,
    it is easy to tell that only salesperson John and Pam have sales to company RED,
    so we report all the other names in the table salesperson.
*/

SELECT
    SalesPerson.name
FROM SalesPerson
LEFT JOIN Orders
    ON SalesPerson.sales_id = Orders.sales_id
LEFT JOIN Company
    ON Orders.com_id = Company.com_id
GROUP BY SalesPerson.name
-- HAVING COALESCE(SUM(Company.name = 'RED'), 0) < 1;                            -- DB Engine: MySQL
HAVING COALESCE(SUM(CASE WHEN Company.name = 'RED' THEN 1 ELSE 0 END), 0) < 1;   -- DB Engine: MSSQL
