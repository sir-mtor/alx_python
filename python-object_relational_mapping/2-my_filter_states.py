'''
import MySQLdb
import sys

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = 'Nevada' ORDER BY id ASC;"
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

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
connect.close(). 