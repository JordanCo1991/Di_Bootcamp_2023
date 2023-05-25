-- CREATE TABLE items (
--     items_id SERIAL PRIMARY KEY,
--     model VARCHAR(100) NOT NULL,
--   	price SMALLINT NOT NULL DEFAULT  0
-- )

-- CREATE TABLE customers (
--     customers_id SERIAL PRIMARY KEY,
--     first_name VARCHAR(100) NOT NULL,
--     last_name VARCHAR(100) NOT NULL
-- )



-- INSERT INTO customers (first_name, last_name)
-- VALUES 
-- ('Greg', 'Jones'),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'), 
-- ('Trevor', 'Freen') ,
-- ('Melanie', 'Johnson')

-- INSERT INTO items (model, price)
-- VALUES ('small_desk' , 100 ),
-- ('large_desk', 300),
-- ('fan', 80)

-- SELECT * FROM items
-- SELECT price
-- 	FROM items
-- 	WHERE price > 80


-- SELECT price
-- 	FROM items
-- 	WHERE price <= 300

-- SELECT first_name, last_name FROM customers WHERE last_name = 'Smith'
-- SELECT first_name, last_name FROM customers WHERE last_name = 'Jones'

-- SELECT first_name, last_name FROM customers WHERE NOT first_name = 'Scott'

-- SELECT * FROM items ORDER BY price ASC;
-- SELECT * FROM items WHERE price >= 80 ORDER BY price DESC;
-- SELECT first_name, last_name FROM customers ORDER BY first_name ASC LIMIT 3;
SELECT last_name FROM customers ORDER BY last_name DESC;



