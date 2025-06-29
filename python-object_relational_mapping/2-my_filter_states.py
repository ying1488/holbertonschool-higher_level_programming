#!/usr/bin/python3
"""This module is for filter states by user inputusing MySQLdb"""
import MySQLdb
import sys

# connecting to MySQL database
if __name__ == "__main__":
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    name_search = sys.argv[4]
    cursor = db_connection.cursor()
    # Executing MySQL Queries in Python
    q = (
        "SELECT * FROM states WHERE BINARY" 
        "name = '{}' ORDER BY id ASC"
    )
    cursor.execute(q)
    # Obtaining Query Results
    n_states = cursor.fetchall()

    for n in n_states:
        print(n)
