from pandas import read_excel  # pip install pandas
from urllib2 import urlopen


class ExcelLoader:
    def __init__(self, req_url, excel_path, sheet_name):
        self.req_url

    @staticmethod
    def dl_excel(req_url, excel_path):
        contents = urllib2.urlopen(req_url).read()
        with open(excel_path, "wb") as f: f.write(contents)
        print("Successfully written: ", excel_path)

    @staticmethod
    def load_excel(excel_path):
        data_frame = read_excel(excel_path, sheet_name=None, dtype=str, na_filter=False)
        data_dict = {}
        for frame in data_frame:
            data_dict[frame] = list(data_frame[frame].itertuples())
        return data_dict

if __name__ == '__main__':
    print("Testing ExcelLoader...")
    req_url = "https://docs.google.com/spreadsheets/d/1Ocd8JNLV8IAKWyxKdmcYaGeu09pbH3R5jlf6_PxoUhs/export?format=xlsx"
    excel_path = "temp.xlsx"
    print(ExcelLoader.dl_excel(req_url, excel_path))
    print(ExcelLoader.load_excel(excel_path,))
    print("ExcelLoader tests successful")
