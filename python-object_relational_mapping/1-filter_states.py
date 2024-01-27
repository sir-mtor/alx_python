import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # Execute SQL query to retrieve states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'n%' OR name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows in a list of tuples
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the database connection
    db.close()
