-- select first_name, last_name from students where LOWER(first_name) LIKE '%a';
select first_name, last_name from students where first_name ILIKE '%a';


