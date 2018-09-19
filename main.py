from sqlConnector import SqlConnector
from excelLoader import ExcelLoader

import sys


schema_name = "grading"
translate_table = {
    "Faculties": "faculty",
    "Sections": "sections",
    "Students": "students",
    "Subjects": "subjects",
}


if __name__ == '__main__':
    excel_path = input("Drag and drop the Database Entries xlsx file here...")
    if excel_path.startswith('"') and excel_path.endswith('"'):
        excel_path = excel_path[1:-1]
    data_dict = ExcelLoader.load_excel(excel_path)
    tables_found = [table for table in data_dict if table in translate_table.keys()]
    ignore_row_start = ["NotEnrolled"]

    connection = SqlConnector()
    connection.open_cnx(schema_name)

    for table in tables_found:
        connection.execute_in_cursor(f"TRUNCATE {translate_table[table]};")
        table_col_count = connection.execute_in_cursor(f"SELECT count(*) FROM information_schema.columns WHERE table_name = '{translate_table[table]}';")[0][0]
        for idx, *row in data_dict[table]:
            if not row[0]: break  # assume end of data
            if row[0] in ignore_row_start: continue
            row_str = ', '.join(map(lambda r: f'"{r}"', row[ :table_col_count]))
            connection.execute_in_cursor(f'INSERT INTO {translate_table[table]} VALUES ({row_str});')

    connection.cnx.commit()
    connection.close_cnx()
    connection.print_error_log()
    input("Press Enter to exit...")