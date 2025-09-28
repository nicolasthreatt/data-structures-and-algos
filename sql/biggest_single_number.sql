/*
Biggest Single Number
https://leetcode.com/problems/biggest-single-number

Table: MyNumbers
+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
This table may contain duplicates (In other words, there is no primary key for this table in SQL).
Each row of this table contains an integer.

A single number is a number that appeared only once in the MyNumbers table.

Find the largest single number. If there is no single number, report null.

Input: 
    MyNumbers table:
    +-----+
    | num |
    +-----+
    | 8   |
    | 8   |
    | 3   |
    | 3   |
    | 1   |
    | 4   |
    | 5   |
    | 6   |
    +-----+
Output: 
    +-----+
    | num |
    +-----+
    | 6   |
    +-----+
Explanation:
    The single numbers are 1, 4, 5, and 6.
    Since 6 is the largest single number, we return it.

Input: 
    MyNumbers table:
        +-----+
        | num |
        +-----+
        | 8   |
        | 8   |
        | 7   |
        | 7   |
        | 3   |
        | 3   |
        | 3   |
        +-----+
Output: 
    +------+
    | num  |
    +------+
    | null |
    +------+
Explanation:
    There are no single numbers in the input table so we return null.
*/

-- Algorithm Used: Sub-Query
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) SingleNumbers;

-- Algorithm Used: Offset Limit
SELECT TOP 1  -- DB Engine: MSSQL (T-SQL)
    CASE WHEN COUNT(*) = 1 THEN num ELSE 0 END AS num
FROM MyNumbers
GROUP BY num
ORDER BY num DESC;
-- LIMIT 1;  -- DB Engine: MySQL
