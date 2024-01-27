import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to retrieve states matching the provided state_name
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))

    # Fetch all the rows in a list of tuples
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the database connection
    db.close()
