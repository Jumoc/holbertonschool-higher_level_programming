-- lists all cities in the db
SELECT cities.id, cities.name, states.name FROM cities JOIN states WHERE states.id = cities.state_id;
