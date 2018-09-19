from pandas import read_excel  # pip install pandas


class ExcelLoader:
    @staticmethod
    def load_excel(excel_path=None):
        data_frame = read_excel(excel_path, sheet_name=None, dtype=str, na_filter=False)
        data_dict = {}
        for frame in data_frame:
            data_dict[frame] = list(data_frame[frame].itertuples())
        return data_dict

if __name__ == '__main__':
    print("Testing ExcelLoader...")
    print(ExcelLoader.load_excel())
    print("ExcelLoader tests successful")
