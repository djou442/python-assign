
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy


book = xlrd.open_workbook("employeedata.xls")

sh = book.sheet_by_index(0)

rb = open_workbook("employeedata.xls")
wb = copy(rb)

s = wb.get_sheet(0)
q  

myString = sh.cell_value(rowx=1, colx=1)
myString = myString.replace("helpinghands.com", "handsinhands.org")

for rx in range(sh.nrows - 1):
    print("the unchange version {}".format(sh.row(rx)))
    myString = sh.cell_value(rowx=rx + 1, colx=1)
    myString = myString.replace("helpinghands.com", "handsinhands.org")
    print("the change version {}".format(myString))
    s.write(rx + 1, 1, myString)
wb.save('employeedata.xls')
