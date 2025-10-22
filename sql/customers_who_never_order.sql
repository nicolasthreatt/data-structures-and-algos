/*
Customers Who Never Order
https://leetcode.com/problems/customers-who-never-order

Table: Customers
    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | id          | int     |
    | name        | varchar |
    +-------------+---------+
- id is the primary key (column with unique values) for this table
- Each row of this table indicates the ID and name of a customer

Table: Orders
    +-------------+------+
    | Column Name | Type |
    +-------------+------+
    | id          | int  |
    | customerId  | int  |
    +-------------+------+
- id is the primary key (column with unique values) for this table
- customerId is a foreign key (reference columns) of the ID from the Customers table
- Each row of indicates the ID of an order and the ID of the customer who ordered it

Write a solution to find all customers who never order anything.

Return the result table in any order.

Input: 
Customers table:
    +----+-------+
    | id | name  |
    +----+-------+
    | 1  | Joe   |
    | 2  | Henry |
    | 3  | Sam   |
    | 4  | Max   |
    +----+-------+
Orders table:
    +----+------------+
    | id | customerId |
    +----+------------+
    | 1  | 3          |
    | 2  | 1          |
    +----+------------+

Output: 
    +-----------+
    | Customers |
    +-----------+
    | Henry     |
    | Max       |
    +-----------+
*/

SELECT Customers.name as Customers
FROM Customers
WHERE Customers.id NOT IN (SELECT DISTINCT customerId FROM Orders);
