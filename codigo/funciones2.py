from random import uniform
import csv

matrizActas = []
matrizComparativo = []
matrizEducacion = []
matrizIndicadores = []
matrizJrv = []
matrizOcupado = []
matrizPea = []
matrizPiramide = []
matrizSeguro = []
matrizTic = []


def leerCsv(nombreArchivo, nombreMatriz):	
    archivo = open(nombreArchivo, "rU")
    lector = csv.reader(archivo, delimiter=",")
    indice = 0	
    for fila in lector:
        nombreMatriz.append(fila)
        indice += 1
    archivo.close()


def obtenerVotantesCanton(canton, provincia):
    total = 0
    for i in matrizJrv:
        if (i[0] == provincia) & (i[1] == canton):
            total += int(i[5])
    return total


def esHombre():
    return (uniform(0, 1) * 100) < 49


def obtenerPromedioDeOcupantes(canton):
    for i in matrizIndicadores:
        if i[0] == canton:
            return i[9]
    return -1


def obtenerPromedioAlfabetismo(canton, edad):
    for i in matrizIndicadores:
        if i[0] == canton:
            if edad < 25:
                return i[13]
            return i[14]
    return -1


def estaDesempleado(canton):
    for i in matrizIndicadores:
        if i[0] == canton:
            return (uniform(0, 1)*100) < float(i[23])
    return -1


def estaAsegurado(canton):
    for i in matrizIndicadores:
        if i[0] == canton:
            return (uniform(0, 1)*100) < float(i[27])
    return -1


def obtenerEdad(canton, esHombre):  # 6-19
    ages = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
    sexo = "Hombres" if esHombre else "Mujeres"
    for i in matrizPiramide:
        if (i[0] == canton) & (i[1] == sexo):
            rangos = i[6:]
            total = sum(float(n) for n in rangos)
            ageSeed = uniform(0, total)
            print("ageSeed: "+str(ageSeed))
            ageIndex = -1
            for j, k in enumerate(rangos):
                if ageSeed < sum(float(n) for n in rangos[:j]):
                    ageIndex = j
                    break
            age = ages[ageIndex]
            return age
    return -1


def obtenerCantones(provincia): 
    # inestable
    cantones = []
    for i in matrizJrv:
        if i[0] == provincia:
            cant = i[1].lower()
            if cant == "central":
                cant = i[0].lower()
            if cant not in cantones:
                cantones.append(cant.lower())
    return cantones


provincias = [
    "CARTAGO",
    "SAN JOSE",
    "ALAJUELA",
    "PUNTARENAS",
    "GUANACASTE",
    "HEREDIA",
    "LIMON"
    ]


def obtenerCantonesTodos():
    return sum(list(obtenerCantones(y) for y in provincias), [])


leerCsv("../resources/actas.csv", matrizActas)
leerCsv("../resources/comparativo.csv", matrizComparativo)
leerCsv("../resources/educacion.csv", matrizEducacion)
leerCsv("../resources/indicadores.csv", matrizIndicadores)
leerCsv("../resources/jrv.csv", matrizJrv)
leerCsv("../resources/ocupado.csv", matrizOcupado)
leerCsv("../resources/pea.csv", matrizPea)
leerCsv("../resources/pramide.csv", matrizPiramide)
leerCsv("../resources/seguro.csv", matrizSeguro)
leerCsv("../resources/tic.csv", matrizTic)

print(len(obtenerCantonesTodos()))

print(esHombre())
print(obtenerVotantesCanton("ESCAZU", "SAN JOSE"))
print(obtenerPromedioDeOcupantes("Moravia"))
print(obtenerPromedioAlfabetismo("Moravia", 20))
print(obtenerPromedioAlfabetismo("Moravia", 50))
print(estaDesempleado("Moravia"))
print(estaAsegurado("Moravia"))
print(obtenerEdad("Moravia", esHombre()))