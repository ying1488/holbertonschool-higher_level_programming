#!/usr/bin/python3
"""SQL Inhection"""
import MySQLdb
import sys

# connecting to MySQL database
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    cursor = db_connection.cursor()
    q = """
        SELECT cities.name FROM cities JOIN states 
        ON cities.state_id = states.id WHERE states.name = %s
        ORDER BY cities.id ASC
        """
    cursor.execute(q, (state_name,))

    n_cities = cursor.fetchall()
    print(", ".join(n[0] for n in n_cities))

    cursor.close()
    db_connection.close()
