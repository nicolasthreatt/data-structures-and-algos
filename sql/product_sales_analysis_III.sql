/*
Product Sales Analysis III
https://leetcode.com/problems/product-sales-analysis-iii

Table: Sales
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to Product table.
Each row records a sale of a product in a given year.
A product may have multiple sales entries in the same year.
Note that the per-unit price.

Write a solution to find all sales that occurred in the first year each product was sold.

For each product_id, identify the earliest year it appears in the Sales table.

Return all sales entries for that product in that year.
Return a table with the following columns: product_id, first_year, quantity, and price.

Input:
    Sales table:
    +---------+------------+------+----------+-------+
    | sale_id | product_id | year | quantity | price |
    +---------+------------+------+----------+-------+ 
    | 1       | 100        | 2008 | 10       | 5000  |
    | 2       | 100        | 2009 | 12       | 5000  |
    | 7       | 200        | 2011 | 15       | 9000  |
    +---------+------------+------+----------+-------+
Output:
    +------------+------------+----------+-------+
    | product_id | first_year | quantity | price |
    +------------+------------+----------+-------+ 
    | 100        | 2008       | 10       | 5000  |
    | 200        | 2011       | 15       | 9000  |
    +------------+------------+----------+-------+
*/

-- Algorithm Used: Join
SELECT
    Sales.product_id,
    FirstYears.first_year,
    Sales.quantity,
    Sales.price
FROM Sales
JOIN (
    SELECT product_id, MIN(year) as first_year
    FROM Sales
    GROUP BY product_id
) FirstYears ON Sales.product_id = FirstYears.product_id AND Sales.year = FirstYears.first_year;

-- Algorithm Used: CTE, Join
WITH FirstYears AS (
    SELECT
        product_id,
        MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
)
SELECT
    Sales.product_id,
    FirstYears.first_year,
    Sales.quantity,
    Sales.price
FROM Sales
JOIN FirstYears ON 
    Sales.product_id = FirstYears.product_id AND
    Sales.year = FirstYears.first_year;
