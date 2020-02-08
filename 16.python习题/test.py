import openpyxl

wb = openpyxl.load_workbook('def_amount.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
re = sheet.max_row
print(re)