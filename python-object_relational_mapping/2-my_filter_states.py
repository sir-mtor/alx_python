import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        sys.exit(1)

    # Get command line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to fetch states where name is 'Nevada'
    query = "SELECT * FROM states WHERE name = 'Nevada' ORDER BY id ASC;"
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

    '''
import MySQLdb
import sys
connect = MySQLdb.connect(
        host="localhost", user=sys.argv[1], password=sys.argv[2],
        database=sys.argv[3], port=3306
)
input_name = sys.argv[4]
cursor = connect.cursor()
query = """
    SELECT *
    FROM states
    WHERE name LIKE BINARY '{}%'
    ORDER BY id ASC;
    """.format(input_name)
cursor.execute(query)
for obj in cursor:
    print(obj)
cursor.close()
connect.close()
'''