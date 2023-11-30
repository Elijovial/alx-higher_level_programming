#!/usr/bin/python3
""" A script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    # Create a cursor object
    cursor = db.cursor()
    # Execute SQL query
    cursor.execute("SELECT * FROM states")
    # Fetch all records
    rows = cursor.fetchall()
    # Print each record
    for row in rows:
        print(row)
    # Close cursor and database
    cursor.close()
    db.close()
