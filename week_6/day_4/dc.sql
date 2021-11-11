-- Instructions
-- Create a table called orders and a table called items.
--  You decide which fields should be in each table,
-- although make sure the items table has a column called price.


create table items(
    item_id serial primary key,
    item_name varchar (50),
    price numeric
);


create table orders(
    id serial primary key,
    order_id integer,
    item_id integer,
    foreign key(item_id) references items(item_id)
)

insert into items(item_name,price) values
('Chair',15),
('Fan',20),
('Freezer',300),

insert into orders(order_id, item_id) values (1,1), (1,2), (1,3), (2,3), (3,1)

select order_id, items.item_id, item_name ,price from orders
inner join items on items.item_id = orders.item_id


-- There should be a one to many relationship
--  between the orders table and the items table.
--  An order can have many items, but an item can belong to only one order.

-- Create a function that returns the total price for a given order.
CREATE or REPLACE FUNCTION total_order_price(wanted_order_id integer)
RETURNS numeric AS $total_price_for_order$
BEGIN
    if exists(select order_id from orders where order_id = wanted_order_id) Then
        RETURN(SELECT SUM(price) from orders
            inner join items on items.item_id = orders.item_id
            where orders.order_id = wanted_order_id);
    else RETURN  NULL;
	END if;
END;
$total_price_for_order$ LANGUAGE plpgsql;



SELECT * FROM total_order_price(1);
SELECT * FROM total_order_price(2);
SELECT * FROM total_order_price(3);
SELECT * FROM total_order_price(4);
SELECT * FROM total_order_price(100);
