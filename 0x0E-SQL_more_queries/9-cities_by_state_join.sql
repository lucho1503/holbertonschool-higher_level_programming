-- this query lists all cities in the database
SELECT cities.id, cities.name, states.name FROM states INNER JOIN cities ON cities.id = states.id;
