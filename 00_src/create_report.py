import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt
header = ["Fecha", "Edad", "Talla", "Peso", "IMC", "% De Grasa", "% De Masa Muscular", "% De Grasa Vicesal", "Edad Metabolica", "C. Pecho","C. Cintura", "C. Cadera", "C. Brazo Rep", "C. Brazo Cont", "C. Pierna", "% De Agua", "Glucosa", "PA", "Observaciones"]
header2 = ["Fecha", "Edad", "Talla", "Peso", "IMC", "% Grasa", "%  M M", "% De G V", "Edad M", "C. Pecho","C. Cintura", "C. Cadera", "C. Brazo R", "C. Brazo C", "C. Pierna", "% De Agua", "Glucosa", "PA", "Observaciones"]


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

    #Get patients Name
    paciente = file[10:-5].replace("_"," ").title()

    #create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.image('./00_src/logo.png', 10, 8, 40)
    pdf.set_font('arial', 'B', 12)
    pdf.cell(60)
    pdf.cell(0, 30, "Reporte de consulta de Paciente"+"  " +paciente, 0, 2, 'C')
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-50)
    pdf.set_font('arial', '', 5)
    for elements in header2[:-1]:
        if(elements != header2[17]):
            pdf.cell(10, 10, elements, 1, 0, 'C')
        else:
            pdf.cell(10, 10, elements, 1, 1, 'C')
    for i in range(0, len(df)):
        for j in range(0,len(header)-1):
            if(j != 17):
                pdf.cell(10, 10, '%s' % (df[header[j]].ix[i]), 1, 0, 'C')
            else:
                pdf.cell(10, 10, '%s' % (df[header[j]].ix[i]), 1, 1, 'C')
    pdf.image('./00_src/report.png', x=30, y=170, w=170, h=120, type='', link='https://www.facebook.com/pauwattynutri/')
    pdf.output('./02_Reports/test.pdf', 'F')