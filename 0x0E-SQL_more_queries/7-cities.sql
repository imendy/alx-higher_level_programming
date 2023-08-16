-- Creates a database that doesn't overwrite pre-existing versions
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switches the active database
USE hbtn_0d_usa;
-- Creates a table with a column that is a foreign key
CREATE TABLE IF NOT EXISTS cities(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    UNIQUE(id),
    FOREIGN KEY(state_id)
        REFERENCES states(id)
);
