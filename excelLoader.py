from pandas import read_excel  # pip install pandas

from config import excel_test_file_path


class ExcelLoader:
    @staticmethod
    def load_excel(excel_path=None):
        if not excel_path: excel_path = excel_test_file_path
        data_frame = read_excel(excel_path, sheet_name=None, dtype=str)
        data_dict = {}
        for frame in data_frame:
            data_dict[frame] = list(data_frame[frame].itertuples())
        return data_dict

if __name__ == '__main__':
    print("Testing ExcelLoader...")
    print(ExcelLoader.load_excel())
    print("ExcelLoader tests successful")
