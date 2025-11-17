/*
Pizzeria Galactica - Shift Work

According to Pizzeria Galactica company policy,
employees must be scheduled in pairs for each shift.

To help the managers create schedules properly,
each manager needs to know the pairs of employees reporting to them.

Write an SQL query to get all possible pairs of employees reporting to the same manager.

Make a selection of employees regardless of their order.
In other words, Bob, Alice and Alice, Bob are really the same pair and should only be included in the result once

The result should have following columns:
  - manager id
  - manager name
  - employee 1 id
  - employee 1 name
  - employee 2 id
  - employee 2 name

Where:
  - employee 1 id < employee 2 id
  - each name is a space-delimited concatenation of the first_name and the last_name fields

Sort the query results by manager id in ascending order.

NOTE:
  - Some employees are no longer working in Pizzeria Galactica and must be excluded from the result.
  - These employees will have an end_date set in the database.

The employee table has the following schema:
  +-------------+---------+
  | COLUMN      | TYPE    |
  +-------------+---------+
  | employee_id | BIGINT  |
  +-------------+---------+
  | store_id    | BIGINT  |
  +-------------+---------+
  | manager_id  | BIGINT  |
  +-------------+---------+
  | title       | VARCHAR |
  +-------------+---------+
  | first_name  | VARCHAR |
  +-------------+---------+
  | last_name   | VARCHAR |
  +-------------+---------+
  | suffix      | VARCHAR |
  +-------------+---------+
  | password    | BYTEA   |
  +-------------+---------+
  | start_date  | DATE    |
  +-------------+---------+
  | end_date    | DATE    |
  +-------------+---------+
*/

SELECT

  -- Manager
  m.employee_id AS "manager id",
  CONCAT(m.first_name, ' ', m.last_name) AS "manager name",
  
  -- Employee 1
  e1.employee_id AS "employee 1 id",
  CONCAT(e1.first_name, ' ', e1.last_name) AS "employee 1 name",
  
  -- Employee 2
  e2.employee_id AS "employee 2 id",
  CONCAT(e2.first_name, ' ', e2.last_name) AS "employee 2 name"

FROM employee m
JOIN employee e1  -- Get FIRST employee reporting to manager
  ON e1.manager_id = m.employee_id AND e1.end_date IS NULL
JOIN employee e2  -- Get SECOND employee reporting to manager
  ON e2.manager_id = m.employee_id AND e2.end_date IS NULL AND e1.employee_id < e2.employee_id
ORDER BY m.employee_id, e1.employee_id, e2.employee_id
