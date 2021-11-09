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