#!/usr/bin/python3
""" this script takes in argument and display all values in the table """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT *\
    FROM states WHERE states.name =%s\
    ORDER BY id ASC", (sys.argv[4],))

    q_rows = cur.fetchall()
    for row in q_rows:
        print(row)
    cur.close()
    db.close()
