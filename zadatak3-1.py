import openpyxl as openpyxl

wb=openpyxl.load_workbook('proizvodi.xlsx')
ws=wb.active

c=ws["A2":"C6"]

for i in c:
    print("Naziv:",i[0].value)
    print("Kolicina:",i[1].value)
    print("Cena:",i[2].value)
    print("Vrednost:",i[1].value*i[2].value)
    print("="*25)