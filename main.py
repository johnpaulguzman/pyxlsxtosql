from sqlConnector import SqlConnector
from excelLoader import ExcelLoader

import sys


translate_table = {
    "Faculties": "faculty",
    "Sections": "sections",
    "Students": "students",
    "Subjects": "subjects",
#    "Example Test":1,
}

def main():
    excel_path = sys.argv[1] if len(sys.argv) > 1 else None
    data_dict = ExcelLoader.load_excel(excel_path)
    tables_found = [table for table in data_dict if table in translate_table.keys()]

    connection = SqlConnector()
    connection.open_cnx()

    for table in tables_found:
        connection.execute_in_cursor(f"TRUNCATE {translate_table[table]}")
        #connection.execute_in_cursor(f"""INSERT INTO {translate_table[table]}""")

    ## TODO continue
    import code;code.interact(local={**locals(), **globals()})
    connection.close_cnx()


if __name__ == '__main__':
    main()