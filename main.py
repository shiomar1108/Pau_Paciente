import sys
import glob
from tkinter import *
from PIL import ImageTk, Image
sys.path.append("./00_src/")
from Functions import create_report, new_patient
file = "./01_Data/shiomar_salazar.xlsx"

def option1():
    master = Toplevel()
    master.title("Nuevo Paciente")
    Label(master, text="Nombre del Paciente: ", font=("Calibri", 20)).grid(row=0)
    e1 = Entry(master, font=("Calibri Bold", 20), width = 20)
    e1.grid(row=0, column=1)

    def btn_new_patient():
        print("hola")
        new_patient(e1.get())
        master.destroy()

    Button(master, text='Capturar Datos',font=("Calibri", 15), width = 20 , command=master.destroy).grid(row=3, column=0, pady=4)
    Button(master, text='Cerrar',font=("Calibri", 15), width= 20 , command= btn_new_patient).grid(row=3, column=1, pady=4)


def option2():
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
        index = listbox.curselection()
        temp = file_list[index[0]]
        text = temp[10:-4]
        create_report(text)
        master.destroy()

    panel0 = Button(master, text="Iniciar Captura ", font=("Calibri", 20), command=master.destroy)
    panel0.pack(side="top", fill="both", expand='yes')
    panel1 = Button(master, text="Generar Reporte", font=("Calibri", 20), command=btn_gene_rep)
    panel1.pack(side="top", fill="both", expand='yes')
    panel2 = Button(master, text="Cerrar", font=("Calibri", 20), command=master.destroy)
    panel2.pack(side="top", fill="both", expand='yes')


def option3():
    master = Toplevel()
    master.title("Generar Reporte")
    master.geometry('400x300')
    panel = Label(master, text="Lista de Pacientes: ", font=("Calibri", 20))
    panel.pack(side="top", fill="both", expand="yes")
    listbox = Listbox(master)
    file_list = glob.glob("./01_Data/*.xls")
    for name in file_list:
        text = name[10:]
        listbox.insert('end', text)
    listbox.pack(side="top", fill="both", expand="yes")

    def btn_gene_rep():
        index = listbox.curselection()
        temp = file_list[index[0]]
        text = temp[10:-4]
        create_report(text)
        master.destroy()

    panel1 = Button(master, text="Generar Reporte", font=("Calibri", 20), command=btn_gene_rep)
    panel1.pack(side="top", fill="both", expand='yes')
    panel2 = Button(master, text="Cerrar", font=("Calibri", 20), command=master.destroy)
    panel2.pack(side="top", fill="both", expand='yes')


window = Tk()

window.title("Alimente Desktop App")
window.geometry('750x800')

img = ImageTk.PhotoImage(Image.open("./00_src/logo.png"))
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