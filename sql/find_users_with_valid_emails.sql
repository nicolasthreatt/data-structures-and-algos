/*
Find Users With Valid E-Mails
https://leetcode.com/problems/find-users-with-valid-e-mails

Table: Users
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
| mail          | varchar |
+---------------+---------+
- user_id is the primary key (column with unique values) for this table.
- This table contains information of the users signed up in a website. Some e-mails are invalid.

A valid e-mail must:
  - Start with a letter (uppercase or lowercase)
  - Followed by zero or more allowed characters: letters, digits, underscore '_', period '.', or dash '-'
  - End with '@leetcode.com' (domain must be exactly in lowercase)

Return the result table in any order.

Example:
    Input:
    Users table:
    +---------+-----------+-------------------------+
    | user_id | name      | mail                    |
    +---------+-----------+-------------------------+
    | 1       | Winston   | winston@leetcode.com    |
    | 2       | Jonathan  | jonathanisgreat         |
    | 3       | Annabelle | bella-@leetcode.com     |
    | 4       | Sally     | sally.come@leetcode.com |
    | 5       | Marwan    | quarz#2020@leetcode.com |
    | 6       | David     | david69@gmail.com       |
    | 7       | Shapiro   | .shapo@leetcode.com     |
    +---------+-----------+-------------------------+

Expected Output:
    +---------+-----------+-------------------------+
    | user_id | name      | mail                    |
    +---------+-----------+-------------------------+
    | 1       | Winston   | winston@leetcode.com    |
    | 3       | Annabelle | bella-@leetcode.com     |
    | 4       | Sally     | sally.come@leetcode.com |

Explanation:
    - User 2 is invalid: no domain present.
    - User 5 is invalid: '#' is not an allowed character.
    - User 6 is invalid: domain is not '@leetcode.com'.
    - User 7 is invalid: prefix starts with a period, which is not allowed.
*/

SELECT *
FROM Users
WHERE REGEXP_LIKE(
    mail,
    /* 
        ^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$
        │   │        │             │
        │   │        │             └─ Must end with exactly "@leetcode.com"
        │   │        └─ Zero or more allowed characters: letters, digits, ., _, -
        │   └─ First character must be a letter (uppercase or lowercase)
        └─ Start of string
    */
    '^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$',
    'c'  -- 'c' ensures case-sensitive match
);
