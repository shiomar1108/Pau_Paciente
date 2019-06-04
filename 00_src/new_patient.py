import xlrd
import xlwt
header = ["Fecha", "Edad", "Talla", "Peso", "IMC", "% De Grasa", "% De Masa Muscular", "% De Grasa Vicesal", "Edad Metabolica", "C. Pecho","C. Cintura", "C. Cadera", "C. Brazo Rep", "C. Brazo Cont", "C. Pierna", "% De Agua", "Glucosa", "PA", "Observaciones"]


def new_patient (name):
    file = "./01_Data/" + name.replace(" ", "_").lower() + ".xls"

    book = xlwt.Workbook()
    sheet = book.add_sheet("2019")
    for i in range(19):
        sheet.write(0, i, header[i])
    book.save(file)
    return file
