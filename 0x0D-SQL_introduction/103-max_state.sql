-- this query display the temperature max of a state order by name state
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state;
