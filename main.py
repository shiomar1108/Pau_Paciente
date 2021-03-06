import glob
import os
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import xlrd
import xlwt
import time
from xlutils.copy import copy
import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt

header = ["Fecha", "Edad", "Talla", "Peso", "IMC", "% De Grasa", "% De Masa Muscular", "% De Grasa Viceral", "Edad Metabolica", "C. Pecho","C. Cintura", "C. Cadera", "C. Brazo Rep", "C. Brazo Cont", "C. Pierna", "% De Agua", "Glucosa", "PA", "Observaciones"]
header2 = ["Fecha", "Edad", "Talla", "Peso", "IMC", "% Grasa", "%  M M", "% De G V", "Edad M", "C. Pecho","C. Cintura", "C. Cadera", "C. Brazo R", "C. Brazo C", "C. Pierna", "% De Agua", "Glucosa", "PA", "Observaciones"]

def new_patient (name):
    file = "./01_Data/" + name.replace(" ", "_").lower() + ".xls"
    book = xlwt.Workbook()
    sheet = book.add_sheet("2019")
    for i in range(19):
        sheet.write(0, i, header[i])
    book.save(file)

def create_report(name):
    #create path
    file = "./01_Data/" + name + ".xls"
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
    plt.plot(fechas,masas, label="% de Masa Muscular", color = "r")
    plt.plot(fechas,imcs, label="IMC", color = "k")
    plt.legend()
    plt.axis([0, puntos, 0, 100])
    plt.savefig('report.png', dpi=90)
    #Get patients Name
    paciente = file[10:-4].replace("_"," ").title()
    #Get Pdf file
    pdf_path = "./02_Reports/" + file[10:-4] +".pdf"
    #create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.image('logo.png', 10, 8, 40)
    pdf.set_font('arial', 'B', 12)
    pdf.cell(60)
    pdf.cell(0, 30, "Reporte de consulta de Paciente"+"  " + paciente, 0, 2, 'C')
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
    pdf.image('report.png', x=30, y=170, w=170, h=120, type='', link='https://www.facebook.com/pauwattynutri/')
    pdf.output(pdf_path, 'F')
    os.remove("report.png")


def write_excel (data, file):
    rb = xlrd.open_workbook(file)
    r_sheet = rb.sheet_by_index(0)
    r = r_sheet.nrows
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    for i in range(0, 19):
        sheet.write(r, i, data[i])
    wb.save(file)


def add_new_data(name):
    # create path
    file = "./01_Data/" + name + ".xls"
    data = []
    temp = time.strftime("%m/%d/%Y")
    data.append(temp)

    window = Tk()
    window.title("Captura de Datos")
    window.geometry('600x600')

    a = Label(window, text=header[1], font=("Calibri", 15)).grid(row=0, column=0)
    b = Label(window, text=header[2], font=("Calibri", 15)).grid(row=1, column=0)
    c = Label(window, text=header[3], font=("Calibri", 15)).grid(row=2, column=0)
    f = Label(window, text=header[5], font=("Calibri", 15)).grid(row=4, column=0)
    g = Label(window, text=header[6], font=("Calibri", 15)).grid(row=5, column=0)
    h = Label(window, text=header[7], font=("Calibri", 15)).grid(row=6, column=0)
    i = Label(window, text=header[8], font=("Calibri", 15)).grid(row=7, column=0)
    j = Label(window, text=header[9], font=("Calibri", 15)).grid(row=8, column=0)
    k = Label(window, text=header[10], font=("Calibri", 15)).grid(row=9, column=0)
    l = Label(window, text=header[11], font=("Calibri", 15)).grid(row=10, column=0)
    m = Label(window, text=header[12], font=("Calibri", 15)).grid(row=11, column=0)
    n = Label(window, text=header[13], font=("Calibri", 15)).grid(row=12, column=0)
    o = Label(window, text=header[14], font=("Calibri", 15)).grid(row=13, column=0)
    p = Label(window, text=header[15], font=("Calibri", 15)).grid(row=14, column=0)
    q = Label(window, text=header[16], font=("Calibri", 15)).grid(row=15, column=0)
    r = Label(window, text=header[17], font=("Calibri", 15)).grid(row=16, column=0)
    s = Label(window, text=header[18], font=("Calibri", 15)).grid(row=17, column=0)

    a1 = Entry(window, width=30, font=("Calibri", 15))
    a1.grid(row=0, column=1)
    b1 = Entry(window, width=30, font=("Calibri", 15))
    b1.grid(row=1, column=1)
    c1 = Entry(window, width=30, font=("Calibri", 15))
    c1.grid(row=2, column=1)
    e1 = Entry(window, width=30, font=("Calibri", 15))
    e1.grid(row=4, column=1)
    f1 = Entry(window, width=30, font=("Calibri", 15))
    f1.grid(row=5, column=1)
    g1 = Entry(window, width=30, font=("Calibri", 15))
    g1.grid(row=6, column=1)
    h1 = Entry(window, width=30, font=("Calibri", 15))
    h1.grid(row=7, column=1)
    i1 = Entry(window, width=30, font=("Calibri", 15))
    i1.grid(row=8, column=1)
    j1 = Entry(window, width=30, font=("Calibri", 15))
    j1.grid(row=9, column=1)
    k1 = Entry(window, width=30, font=("Calibri", 15))
    k1.grid(row=10, column=1)
    l1 = Entry(window, width=30, font=("Calibri", 15))
    l1.grid(row=11, column=1)
    m1 = Entry(window, width=30, font=("Calibri", 15))
    m1.grid(row=12, column=1)
    n1 = Entry(window, width=30, font=("Calibri", 15))
    n1.grid(row=13, column=1)
    o1 = Entry(window, width=30, font=("Calibri", 15))
    o1.grid(row=14, column=1)
    p1 = Entry(window, width=30, font=("Calibri", 15))
    p1.grid(row=15, column=1)
    q1 = Entry(window, width=30, font=("Calibri", 15))
    q1.grid(row=16, column=1)
    r1 = Entry(window, width=30, font=("Calibri", 15))
    r1.grid(row=17, column=1)

    def btn_submit():
        try:
            data.append(a1.get())
            data.append(b1.get())
            data.append(c1.get())
            z = int(a1.get())
            x = float(b1.get())
            y = float(c1.get())
            d1 = (y/(pow(x/100, 2)))
            data.append(round(d1,2))
            data.append(e1.get())
            data.append(f1.get())
            data.append(g1.get())
            data.append(h1.get())
            data.append(i1.get())
            data.append(j1.get())
            data.append(k1.get())
            data.append(l1.get())
            data.append(m1.get())
            data.append(n1.get())
            data.append(o1.get())
            data.append(p1.get())
            data.append(q1.get())
            data.append(r1.get())
            write_excel(data,file)
            window.destroy()
        except PermissionError:
            messagebox.showerror("Error", "Cerrar el Excel para poder editarlo ")
            window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Ingrese Edad, Talla y Peso Correctamente ")
            window.destroy()

    Button(window, text='Guardar', font=("Calibri", 15), width=20, command=btn_submit).grid(row=18, column=1, pady=4)
    window.mainloop()

def option1():
    master = Toplevel()
    master.title("Nuevo Paciente")
    master.geometry('750x100')
    Label(master, text="Nombre del Paciente: ", font=("Calibri", 20)).grid(row=0)
    e1 = Entry(master, font=("Calibri", 20), width = 30)
    e1.grid(row=0, column=1)

    def btn_new_patient():
        if(e1.get() == ""):
            messagebox.showerror("Error", "Nombre del Paciente no puede estar vacio")
        else:
            new_patient(e1.get())
            master.destroy()

    def capture_new():
        if (e1.get() == ""):
            messagebox.showerror("Error", "Nombre del Paciente no puede estar vacio")
        else:
            text = e1.get().replace(" ", "_").lower()
            new_patient(e1.get())
            add_new_data(text)
            master.destroy()

    Button(master, text='Capturar Datos',font=("Calibri", 15), width = 20 , command=capture_new).grid(row=3, column=0, pady=4)
    Button(master, text='Crear y Cerrar',font=("Calibri", 15), width= 20 , command= btn_new_patient).grid(row=3, column=1, pady=4)


def option2():
    master = Toplevel()
    master.title("Paciente Existente ")
    master.geometry('400x400')
    panel = Label(master, text="Lista de Pacientes: ", font=("Calibri", 20))
    panel.pack(side="top", fill="both", expand="yes")
    listbox = Listbox(master)
    file_list = glob.glob("./01_Data/*.xls")
    for name in file_list:
        text = name[10:]
        listbox.insert('end', text)
    listbox.pack(side="top", fill="both", expand="yes")

    def btn_captura():
        try:
            index = listbox.curselection()
            temp = file_list[index[0]]
            text = temp[10:-4]
            add_new_data(text)
        except IndexError:
            messagebox.showerror("Error", "Selecciona archivo de Paciente ")

    def btn_gene_rep():
        try:
            index = listbox.curselection()
            temp = file_list[index[0]]
            text = temp[10:-4]
            create_report(text)
            master.destroy()
        except IndexError:
            messagebox.showerror("Error", "Selecciona archivo de Paciente ")
            master.destroy()

    panel0 = Button(master, text="Iniciar Captura ", font=("Calibri", 20), command=btn_captura)
    panel0.pack(side="top", fill="both", expand='yes')
    panel1 = Button(master, text="Generar Reporte", font=("Calibri", 20), command=btn_gene_rep)
    panel1.pack(side="top", fill="both", expand='yes')
    panel2 = Button(master, text="Cerrar", font=("Calibri", 20), command=master.destroy)
    panel2.pack(side="top", fill="both", expand='yes')


def option3():
    master = Toplevel()
    master.title("Generar Reporte")
    master.geometry('400x400')
    panel = Label(master, text="Lista de Pacientes: ", font=("Calibri", 20))
    panel.pack(side="top", fill="both", expand="yes")
    listbox = Listbox(master)
    file_list = glob.glob("./01_Data/*.xls")
    for name in file_list:
        text = name[10:]
        listbox.insert('end', text)
    listbox.pack(side="top", fill="both", expand="yes")

    def btn_gene_rep():
        try:
            index = listbox.curselection()
            temp = file_list[index[0]]
            text = temp[10:-4]
            create_report(text)
            master.destroy()
        except IndexError:
            messagebox.showerror("Error", "Selecciona archivo de Paciente ")
            master.destroy()

    panel1 = Button(master, text="Generar Reporte", font=("Calibri", 20), command=btn_gene_rep)
    panel1.pack(side="top", fill="both", expand='yes')
    panel2 = Button(master, text="Cerrar", font=("Calibri", 20), command=master.destroy)
    panel2.pack(side="top", fill="both", expand='yes')


window = Tk()
window.title("Alimente Desktop App")
window.geometry('750x800')

img = ImageTk.PhotoImage(Image.open("./logo.png"))
panel1 = Label(window, image = img)
panel1.pack(side = "top", fill = "both", expand = "yes")

panel5 = Label(window, text="Bienvenida Dr. Paulina ", font=("Calibri Bold", 45))
panel5.pack(side = "top", fill = "both", expand = "yes")

panel2 = Button(window, text="Nuevo Paciente", font=("Calibri", 25), command = option1)
panel2.pack(side = "top", fill = "both", expand = 'yes')

panel3 = Button(window, text="Paciente Existente", font=("Calibri", 25), command = option2)
panel3.pack(side = "top", fill = "both", expand = 'yes')

panel4 = Button(window, text="Generar Reporte", font=("Calibri", 25), command = option3)
panel4.pack(side = "top", fill = "both", expand = 'yes')

window.mainloop()