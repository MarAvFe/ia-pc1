from random import uniform
import csv
from random import randint
import unicodedata
from random import uniform
from unicodedata import normalize

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

def normalize_text ( text ):
    return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').upper()


def leerCsv(nombreArchivo, nombreMatriz):   
    archivo = open(nombreArchivo, "rU")
    lector = csv.reader(archivo, delimiter=",")
    for fila in lector:
        filaTmp=[]
        for atributo in fila:
            atributoTmp= normalize_text(atributo)
            filaTmp.append(atributoTmp.decode('UTF-8'))
        nombreMatriz.append (filaTmp)
    archivo.close()


def obtener_muestra_pais(n):
    muestra = []
    for i in range(n):
        muestra.append(obtenerVotante())
    return muestra


def obtener_muestra_provincia(n, provincia):
    muestra = []
    for i in range(n):
        muestra.append(obtenerVotante(provincia))
    return muestra


def obtenerVotante(provincia=""):
    votante = []
    canton = obtenerCantonAleatorio(provincia)
    sexo = esHombre()
    edad = obtenerEdad(canton,sexo)
    votante.append(canton)
    votante.append(sexo)
    votante.append(edad)
    # Todos los indicadores
    votante.append(obtenerPromedioAlfabetismo(canton,edad))
    votante.append(obtenerPromedioDeOcupantes(canton))
    votante.append(estaAsegurado(canton))
    votante.append(estaDesempleado(canton))
    return votante


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


def estaDesempleado(canton, r=-1):
    aleatorio = uniform(0, 1) if r==-1 else r
    for i in matrizIndicadores:
        if i[0] == canton:
            return (aleatorio*100) < float(i[23])
    return -1


def estaAsegurado(canton, r=-1):
    aleatorio = uniform(0, 1) if r==-1 else r
    for i in matrizIndicadores:
        if i[0] == canton:
            return (aleatorio*100) < float(i[27])
    return -1


def obtenerEdad(canton, esHombre):  # 6-19
    ages = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
    sexo = "Hombres" if esHombre else "Mujeres"
    for i in matrizPiramide:
        if (i[0] == canton) & (i[1] == sexo):
            rangos = i[6:]
            total = sum(float(n) for n in rangos)
            ageSeed = uniform(0, total)
            ageIndex = -1
            for j, k in enumerate(rangos):
                if ageSeed < sum(float(n) for n in rangos[:j]):
                    ageIndex = j
                    break
            age = ages[ageIndex]
            return age
    return -1


def obtenerCantonesPoblacion(provincia=""): 
    cantones = []
    ultimoCanton = ""
    for i in matrizJrv:
        if (provincia != "") & (provincia != i[0]):
            continue
        if i[1] != ultimoCanton:
            ultimoCanton = i[1]
            cant = i[1].lower()
            if cant == "central":
                cant = i[0].lower()
            if cant not in cantones:
                cantones.append([cant.lower(),int(i[-1])])
        else:
            cantones[-1][1] += int(i[-1])
    return cantones


def obtenerCantonAleatorio(provincia=""): 
    cantonesPoblacion = obtenerCantonesPoblacion(provincia)
    total = sum(i[1] for i in cantonesPoblacion)
    cantonSeed = uniform(0,total)
    cantonIndex = -1
    for j, k in enumerate(cantonesPoblacion):
        if cantonSeed < sum(float(n[1]) for n in cantonesPoblacion[:j]):
            cantonIndex = j
            break
    canton = cantonesPoblacion[cantonIndex][0]
    return canton


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
print(estaDesempleado("Moravia"))
print(estaAsegurado("Moravia"))
print(obtenerEdad("Moravia", esHombre()))

print(len(obtenerCantonesPoblacion()))

print(obtenerCantonAleatorio())
print(obtenerCantonAleatorio("CARTAGO"))

print(obtener_muestra_pais(5))


def getDensidad(canton):
    for fila in matrizIndicadores:
        cantonCsv = fila[0]
        annoCsv = fila [1]
        densidad = fila [4]
        if (cantonCsv == canton and annoCsv == "2011" ): 
            densidad = fila[4] 
            return densidad


def esDependiente(canton, r=-1):
    random = randint(1,100) if r==-1 else r
    for fila in matrizIndicadores:
        cantonCsv = fila[0]
        annoCsv = fila [1]
        if (cantonCsv == canton and annoCsv == "2011" ): 
            dependencia = float(fila [7])
            return random>dependencia


def esBuenoEstadoDeVivienda(canton, r=-1):
    random = randint(1,100) if r==-1 else r
    for fila in matrizIndicadores:
        cantonCsv = fila[0]
        annoCsv = fila [1]
        if (cantonCsv == canton and annoCsv == "2011" ): 
            estadoVivienda = float(fila [10])
            return random<estadoVivienda

def annosAprobadosEducacionRegular(canton, edad):
    for fila in matrizIndicadores:
        cantonCsv = fila[0]
        annoCsv = fila [1]
        if (cantonCsv == canton and annoCsv == "2011" ): 
            if (edad <=49): 
                return matrizIndicadores[16]
            else:
                return matrizIndicadores[17]


def porcentajeAsistenciaEducacionRegular(canton, edad):
    for fila in matrizIndicadores:
        cantonCsv = fila[0]
        annoCsv = fila [1]
        if (cantonCsv == canton and annoCsv == "2011" ): 
            if (edad<=24):
                return matrizIndicadores[21]
            else: 
                return matrizIndicadores[22]


def tieneTrabajo(canton, genero, r=-1):
    random = randint(1,100) if r==-1 else r
    for fila in matrizIndicadores:
        cantonCsv = fila[0]
        annoCsv = fila [1]
        if (cantonCsv == canton and annoCsv == "2011" ): 
            if (genero==True):
                trabaja=  float(fila [25])
            else: 
                trabaja=  float(fila [26])
            return random<trabaja

def esNacidoEnElExtranjero(canton, r=-1):
    random = randint(1,100) if r==-1 else r
    for fila in matrizIndicadores:
        cantonCsv = fila[0]
        annoCsv = fila [1]
        if (cantonCsv == canton and annoCsv == "2011" ): 
            nacidoExtranjero = float(fila [28])
            return random<nacidoExtranjero


