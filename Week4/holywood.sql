-- CREATE TABLE actor (
--     actor_id SERIAL PRIMARY KEY,
--     first_name VARCHAR(100) NOT NULL,
--     last_name VARCHAR(100) NOT NULL,
--     date_birth DATE NOT NULL,
--     number_oscars SMALLINT NOT NULL DEFAULT 0
-- )

-- SELECT * FROM actor

-- INSERT INTO actor (first_name, last_name, date_birth, number_oscars)
-- VALUES ('Georges', 'Cloney', '1976-03-12', 2)

-- SELECT * FROM actor

-- INSERT INTO actor (first_name, last_name, date_birth, number_oscars)
-- VALUES 
-- ('Brad', 'Pitt', '1980-04-22', 1),
-- ('Matt', 'Damon', '1982-11-22', 2)


-- INSERT INTO actor (first_name, last_name, date_birth, number_oscars)
-- VALUES 
-- ('Leonardo', 'Di Caprio', '1990-10-8', 1),
-- ('Tom', 'Hanks', '1960-8-24', 5)

-- INSERT INTO actor (first_name, last_name, date_birth, number_oscars)
-- VALUES 
-- ('Nathalie', 'Portman', '1987-02-14', 2)

-- INSERT INTO actor (first_name, last_name, date_birth, number_oscars)
-- VALUES 
-- ('Margot', 'Robbie', '1990-04-21', 0)

-- SELECT * FROM actor
-- INSERT INTO actor (first_name, last_name, date_birth, number_oscars)
-- VALUES 
-- ('Brad', 'Pitt', '1980-04-22', 1),
-- ('Matt', 'Damon', '1982-11-22', 2)
-- SELECT * FROM actor

-- INSERT INTO actor (first_name, last_name, date_birth, number_oscars)
-- VALUES 
-- ('Brad', 'Pitt', '1980-04-22', 1),
-- ('Matt', 'Damon', '1982-11-22', 2)

-- SELECT * FROM  actor



-- exercise 1
-- Use the table actors to retrieve :

-- The first 4 actors
-- The first 4 actors ordered in descending order of the last_name (ie. sorted DESCENDING by the "last_name" column))
-- The actors that have the letter 'e' in their first_name
-- The actors that got at least 5 oscars


-- SELECT * FROM actor ORDER BY first_name LIMIT 4

-- SELECT * FROM actor WHERE first_name LIKE '%e%'
-- SELECT first_name, last_name FROM actor WHERE number_oscars >= 5

-- exercise 2
-- In the table actors, write the following commands:

-- Update the first name of Matt Damon to "Maty"
-- Update the number of oscars of George Clooney to 4, and return the updated record
-- Rename the 'age' column by 'birthdate'
-- Delete one actor and return it


-- SELECT * FROM actor

-- UPDATE actor
-- SET first_name = 'Maty'
-- WHERE actor_id = 7
-- RETURNING *

-- UPDATE actor
-- SET number_oscars = 4
-- WHERE actor_id = 1
-- RETURNING *

-- ALTER TABLE actor RENAME COLUMN date_birth TO age;

-- SELECT COUNT(actor_id)
-- FROM actor;

-- INSERT INTO actor (first_name, last_name, age, number_oscars)
-- VALUES ('', '', , )