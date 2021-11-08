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



-- Exercise 2 : Dvdrental Database
-- In the dvdrental database write a query to select all the
--  columns from the “customer” table.
select * from customer;

-- Write a query to display the names (first_name, last_name) using an alias named “full_name”.
select first_name || ' ' || last_name AS full_name from customer;
--3
-- Lets get all the dates that accounts were created. Write a query
--  to select all the create_date from the “customer” table (there should be no duplicates).
select DISTINCT create_date from customer;

-- Write a query to get all the customer details from the customer
-- table, it should be displayed in descending order by their first name.
select * from customer order by first_name desc;

-- Write a query to get the film ID, title, description, year of
-- release and rental rate in ascending order according to their rental rate.
select film_id, title, description, release_year, rental_rate from film order by rental_rate DESC;

-- Write a query to get the address, and the phone number of all
-- customers living in the Texas district, these details can be found in the “address” table.
 select address,phone from address where address.address_id in (select address_id from customer) and address.district = 'Texas';

-- Write a query to retrieve all movie details where the movie id is either 15 or 150.
 select * from film where film_id = 5 or film_id = 150;

-- Write a query which should check if your favorite movie exists in the database.
-- Have your query get the film ID, title, description, length and the rental rate,
--  these details can be found in the “film” table.
select film_id, title,rental_rate,description,length from film  where film.title='Groundhog Uncut';
select film_id, title,rental_rate,description,length from film  where film.title='Jurassic Park';


-- No luck finding your movie? Maybe you made a mistake spelling the
-- name. Write a query to get the film ID, title, description, length and the
--  rental rate of all the movies starting with the two first letters of your favorite movie.

-- Write a query which will find the 10 cheapest movies.

-- Not satisfied with the results. Write a query which will find the
-- next 10 cheapest movies.
-- Bonus: Try to not use LIMIT.

-- Write a query which will join the data in the customer table and the
-- payment table. You want to get the amount and the date of every payment made by
-- a customer, ordered by their id (from 1 to…).

-- You need to check your inventory. Write a query to get all the movies
--  which are not in inventory.

-- Write a query to find which city is in which country.

-- Bonus You want to be able to see how your sellers have been doing?
--  Write a query to get the customer’s id, names (first and last), the amount and
--  the date of payment ordered by the id of the staff member who sold them the dvd.