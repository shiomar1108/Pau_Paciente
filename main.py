import os

paciente = raw_input(" Di el nombre del paciente:  ")
archivo = (paciente.replace(" ","_").lower()) + ".txt"
ruta = "./01_Datos/" + archivo

exists = os.path.isfile(ruta)

if exists:
	f = open(ruta,"a")
else:
	f = open(ruta,"w")
	f.write("Edad \t Talla \t Peso \t IMC \t% De Grasa \t% De Masa Muscular \t % De Grasa Vicesal \t Edad Metabolica \t C. Pecho \t C. Cintura \t C. Cadera \t C. Brazo Rep \t C. Brazo Cont \t C. Pierna \t % De Agua \t Glucosa \t PA \t Observaciones")

print ("\n DONE \n")