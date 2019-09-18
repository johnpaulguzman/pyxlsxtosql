import urllib2

if __name__ == '__main__':
    req_url = "https://docs.google.com/spreadsheets/d/1Ocd8JNLV8IAKWyxKdmcYaGeu09pbH3R5jlf6_PxoUhs/export?format=xlsx"
out_file = "temp.xlsx"
contents = urllib2.urlopen(req_url).read()
with open(out_file, "wb") as f: f.write(contents)
print("Successfully written: ", out_file)
