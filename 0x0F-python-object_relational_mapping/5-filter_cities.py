#!/usr/bin/python3
"""Module states"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3], charset="utf8"
        )
    cur = conn.cursor()
    cur.execute(
        """SELECT cities.name
         FROM cities JOIN states WHERE cities.state_id=(SELECT id FROM states WHERE name=%(name)s)
         GROUP BY cities.id
         ORDER BY cities.id ASC""",
         {"name": sys.argv[4]}
        )
    query_rows = cur.fetchall()
    for i in range(len(query_rows)):
        print(query_rows[i][0], end="")
        if i < len(query_rows) - 1:
            print(end=", ")
    print()

    cur.close()
    conn.close()
