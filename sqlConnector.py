from mysql.connector.connection import MySQLConnection  # pip install mysql-connector
import json


config_local = {
    "user": "root",
    "password": "p@ssword",
    "host": "localhost",
    "port": 3306,
    "database": "grading"
}
config_remote = {
    "user": "root",
    "password": "p@ssword",
    "host": "10.20.11.60",
    "port": 3306,
    "database": "grading"
}

class SqlConnector:
    def __init__(self):
        self.cnx = None
        self.error_log = []

    def open_cnx(self, schema_name):
        try:
            self.cnx = MySQLConnection(**config_local)
        except:
            self.cnx = MySQLConnection(**config_remote)
        self.cnx.database = schema_name
        print("Successfully opened MySQLConnection")

    def execute_in_cursor(self, command):
        try:
            cursor = self.cnx.cursor()
            cursor.execute(command)
            result = list(cursor)
            cursor.close()
            print(f"Query results for ( {command} ): {result}")
            return result
        except Exception as e:
            print(f"Query error occured {e}")
            self.error_log += [(command, e)]
            print(command)
            #raise e
        finally:
            cursor.close()

    def close_cnx(self):
        self.cnx.close()

    def print_error_log(self):
        if not self.error_log: return print("No errors logged.\nDatabase update successful!")
        print("Errors logged:")
        for error in self.error_log:
            print(error)
        print("Database update unsuccessful!")

## TODO: make open_cnx > callback > close_cnx
if __name__ == '__main__':
    print("Testing SqlConnector...")
    s = SqlConnector()
    s.open_cnx()
    print(s.execute_in_cursor("SHOW DATABASES"))
    print(s.execute_in_cursor("SHOW TABLES"))
    s.close_cnx()
    print("SqlConnector tests successful")
