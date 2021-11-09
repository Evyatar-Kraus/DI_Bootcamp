
-- Instructions
-- You are going to practice tables relationships

-- Create 2 tables : Customer and Customer profile.


CREATE TABLE customer(
    customer_id serial primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null
);

CREATE TABLE customer_profile (
    profile_id serial primary key,
    customer_id integer,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id) on delete cascade,
);


insert  into customer(first_name,last_name) values ('Billy', 'Mackey'),('Johnny','Big'),('Sonny','Lin')
insert  into customer_profile(customer_id) values (1),(2),(3)

insert  into customer(first_name,last_name) values ('Jason','Key')
insert  into customer_profile(customer_id) values (7)

--  They have a One to One relationship. Use all the types of Joins to display the data.
select * from customer inner join customer_profile on customer.customer_id = customer_profile.customer_id;
select * from customer left outer join customer_profile on customer.customer_id = customer_profile.customer_id;
select * from customer right outer join customer_profile on customer.customer_id = customer_profile.customer_id;
select * from customer full outer join customer_profile on customer.customer_id = customer_profile.customer_id;



-- Create 2 other tables : Product and Order. Order is
--  a table with a Many to Many relationship with the Customer and Product tables. Use all the types of Joins to display the data.
