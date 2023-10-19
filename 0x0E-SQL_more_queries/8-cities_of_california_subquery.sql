-- script to lists the cities od california that can be found in database
-- states table contains only one record wher name = california
SELECT id, name FROM cities
WHERE state_id IN(
	SELECT id FROM states 
	WHERE name = "California")
ORDER BY id;
