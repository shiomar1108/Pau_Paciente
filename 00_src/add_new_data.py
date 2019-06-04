import xlrd
import xlwt
import time
from xlutils.copy import copy
header = ["Fecha", "Edad", "Talla", "Peso", "IMC", "% De Grasa", "% De Masa Muscular", "% De Grasa Vicesal", "Edad Metabolica", "C. Pecho","C. Cintura", "C. Cadera", "C. Brazo Rep", "C. Brazo Cont", "C. Pierna", "% De Agua", "Glucosa", "PA", "Observaciones"]

def add_new_data(file):
    data = []
    temp = time.strftime("%m/%d/%Y")
    data.append(temp)
    for i in range(1,19):
        text = "Diga " + header[i] + " :  "
        data.append(raw_input(text))

    rb = xlrd.open_workbook(file)
    r_sheet = rb.sheet_by_index(0) 
    r = r_sheet.nrows
    wb = copy(rb) 
    sheet = wb.get_sheet(0)
    for i in range(0,19):
        sheet.write(r,i,data[i])
    wb.save(file)




