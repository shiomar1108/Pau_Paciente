import os
import pandas as pd
import matplotlib
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from fpdf import FPDF
import time

header = "Fecha \t Edad \t Talla \t Peso \t IMC \t % De Grasa \t % De Masa Muscular \t % De Grasa Vicesal \t Edad Metabolica \t C. Pecho \t C. Cintura \t C. Cadera \t C. Brazo Rep \t C. Brazo Cont \t C. Pierna \t % De Agua \t Glucosa \t PA \t Observaciones"
inputs = header.split(" \t ")
#paciente = raw_input(" Di el nombre del paciente:  ")
paciente = "ShiOMAr SAlaZAr"
archivo = (paciente.replace(" ","_").lower()) + ".txt"
reporte = (paciente.replace(" ","_").lower()) + ".pdf"
ruta = "./01_Datos/" + archivo
ruta_reporte = "./02_Reportes/" + reporte

def pacienteNuevo(f):
    f.write(header)
    f.write("\n")

def pacienteViejo(f):
    for elements in inputs[1:]:
        f.write(raw_input(("Diga "+elements+":  ")))
        f.write(" \t ")

def expediente():
    exists = os.path.isfile(ruta)
    dia =time.strftime("%x")
    if not exists:
        f = open(ruta,"w")
        print("\n Nuevo Paciente...")
        pacienteNuevo(f)
        f.write(dia + " \t ")
        pacienteViejo(f)
    else:
        f = open(ruta,"a")
        print("\n Paciente encontrado...")
        #f.write(dia + " \t ")
        #pacienteViejo(f)
        #f.write("\n")
    f.close()
    return f

def reporte(f):
    f = open(ruta,"r")
    lines = f.read().splitlines()
    num = (len(lines)-1)
    ultima = lines[num].split(" \t ")
    ultima1 = lines[num-1].split(" \t ")
    ultima2 = lines[num-2].split(" \t ")
    ultima3 = lines[num-3].split(" \t ")

    fechas = []
    porcentaje = []
    for i in range(1,num):
        temp = lines[i].split(" \t ")
        fechas.append(temp[0])
        porcentaje.append(temp[5])

    title("Evolucion % De Grasa")
    xlabel('Fecha')
    ylabel('% De Grasa')


    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 12)
    pdf.cell(60)
    pdf.cell(75, 10, "Reporte de Avance de Paciente: " + paciente.capitalize(), 0, 2, 'C')
    pdf.cell(90, 10, " ", 0, 1, 'C')
    pdf.cell(90, 10, " ", 0, 1, 'C')
    pdf.set_font('arial', 'B', 10)
    for i in range(19):
        pdf.cell(37, 8, inputs[i], 1, 0, 'C')
        pdf.cell(37, 8, ultima3[i], 1, 0, 'C')
        pdf.cell(37, 8, ultima2[i], 1, 0, 'C')
        pdf.cell(37, 8, ultima1[i], 1, 0, 'C')
        pdf.cell(37, 8, ultima[i], 1, 1, 'C')
    pdf.cell(-90)
    pdf.output(ruta_reporte, 'F')

def main():
    f = expediente()
    reporte(f)
    print ("\n DONE \n")

if __name__ == "__main__":
    main()