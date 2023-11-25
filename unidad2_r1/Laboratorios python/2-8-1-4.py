"""
    Elaborado por:  Cristopher López Jiménez
    Descripción:    Laboratorios R1
"""

def read_int(prompt, min, max):

    while True:
        try:
            response = int(input(prompt))
            if min <= response <= max:
                return response
            else:
                print("Error: el valor no esta dentro del rango " + str(min) + ".." + str(max))
        except ValueError:
            print("Error, entrada equivocada")

v = read_int("Ingresa un numero de -10 al 10: ", -10, 10)

print("El numero es:", v)