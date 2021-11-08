-- Exercise 1 : Items And Customers
-- Instructions
-- We will work on the public database that we created yesterday.

-- All items, ordered by price (lowest to highest).
-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
-- The first 3 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
-- All last names (no other columns!), in reverse alphabetical order (Z-A)


-- 1.1
select * from items ORDER BY product_cents_price ASC;
--1.2
select * from items WHERE product_cents_price >= 8000 ORDER BY product_cents_price DESC;
-- 1.3
select first_name, last_name from customers ORDER BY first_name ASC, last_name ASC  limit 3 ;
-- 1.4
select last_name from customers ORDER BY last_name DESC;
--1.4 another version (if someone entered only a first_name)
select last_name from customers WHERE last_name is not NULL ORDER BY last_name DESC;


-- Create a table named purchases. It should have 2 columns : customer_id and item_id.
-- These columns are references from the tables customers and items.
--  Edit the data of the purchases table:
-- Add a row which references a customer by ID, but does not
--  reference an item by ID (leave it blank). Does this work? Why/why not?
-- Add 5 rows which reference existing customers and items.
-- 2

CREATE TABLE purchases(
id  SERIAL PRIMARY KEY,
customer_id INTEGER NOT NULL,
item_id INTEGER NOT NULL,
FOREIGN KEY (customer_id) REFERENCES customers(id),
FOREIGN KEY (item_id) REFERENCES items(id)
);

--2.1
-- the row will be added if item_id doesnt have constraint not null - but here it does have it
-- so there will be an error
-- ERROR:  null value in column "item_id" of relation "purchases" violates not-null constraint
-- DETAIL:  Failing row contains (1, null).
-- SQL state: 23502
INSERT INTO purchases (customer_id) VALUES (1);


--2.2
INSERT INTO purchases (customer_id,item_id) VALUES (1,3),(4,1),(3,2),(2,3),(2,1);



--3.1
-- not very useful to use - but could be useful to linking the customers and the items and for joins
select * from purchases;
--3.2
select customers.first_name, customers.last_name, purchases.item_id from purchases
 INNER JOIN customers
 on customers.id = purchases.customer_id;
 --3.3
 select * from purchases
 INNER JOIN customers
 on customers.id = purchases.customer_id WHERE purchases.customer_id = 4;
 --3.4
 select * from purchases
 INNER JOIN items
 on items.id = purchases.item_id WHERE LOWER(items.product_name) =  'large desk'
 OR LOWER(items.product_name) = 'small desk';

 --4 - also returned the purchase details
insert into items (product_name, product_cents_price) VALUES ('Hard disk', 20000);

INSERT into purchases (customer_id,item_id)
VALUES ((SELECT id from customers WHERE first_name = 'Scott' and last_name = 'Scott'),
        (SELECT id from items WHERE LOWER(product_name) = 'hard disk'))
returning customer_id, item_id;

--5.1
select first_name from customers inner join purchases on customers.id = purchases.customer_id;
-- another way
select first_name from customers where id in (select customer_id from purchases)
--5.2
select last_name from customers inner join purchases on customers.id = purchases.customer_id;
--another way
select last_name from customers where id in (select customer_id from purchases)

--5.3
-- if it means to show a way to show the names of clients and what they bought
--also one way to do it if i understood correctly
SELECT customers.first_name,customers.last_name, items.product_name
FROM purchases
    INNER JOIN customers
        ON purchases.customer_id = customers.id
    INNER JOIN items
        ON purchases.item_id = items.id;