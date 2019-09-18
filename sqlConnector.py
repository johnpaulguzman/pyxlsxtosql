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
 TODO CONFIG ... 
class SqlConnector:
    def __init__(self, schema_name):
        self.schema_name = schema_name
        self.cnx = None
        self.error_log = []

    def __enter__(self, schema_name):
        try:
            self.cnx = MySQLConnection(**config_local)
        except:
            self.cnx = MySQLConnection(**config_remote)
        self.cnx.database = schema_name
        print("Successfully opened MySQLConnection")

    def __exit__(self):
        if self.cnx is not None:
            self.cnx.close()
            print("Successfully closed MySQLConnection")

    def execute_in_cursor(self, command):
        new_cursor = self.cnx.cursor()
        try:
            new_cursor.execute(command)
            result = list(new_cursor)
            new_cursor.close()
            print(f"Query results for ( {command} ): {result}")
            return result
        except Exception as e:
            print(f"Query error occured: {e}")
            self.error_log += [(command, e)]
        finally:
            new_cursor.close()

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
