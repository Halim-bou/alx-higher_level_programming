-- script to create a teble and databse
-- id is unique, int, not null, PK, auto generated and state_id is int , not null, FK, references to id.states and name is not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
       (id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
       state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
       name VARCHAR(256) NOT NULL);
