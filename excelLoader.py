import pandas  # pip install pandas xlrd

import urllib.request
import os


class ExcelLoader:
    def __init__(self, req_url, excel_path="temp.xlsx"):
        self.req_url = req_url
        self.excel_path = excel_path

    def __call__(self):
        self.dl_excel()
        excel_dict = self.load_excel()
        self.rm_excel()
        return excel_dict

    def dl_excel(self):
        if os.path.exists(self.excel_path):
            print(f"File already exists: {self.excel_path}")
            return
        print(f"Downloading file from: {self.req_url}")
        contents = urllib.request.urlopen(self.req_url).read()
        with open(self.excel_path, "wb") as out_file:
            out_file.write(contents)
        print(f"Successfully written to file: {self.excel_path}")

    def load_excel(self):
        data_frame = pandas.read_excel(self.excel_path, sheet_name=None, dtype=str, na_filter=False)
        data_dict = {}
        for frame in data_frame:
            data_dict[frame] = list(data_frame[frame].itertuples())
        return data_dict

    def rm_excel(self):
        os.remove(self.excel_path)
        print(f"Successfully deleted file: {self.excel_path}")


if __name__ == '__main__':
    req_url = "https://docs.google.com/spreadsheets/d/1Ocd8JNLV8IAKWyxKdmcYaGeu09pbH3R5jlf6_PxoUhs/export?format=xlsx"
    print("Testing ExcelLoader...")
    el = ExcelLoader(req_url)
    print(f"Sheets in dict: {el().keys()}")
    import code; code.interact(local={**locals(), **globals()})
''' code generator
import re
sheets = el()
quarter_num = '1'
levels_list = ['11', '12']
strand_regex = "^(?!nonSHS|NotLoaded)"

shs_sections = [section.name for section in sheets['Sections'] if section.level in levels_list]
shs_strands = [strand.strand for strand in sheets['Strands'] if re.match(strand_regex, strand.strand)]
shs_subjects = [subject for subject in sheets['Subjects'] if \
    quarter_num in subject.quarterNum and \
    subject.sectionName in shs_sections and \
    subject.strand in shs_strands]

    for (level, section_name, strand) in [(_level, _section_name, _strand) \
            for _level in levels_list \
            for _section_name in shs_sections \
            for _strand in shs_strands]:
        loaded_subjects = [s.Subject for s in shs_subjects if s.sectionName == section_name and s.strand == strand]
        if not loaded_subjects: continue
        print("\n", level, section_name, strand)
        print(loaded_subjects)

template_1 = """\tparts.add(new compUtil("%s", 1.0 / %s * 1000));"""
template_2 = """
if (strand.matches("%s") && section.equals("%s") && level.matches("%s") && quarterNum > 2) {
    ArrayList<compUtil> parts = new ArrayList<compUtil>();
    String compName = "Average";
    %s
    addNewGrade(parts, compName);
}"""

'''
