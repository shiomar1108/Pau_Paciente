from openpyxl import load_workbook

def add_new_data(file):
    wb = load_workbook(file)
    data = ((10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10))
    sheet = wb.active
    sheet.append(data)
    wb.save(file)