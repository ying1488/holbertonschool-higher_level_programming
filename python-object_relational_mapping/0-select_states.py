#!/usr/bin/python3
""" This module is for listing all states using MySQLdb"""

#connecting to MySQL database
if __name__ == "__main__":
    import MySQLdb
    import sys
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db_connection.cursor()
# Executing MySQL Queries in Python
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
# Obtaining Query Results
    states = cursor.fetchall()

    for state in states:
        print(state)

# Clean Up
    cursor.close()
    db_connection.close()
