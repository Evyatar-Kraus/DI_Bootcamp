-- Exercise 1: DVD Rental
-- Instructions
-- Get a list of all film languages.

select name from language;

-- Get a list of all films joined with their languages –
-- select the following details : film title, description, and language name.
select title, description, name from film inner join language on
 film.language_id = language.language_id;



-- Try your query with different joins:
-- Get all films, even if they don’t have languages.

select * from film left outer join
language on film.language_id = language.language_id;

-- Get all languages, even if there are no films in those languages.

select * from film right outer join
language on film.language_id = language.language_id;

-- Create a new table called new_film with the following columns : id,
--  name. Add some new films to the table.

create table new_film as (select film_id as id, title as name) with no data;

-- Create a new table called customer_review,
-- which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted,
-- it’s review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.

CREATE TABLE customer_review(
    review_id  SERIAL PRIMARY KEY ,
    title VARCHAR(50) NOT NULL,
    score INTEGER NOT NULL,
    review_text text NOT NULL,
    film_id INTEGER NOT NULL,
    language_id INTEGER NOT NULL,
    last_update DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (film_id) REFERENCES new_film(id)  ON DELETE CASCADE,
    FOREIGN KEY (language_id) REFERENCES language(language_id),
    CHECK (score BETWEEN 1 AND 10)
);
-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO customer_review(title, score, review_text,film_id,language_id) values
('A love letter to cinema lovers', 9, 'This classic cult-to-be-film doesn''t cut any corners and pull any punches', 1, 2),
('A presentation or a movie?', 6, 'I will not be too harsh on this movie, because it definitely is not one', 3, 2);

-- Delete a film that has a review from the new_film table,
DELETE FROM new_film where new_film.id in (select film_id from customer_review LIMIT 1) returning *;

-- what happens to the customer_review table?
-- ANSWER the review related to this movie also got deleted because of the on delete cascade since the child table
-- that references the key on parent table
-- will delete the  rows that were related by a foreign key to the rows with the primary keys that were deleted.



-- Instructions
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film set language_id = (select language.language_id from language order by random() limit 1)
where film_id in (select film_id from film order by film.film_id limit 3) returning film_id,title,language_id;

-- Which foreign keys (references) are defined for the customer table? How does this affect the way
-- in which we INSERT into the customer table?
-- we need to insert an address_id to match one of the addresses in address table with that id
-- the key customer_address_id_fkey


-- We created a new table called customer_review. Drop this table. Is this an easy step,
-- or does it need extra checking?
DROP TABLE IF EXISTS customer_review;
-- we can check if table exists
-- we need to check if there are foreign keys that reference this table's primary key
-- no table refrences this one's primary key so it was easy


-- Find out how many rentals are still outstanding (ie. have not been returned to the
-- store yet).
select count(*) from inventory where inventory.inventory_id in (select rental.inventory_id from rental)

-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
select film.film_id, film.title as "movie title", film.rental_rate as price, inventory.inventory_id from film
inner join inventory on film.film_id = inventory.film_id where inventory.inventory_id in (select rental.inventory_id from rental)
order by rental_rate DESC limit 30

-- Your friend is at the store, and decides to rent a movie. He knows he wants to see
-- 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors
--  is Penelope Monroe.
select first_name, last_name, actor.actor_id, title, film.description from film_actor inner join
actor on film_actor.actor_id = actor.actor_id
inner join film on film.film_id = film_actor.film_id
where first_name = 'Penelope' and last_name = 'Monroe'
and description ilike  '%sumo wrestler%';

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.

select title,rating,category.name, length from film_category
inner join film on film_category.film_id = film.film_id
inner join category on category.category_id = film_category.category_id
where category.name = 'Documentary' and rating = 'R' and length < 60;

-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over
--  $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.


select first_name, last_name, film.title, film.film_id, rental.return_date, rental.rental_id, inventory.inventory_id
from film inner join inventory on film.film_id = inventory.film_id
inner join rental on rental.inventory_id = inventory.inventory_id
inner join customer on customer.customer_id = rental.customer_id
where customer.first_name = 'Matthew' and last_name = 'Mahan'
and  rental_rate > 4.00
and (return_date between to_timestamp('2005-28-07','YYYY-DD-MM')
and to_timestamp('2005-01-08','YYYY-DD-MM'));

-- The 4th film : His friend Matthew Mahan watched this film, as well.
--  It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.

select first_name, last_name, film.title, description, film.film_id, replacement_cost,
rental.return_date, rental.rental_id,
inventory.inventory_id
from film inner join inventory on film.film_id = inventory.film_id
inner join rental on rental.inventory_id = inventory.inventory_id
inner join customer on customer.customer_id = rental.customer_id
where customer.first_name = 'Matthew' and last_name = 'Mahan'
and (description ilike   '%boat%' or title ilike '%boat%') order by replacement_cost desc limit 1;
