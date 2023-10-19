-- script that create database and table on it
-- is is int and unique and can't be null and autogenarated and he is aprimary key, name can't be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states`(
	PRIMARY KEY(`id`),
	id INT NOT NULL AUTO_INCREMENT UNIQUE,
	name VARCHAR(256) NOT NULL);
