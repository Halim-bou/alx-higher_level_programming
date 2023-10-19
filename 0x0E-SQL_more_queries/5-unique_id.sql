-- script to create a table unique_id
-- id shoul be default 1 and unique
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256));
