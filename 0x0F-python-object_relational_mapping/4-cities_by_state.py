#!/usr/bin/python3
""" this script lists all cities from the database """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
    FROM cities JOIN states\
    ON cities.state_id = states.id\
    ORDER BY cities.id ASC")

    q_rows = cur.fetchall()
    for row in q_rows:
        print(row)
    cur.close()
    db.close()
