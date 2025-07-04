#!/usr/bin/python3
"""SQL Inhection"""
import MySQLdb
import sys

# connecting to MySQL database
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name_search = sys.argv[4]

    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    cursor = db_connection.cursor()
    q = "SELECT * FROM states WHERE BINARY name = %s ORDER BY states.id ASC"
    cursor.execute(q, (name_search,))

    n_states = cursor.fetchall()

    for n in n_states:
        print(n)

    cursor.close()
    db_connection.close()
