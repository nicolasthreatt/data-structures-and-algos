/*
Consecutive Numbers
https://leetcode.com/problems/consecutive-numbers

Table: Logs
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
- In SQL, id is the primary key for this table.
- id is an autoincrement column starting from 1.
 

Find all numbers that appear at least three times consecutively.
Return the result table in any order.

Example:
    Input: 
    Logs table:
    +----+-----+
    | id | num |
    +----+-----+
    | 1  | 1   |
    | 2  | 1   |
    | 3  | 1   |
    | 4  | 2   |
    | 5  | 1   |
    | 6  | 2   |
    | 7  | 2   |
    +----+-----+

    Output: 
    +-----------------+
    | ConsecutiveNums |
    +-----------------+
    | 1               |
    +-----------------+

Explanation:
    1 is the only number that appears consecutively for at least three times.

*/


-- Algorithm Used: WHERE
SELECT DISTINCT L1.num AS ConsecutiveNums
FROM Logs L1, Logs L2, Logs L3
WHERE L1.id = L2.id + 1 and L2.id = L3.id + 1 and L1.num = L2.num and L2.num = L3.num;


-- Algorithm Used: Sub-Query, LAG
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num,
           LAG(num, 1) OVER (ORDER BY id) AS prev1,
           LAG(num, 2) OVER (ORDER BY id) AS prev2
    FROM Logs
) t
WHERE num = prev1 AND num = prev2;
