-- script to lists all cities contained in the database
-- Result is stored in ascending order by cities.name
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id;
