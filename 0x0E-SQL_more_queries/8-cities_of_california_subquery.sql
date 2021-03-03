-- cities of california
SELECT id, name FROM cities WHERE (SELECT id FROM states WHERE name = 'California');
