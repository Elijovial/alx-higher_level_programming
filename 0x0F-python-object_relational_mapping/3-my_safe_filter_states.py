#!/usr/bin/python3
"""
write a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
(safe from mysql injection)
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name LIKE
                  BINARY %s ORDER BY states.id""", (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
