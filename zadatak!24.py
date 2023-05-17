import openpyxl as openpyxl

wb=openpyxl.load_workbook("eksel1.xlsx")

ws=wb.active

c=ws["A1"]
c.style=c.style.copy(font=c.style.font.copy(bold=True))