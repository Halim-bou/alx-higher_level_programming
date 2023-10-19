-- script to creat a table id_not_null
-- id can't be null and with default 1
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256));
