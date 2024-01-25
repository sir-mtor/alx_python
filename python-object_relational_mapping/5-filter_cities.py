
"""Script that takes in the name of a state as an argument and lists all
   cities of that state, using the database hbtn_0e_4_usa."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username, password, database, state_name = sys.argv[1:5]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute(
        "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id",
        (state_name,)
    )

    # Fetch all the rows in a list of lists
    cities = cursor.fetchall()

    # Print the results
    if cities:
        city_names = [city[0] for city in cities]
        print(", ".join(city_names))
    else:
        print()

    # Close the cursor and disconnect from server
    cursor.close()
    db.close()
