from sqlConnector import SqlConnector
from excelLoader import ExcelLoader

import sys


translate_table = {
    "Faculties": "faculty",
    "Sections": "sections",
    "Students": "students",
    "Subjects": "subjects",
}

def main():
    excel_path = sys.argv[1] if len(sys.argv) > 1 else None
    data_dict = ExcelLoader.load_excel(excel_path)
    tables_found = [table for table in data_dict if table in translate_table.keys()]

    connection = SqlConnector()
    connection.open_cnx()

    for table in tables_found:
        connection.execute_in_cursor(f"TRUNCATE {translate_table[table]}")
        table_col_count = connection.execute_in_cursor(f"SELECT count(*) FROM information_schema.columns WHERE table_name = '{translate_table[table]}';")[0][0]
        for row in data_dict[table]:
            row_str = ', '.join(map(lambda r: "'" + r + "'", row[1:table_col_count + 1]))
            connection.execute_in_cursor(f"INSERT INTO {translate_table[table]} VALUES ({row_str})")

    #import code;code.interact(local={**locals(), **globals()})
    connection.close_cnx()
    connection.print_error_log()


if __name__ == '__main__':
    main()