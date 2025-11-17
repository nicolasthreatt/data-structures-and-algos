/*
Pizzeria Galactica - Customer Names, Countries and Phones

Write an SQL query to get the list of customers' full names with their countries and phone numbers

The schema of the database is shown in the attachments tab.

The customer full name is a space-delimited concatenation of the
  - title (if it exists)
  - first_name
  - last_name

If the suffix field is present, it should be appended enclosed in parenthesis.

In other words, output the full name in the following format:
<title> <first_name> <last_name> (suffix)

Output phone numbers in the following format:
<phone_country_code>-<phone_area_code>-<phone_number>

Be sure to include all customers, even if they are missing some information

Sort the results alphabetically by country and then by phone number in ascending order within each country
*/

-- DB Engine: MSSQL
SELECT
    TRIM(
        COALESCE(title + ' ', '') +
        COALESCE(first_name, '') + ' ' +
        COALESCE(last_name, '') +
        COALESCE(' (' + suffix + ')', '')
    ) AS "full name",
  physical_address.country,
  CASE
      WHEN phone_country_code IS NULL AND phone_area_code IS NULL AND phone_number IS NULL
        THEN NULL
      ELSE
          COALESCE(CAST(phone_country_code AS VARCHAR), '') + '-' +
          COALESCE(CAST(phone_area_code AS VARCHAR), '') + '-' +
          COALESCE(CAST(phone_number AS VARCHAR), '')
  END AS "phone number"
FROM customer
LEFT JOIN phone_number 
  ON phone_number.customer_id = customer.customer_id
LEFT JOIN customer_address 
  ON customer_address.customer_id = customer.customer_id
LEFT JOIN physical_address
  ON physical_address.physical_address_id = customer_address.physical_address_id
ORDER BY
  physical_address.country,
  phone_number.phone_country_code,
  phone_number.phone_area_code,
  phone_number.phone_number;


-- DB Engine: PostgreSQL
SELECT
  TRIM(
    COALESCE(title || ' ', '') ||
    first_name || ' ' ||
    last_name || ' ' ||
    COALESCE('(' || suffix || ')', '')
  ) AS "full name",
  physical_address.country,
  CASE
    WHEN
      phone_country_code IS NULL AND
      phone_area_code IS NULL AND
      phone_number IS NULL
     THEN
       NULL
     ELSE COALESCE(CAST(phone_country_code AS TEXT), '') || '-' ||
          COALESCE(CAST(phone_area_code AS TEXT), '') || '-' ||
          COALESCE(CAST(phone_number AS TEXT), '')
  END AS "phone number"
FROM customer
LEFT JOIN phone_number USING(customer_id)
LEFT JOIN customer_address USING(customer_id)
LEFT JOIN physical_address
  ON physical_address.physical_address_id = customer_address.physical_address_id
ORDER BY
  physical_address.country,
  phone_country_code,
  phone_area_code,
  phone_number;
