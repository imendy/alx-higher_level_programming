-- Selects records from one table (cities) with a
-- column value that can be found in another set
SELECT id, name FROM cities
    WHERE state_id IN
    (
        SELECT id FROM states
            WHERE name = 'California'
    )
    ORDER BY id ASC;
