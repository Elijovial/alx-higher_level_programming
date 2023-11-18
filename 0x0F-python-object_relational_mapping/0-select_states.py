#!/usr/bin/python3
""" A script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    #Connect to MySQL server
    db = MySQLdb.connect(host="localhost",user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3], port=3306)
    #Create a cursor object
    cursor = db.cursor()
    #execute SQL query
    cursor.execute("SELECT * FROM states")
    #fetch all records
    rows = cursor.fetchall()
    #print each record
    for row in rows:
        print(row)
    #close cursor and database
    cursor.close()
    db.close()
