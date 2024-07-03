# funcion calcular pies
def functionFoots(valorPies):
    valorPies = float(valorPies)
    valorMetros = round(valorPies / 3.281, 2)
    print(valorPies, "Pies", "en metros son -->", valorMetros, "mts")


# funcion calcular pulgadas
def functionInches(valorInches):
    valorInches = float(valorInches)
    valorCm = round(valorInches * 2.54, 2)
    print(valorInches, "Pulgadas en centimetros son -->", valorCm, "cm")


# funcion transformar millas
def functionMillas(valorMillas):
    valorMillas = float(valorMillas)
    valorKm = round(valorMillas * 1.609, 2)
    print(valorMillas, "Millas en Km son -->", valorKm, 'Km')


# lista de opciones
opciones = ["Transformar Pulgadas", "Transformar Pies", "Transformar Millas"]

for i, opcion in enumerate(opciones):
    print(f"{i+1}. {opcion}")

seleccion = input("Selecciona una opción: ")
seleccion = int(seleccion)
opcion_elegida = opciones[seleccion - 1]

if opcion_elegida == "Transformar Pies":
    valorPies = input("Ingrese la cantidad de pies que quiere transformar a metros: ")
    
    functionFoots(valorPies)
elif opcion_elegida == "Transformar Pulgadas":
    valorInches = input("Ingrese la cantidad de pulgadas que quiere transformar a centimetros: ")
    
    functionInches(valorInches)
elif opcion_elegida == "Transformar Millas":
    valorMillas = input("Ingrese la cantidad de millas que quiere transformar a Km: ")
    
    functionMillas(valorMillas)
