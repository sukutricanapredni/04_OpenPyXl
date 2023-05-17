import openpyxl as openpyxl

wb=openpyxl.load_workbook('demo1.xlsx') ##Ucitava excel file

print(wb.sheetnames) ##vraca nazive sheetova