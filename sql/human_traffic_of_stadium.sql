/*
Human Traffic of Stadium
https://leetcode.com/problems/human-traffic-of-stadium/

Table: Stadium
    +---------------+---------+
    | Column Name   | Type    |
    +---------------+---------+
    | id            | int     |
    | visit_date    | date    |
    | people        | int     |
    +---------------+---------+
- visit_date is the column with unique values for this table.
- Each row contains the visit date and visit id to the stadium with number of people during visit.
- As the id increases, the date increases as well.

Write a solution to display the records with three or more rows with consecutive id's,
and the number of people is greater than or equal to 100 for each.

Return the result table ordered by visit_date in ascending order.

Input: 
    Stadium table:
    +------+------------+-----------+
    | id   | visit_date | people    |
    +------+------------+-----------+
    | 1    | 2017-01-01 | 10        |
    | 2    | 2017-01-02 | 109       |
    | 3    | 2017-01-03 | 150       |
    | 4    | 2017-01-04 | 99        |
    | 5    | 2017-01-05 | 145       |
    | 6    | 2017-01-06 | 1455      |
    | 7    | 2017-01-07 | 199       |
    | 8    | 2017-01-09 | 188       |
    +------+------------+-----------+

Output: 
    +------+------------+-----------+
    | id   | visit_date | people    |
    +------+------------+-----------+
    | 5    | 2017-01-05 | 145       |
    | 6    | 2017-01-06 | 1455      |
    | 7    | 2017-01-07 | 199       |
    | 8    | 2017-01-09 | 188       |
    +------+------------+-----------+

Explanation: 
    - The four rows with ids 5, 6, 7, and 8 have consecutive ids and each has >= 100 people attended
      Note that row 8 was included even though the visit_date was not the next day after row 7
    - The rows with ids 2 and 3 are not included because we need at least three consecutive ids.
*/

WITH FilteredSubSeqs AS (
    SELECT *, id - ROW_NUMBER() OVER (ORDER BY id) AS subseq
    FROM Stadium
    WHERE people >= 100
)
SELECT
    id,
    visit_date,
    people
FROM FilteredSubSeqs
WHERE subseq IN (
    SELECT subseq
    FROM FilteredSubSeqs
    GROUP BY subseq
    HAVING COUNT(*) >= 3
)
ORDER BY visit_date;
