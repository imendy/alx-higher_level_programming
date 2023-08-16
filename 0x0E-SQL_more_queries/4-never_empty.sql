-- Creates a table with a constraint on a column and another
-- column that will  never be empty when given a NULL value
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256) NOT NULL
);
