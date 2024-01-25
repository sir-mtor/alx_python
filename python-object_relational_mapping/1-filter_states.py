
import MySQLdb
import sys 

def filter_states_by_name_starting_with_N(username, password, database):
    
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    filter_states_by_name_starting_with_N(mysql_username, mysql_password, database_name)
