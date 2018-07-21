from mysql.connector.connection import MySQLConnection  # pip install mysql-connector
import json

from config import debug_logger, mysql_config_file_path


class SqlConnector:
    def __init__(self):
        self.cnx = None
        self.mysql_config = None

    def read_config(self):
        with open(mysql_config_file_path, 'r') as config_file:
            self.mysql_config = json.loads(config_file.read())
            debug_logger(f"MySQL config loaded: {self.mysql_config}")

    def open_cnx(self):
        self.read_config()
        self.cnx = MySQLConnection(**self.mysql_config)
        debug_logger("Successfully opened MySQLConnection")

    def execute_in_cursor(self, command):
        cursor = self.cnx.cursor()
        cursor.execute(command)
        result = list(cursor)
        cursor.close()
        return result

    def close_cnx(self):
        self.cnx.close()

## TODO: make open_cnx > callback > close_cnx
if __name__ == '__main__':
    print("Testing SqlConnector...")
    s = SqlConnector()
    s.open_cnx()
    print(s.execute_in_cursor("SHOW DATABASES"))
    print(s.execute_in_cursor("SHOW TABLES"))
    s.close_cnx()
    print("SqlConnector tests successful")
