import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt
header = ["Fecha", "Edad", "Talla", "Peso", "IMC", "% De Grasa", "% De Masa Muscular", "% De Grasa Vicesal", "Edad Metabolica", "C. Pecho","C. Cintura", "C. Cadera", "C. Brazo Rep", "C. Brazo Cont", "C. Pierna", "% De Agua", "Glucosa", "PA", "Observaciones"]
header2 = ["Fecha", "Edad", "Talla", "Peso", "IMC", "% De Grasa", "% De Masa Muscular", "% De Grasa Vicesal", "Edad Metabolica", "C. Pecho","C. Cintura", "C. Cadera", "C. Brazo Rep", "C. Brazo Cont", "C. Pierna", "% De Agua", "Glucosa", "PA", "Observaciones"]


def create_report(file):
    #read excel
    df = pd.read_excel(file)

    #Retrieve data for graphic
    fechas = df["Fecha"].to_numpy()
    porcentajes = df["% De Grasa"].to_numpy()
    masas = df["% De Masa Muscular"].to_numpy()
    imcs = df["IMC"].to_numpy()
    puntos = df[header[0]].count()

    #Graph creation
    plt.title('Evolucion del paciente')
    plt.xlabel('Fechas')
    plt.plot(fechas,porcentajes, label="% de grasa", color = "b")
    plt.plot(fechas,masas, label="& de Masa Muscular", color = "r")
    plt.plot(fechas,imcs, label="IMC", color = "k")
    plt.legend()
    plt.axis([0, puntos, 0, 100])
    plt.savefig('./00_src/report.png', dpi=90)

    #create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.image('./00_src/logo.png', 10, 8, 40)
    pdf.set_font('arial', 'B', 12)
    pdf.cell(60)
    pdf.cell(0, 30, "Reporte de consulta de Paciente", 0, 2, 'C')
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-50)
    pdf.set_font('arial', '', 5)
    #for elements in header2:
    pdf.multi_cell(10, 20, "Test\nTest\nTest\t", 1, 0, 'C')
    pdf.image('./00_src/report.png', x=30, y=170, w=170, h=120, type='', link='https://www.facebook.com/pauwattynutri/')
    pdf.output('./02_Reports/test.pdf', 'F')