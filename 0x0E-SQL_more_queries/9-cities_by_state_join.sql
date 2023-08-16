-- Prints and joins records from the two tables with a matching field
SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states
        ON cities.state_id = states.id
    ORDER BY cities.id ASC;
