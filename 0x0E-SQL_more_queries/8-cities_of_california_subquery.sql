-- cities of california
SELECT id, names FROM cities WHERE (SELECT id FROM states WHERE name = 'California');
