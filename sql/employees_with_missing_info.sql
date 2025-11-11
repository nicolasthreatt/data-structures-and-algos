/*
Employees With Missing Information
https://leetcode.com/problems/employees-with-missing-information

Table: Employees
    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | employee_id | int     |
    | name        | varchar |
+-------------+---------+
- employee_id is the column with unique values for this table.
- Each row of this table indicates the name of the employee whose ID is employee_id

Table: Salaries
    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | employee_id | int     |
    | salary      | int     |
    +-------------+---------+
- employee_id is the column with unique values for this table.
- Each row of this table indicates the salary of the employee whose ID is employee_id

Write a solution to report the IDs of all the employees with missing information.

The information of an employee is missing if either :
    - The employee's name is missing
    - The employee's salary is missing

Return the result table ordered by employee_id in ascending order.

Input: 
    Employees table:
    +-------------+----------+
    | employee_id | name     |
    +-------------+----------+
    | 2           | Crew     |
    | 4           | Haven    |
    | 5           | Kristian |
    +-------------+----------+

    Salaries table:
    +-------------+--------+
    | employee_id | salary |
    +-------------+--------+
    | 5           | 76071  |
    | 1           | 22517  |
    | 4           | 63539  |
    +-------------+--------+

Output: 
    +-------------+
    | employee_id |
    +-------------+
    | 1           |
    | 2           |
    +-------------+

Explanation: 
    - Employees 1, 2, 4, and 5 are working at this company.
    - The name of employee 1 is missing.
    - The salary of employee 2 is missing.
*/


-- Algorithm Used: Union
SELECT DISTINCT employee_id
FROM Employees
WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)

UNION

SELECT DISTINCT employee_id
FROM Salaries
WHERE employee_id NOT IN (SELECT employee_id FROM Employees)

ORDER BY employee_id;

SELECT
    DISTINCT all_employees.employee_id
FROM (
    SELECT * FROM Employees
    UNION
    SELECT * FROM Saleries
) all_employees
WHERE all_employees.name IS NOT NULL OR all_employees.salary IS NOT NULL


-- Algorithm Used: Full Join
-- DB Engine: MSSQL (T-SQL)
SELECT
    ISNULL(E.employee_id,s.employee_id) employee_id
FROM
    Employees E
FULL JOIN 
    Salaries S ON E.employee_id = S.employee_id
WHERE
    E.name IS NULL
OR
    S.salary IS NULL
ORDER BY
     ISNULL(E.employee_id,s.employee_id)
