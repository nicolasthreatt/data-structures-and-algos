/*
Swap Salary
https://leetcode.com/problems/swap-salary

Table: Salary
    +-------------+----------+
    | Column Name | Type     |
    +-------------+----------+
    | id          | int      |
    | name        | varchar  |
    | sex         | ENUM     |
    | salary      | int      |
    +-------------+----------+
- id is the primary key
- ex column is ENUM (category) value of type ('m', 'f')

Write a solution to swap all 'f' and 'm' values using single update statement.
Do not write any select statement for this problem

Input: 
    Salary table:
    +----+------+-----+--------+
    | id | name | sex | salary |
    +----+------+-----+--------+
    | 1  | A    | m   | 2500   |
    | 2  | B    | f   | 1500   |
    | 3  | C    | m   | 5500   |
    | 4  | D    | f   | 500    |
    +----+------+-----+--------+

Output: 
    +----+------+-----+--------+
    | id | name | sex | salary |
    +----+------+-----+--------+
    | 1  | A    | f   | 2500   |
    | 2  | B    | m   | 1500   |
    | 3  | C    | f   | 5500   |
    | 4  | D    | m   | 500    |
    +----+------+-----+--------+
*/

UPDATE Salary
SET sex =
    CASE sex
        WHEN 'm' THEN 'f'
        WHEN 'f' THEN 'm'
    END;
