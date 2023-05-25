-- SELECT * FROM city_info

-- 1. Select everything from the table. (every row and columns) - How many records does the table have?
SELECT * FROM city_info
SELECT COUNT(*) FROM city_info

-- 2. What was Bostons temperature on the 01/03/2015 at 11am ?
SELECT temperature FROM city_info 
WHERE city='Boston' 
AND event_datetime = '2015-03-01 11:00:00'

-- 3. When (ie. days and hours) was the temperature between 28 and 30 degrees in San Francisco ?
SELECT ROUND(temperature),
EXTRACT(DAY FROM event_datetime) AS day, 
EXTRACT(HOUR FROM event_datetime) as hour
FROM city_info
WHERE city='San Francisco' AND temperature BETWEEN 28 and 30

-- 4. Which city was the most noisy (show the name of the city, the date and the noise index)? - Don't use the MAX function
SELECT city, event_datetime, sound FROM city_info
ORDER BY sound DESC
LIMIT 1

-- 5. Which city was the least noisy (show the name of the city, the date and the noise index)? - Don't use the MIN function
SELECT city, event_datetime, sound FROM city_info
ORDER BY sound ASC
LIMIT 1

-- 6. Show the dust index of San Francisco on the 26/03/2015 after 20:00:00.
SELECT event_datetime, dust FROM city_info
WHERE city='San Francisco' 
AND DATE(event_datetime) = '2015-03-26'
AND EXTRACT(HOUR FROM event_datetime) > 20

-- 7. When (ie. days and hours) is the humidity index less that 40 or more than 60 in Geneva?
SELECT city, humidity, event_datetime
FROM city_info
WHERE city='Geneva'
AND (humidity < 40 OR humidity > 60)

-- 8. Where and when (Find the day (Sunday-Saturday)) is the light index the highest? - Use an alias for the day of the week.
SELECT city, TO_CHAR(event_datetime, 'day')
FROM city_info
ORDER BY light DESC
LIMIT 1

SELECT city, TO_CHAR(event_datetime, 'day') AS day
FROM city_info
WHERE light = (SELECT MAX(light) FROM city_info)

-- 9. Select only the info of the cities that start with an "S" (uppercase or lowercase). - Look at the DISTINCT constraint.
SELECT DISTINCT city FROM city_info
WHERE city ILIKE 's%'

-- 10. Add to the table, todays information in Israel - of this very hour. (event_datetime,city,temperature,light,airquality_raw,sound,humidity,dust) -- - Use the return statement to see what you just inserted:
INSERT INTO city_info (event_datetime,city,temperature,light,airquality_raw,sound,humidity,dust) 
VALUES (NOW(), 'Israel', '10', 10,10,10,10,10) RETURNING *










