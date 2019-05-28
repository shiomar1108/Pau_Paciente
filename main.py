import os

paciente = raw_input(" Di el nombre del paciente:  ")
archivo = (paciente.replace(" ","_").lower()) + ".txt"
ruta = "./01_Datos/" + archivo

exists = os.path.isfile(ruta)

if exists:
	f = open(ruta,"a")
else:
	f = open(ruta,"w")

print ("\n DONE \n")