-- 1.1
select * from items ORDER BY product_cents_price ASC;
--1.2
select * from items WHERE product_cents_price >= 8000 ORDER BY product_cents_price DESC;
-- 1.3
select first_name, last_name from customers ORDER BY first_name ASC, last_name ASC  limit 3 ;

