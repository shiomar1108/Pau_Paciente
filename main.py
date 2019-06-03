import sys
sys.path.append("./00_src/")
from create_report import create_report

header = ["Fecha", "Edad", "Talla", "Peso", "IMC", "% De Grasa", "% De Masa Muscular", "% De Grasa Vicesal", "Edad Metabolica", "C. Pecho","C. Cintura", "C. Cadera", "C. Brazo Rep", "C. Brazo Cont", "C. Pierna", "% De Agua", "Glucosa", "PA", "Observaciones"]
file = "./01_Data/shiomar_salazar.xlsx"

def main():
    create_report(file)


if __name__ == '__main__':

    main()
    print ("DONE...")


