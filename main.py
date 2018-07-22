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
        for row in data_dict[table]:
            row_str = ', '.join(map(lambda r: "'" + r + "'", row[1:]))
            connection.execute_in_cursor(f"INSERT INTO {translate_table[table]} VALUES ({row_str})")

    #import code;code.interact(local={**locals(), **globals()})
    #TODO FIX 'nan' reading missing columns or maybe just replace with " "
    connection.close_cnx()
    connection.print_error_log()


if __name__ == '__main__':
    main()