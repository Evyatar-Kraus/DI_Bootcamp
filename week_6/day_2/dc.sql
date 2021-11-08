-- Instructions
-- In this puzzle you have to go through all the SQL queries
-- and provide us the output of the requests before executing them (ie. make an assumption).
-- Then, execute them to make sure you were correct.
-- Queries
-- CREATE TABLE FirstTab (
--      id integer,
--      name VARCHAR(10)
-- )
-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar')
-- SELECT * FROM FirstTab
-- CREATE TABLE SecondTab (
--     id integer
-- )
-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL)
-- SELECT * FROM SecondTab
-- DATA
-- Table1 – FirstTab
-- ID  Name
-- 5   Pawan
-- 6   Sharlee
-- 7   Krish
-- NULL    Avtaar
-- Table2 – SecondTab
-- ID
-- 5
-- NULL
-- Questions
-- Q1. What will be the OUTPUT of the following statement?
SELECT
    COUNT(*)
FROM
    FirstTab AS ft
WHERE
    ft.id NOT IN (
        SELECT
            id
        FROM
            SecondTab
        WHERE
            id IS NULL
    )

    --A1
    -- ASSUMPTION:
    -- SELECT id FROM SecondTab WHERE id IS NULL will return only one row with 5
    --  FROM FirstTab AS ft WHERE ft.id NOT IN (5) will return
    --the rows
    -- 6   Sharlee
    -- 7   Krish
    -- NULL    Avtaar
    --and count on them will return 3 beacuse there are 3 such rows
    --BUT IT REUTRNS 0
    -- so it probably becasue IN doesnt work on (null) beacuse null really has no value
    -- and should be checked with special functions or with IS
    -- like that

    
SELECT
    COUNT(*)
FROM
    FirstTab AS ft
WHERE
    ft.id is not null;

-- Q2. What will be the OUTPUT of the following statement?
SELECT
    COUNT(*)
FROM
    FirstTab AS ft
WHERE
    ft.id NOT IN (
        SELECT
            id
        FROM
            SecondTab
        WHERE
            id = 5
    )

    --A2
    --return 2 beacuse the value with null id in firstTab really cant be checked with IN
    --it will return the id 6 and 7



    -- Q3. What will be the OUTPUT of the following statement?
SELECT
    COUNT(*)
FROM
    FirstTab AS ft
WHERE
    ft.id NOT IN (
        SELECT
            id
        FROM
            SecondTab
    )
     --A3
    -- the null value that will come from the one of 2 row in secondTab will ruin the () list of values
    --in checks against
    -- so this will return 0



    -- Q4. What will be the OUTPUT of the following statement?
SELECT
    COUNT(*)
FROM
    FirstTab AS ft
WHERE
    ft.id NOT IN (
        SELECT
            id
        FROM
            SecondTab
        WHERE
            id IS NOT NULL
    )
    --A4 -
    --this will work since in the list of values there wont be a null - here only 5
    --so it will return 2 in the count
    -- one for (6,'Sharlee'),
    -- and one more for (7,'Krish'),