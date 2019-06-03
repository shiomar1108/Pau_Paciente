from openpyxl import load_workbook
import time

header = ["Fecha", "Edad", "Talla", "Peso", "IMC", "% De Grasa", "% De Masa Muscular", "% De Grasa Vicesal", "Edad Metabolica", "C. Pecho","C. Cintura", "C. Cadera", "C. Brazo Rep", "C. Brazo Cont", "C. Pierna", "% De Agua", "Glucosa", "PA", "Observaciones"]

def add_new_data(file):
    data = []
    wb = load_workbook(file)
    temp = time.strftime("%d/%m/%Y")
    print(temp)
    data.append(temp)
    for i in range(1,19):
        text = "Diga " + header[i] + " :  "
        data.append(raw_input(text))
    print (data)
    sheet = wb.active
    sheet.append(data)
    wb.save(file)