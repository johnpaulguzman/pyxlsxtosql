from sqlConnector import SqlConnector
from excelLoader import ExcelLoader

import sys


def main():
    excel_path = sys.argv[1] if len(sys.argv) > 1 else None
    data_dict = ExcelLoader.load_excel(excel_path)
    print(data_dict)

    connection = SqlConnector()
    connection.open_cnx()
    res = connection.execute_in_cursor("SELECT * FROM students")
    print(res)
    ## TODO continue
    import code;code.interact(local={**locals(), **globals()})
    connection.close_cnx()


if __name__ == '__main__':
    main()