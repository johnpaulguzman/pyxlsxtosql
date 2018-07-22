import os


debug_logger = print
file_path = os.path.dirname(os.path.abspath(__file__))

config_dir = "config_files"
mysql_config_file = "mysql_config_local.json"
excel_test_file = "IHMC DB Entries.xlsx"

mysql_config_file_path = os.path.join(file_path, config_dir, mysql_config_file)
excel_test_file_path = os.path.join(file_path, config_dir, excel_test_file)
