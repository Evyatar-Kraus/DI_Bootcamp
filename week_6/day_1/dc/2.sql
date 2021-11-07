INSERT INTO actors(first_name,last_name,number_oscars) VALUES ('Danny','Mashmo', 2)
-- gives errors because the create table script says thay all fields/columns must be no null
-- /not blank so it will give an error becuase of this not null constraints when trying to perform the insert
-- ERROR:  null value in column "age" of relation "actors" violates not-null constraint
-- DETAIL:  Failing row contains (9, Danny, Mashmo, null, 2).
-- SQL state: 23502