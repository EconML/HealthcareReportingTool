import xlrd
import xlutils.copy import copy

loc = ("worksheet.xlsx")

wb = xlrd.open_workbook(loc)


print(wb.sheet_names())

sheet = wb.sheet_by_index(0)
rb = copy(wb)
w_sheet = rb.get_sheet(0)

print(sheet.cell(0,0))
w_sheet.write(0,0,'Change')
rb.save()
print(sheet.cell(0,0))

