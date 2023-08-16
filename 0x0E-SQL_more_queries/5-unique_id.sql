-- Creates a table with a constraint on a column to have a unique value
-- for each row, which will  never be empty when a value isn't given
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1,
    name VARCHAR(256),
    UNIQUE(id)
);
