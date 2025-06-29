#!/usr/bin/python3
""" This module is for filter states by user inputusing MySQLdb"""

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

    name_search = sys.argv[4]
    cursor = db_connection.cursor()
    # Executing MySQL Queries in Python
    format = "SELECT * FROM states WHERE name = BINARY %s;" \ 
    "ORDER BY id ASC;"
    cursor.execute(format, (name_search))
    # Obtaining Query Results
    n_states = cursor.fetchall()

    for n in n_states:
        print(n)

    # Clean Up
    cursor.close()
    db_connection.close()
