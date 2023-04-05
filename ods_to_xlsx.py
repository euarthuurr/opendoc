import pyexcel as p
import glob, os

os.chdir(".")
for file in glob.glob("*.ods"):
    fname, fext = os.path.splitext(file)
    sheet = p.get_sheet(file_name = file)
    sheet.save_as(fname.lower() + '.xlsx')
    print(fname.lower() + '.xlsx')
    os.remove(file)