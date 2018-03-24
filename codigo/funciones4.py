from datetime import datetime
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
provincias = [
    "CARTAGO",
    "SAN JOSE",
    "ALAJUELA",
    "PUNTARENAS",
    "GUANACASTE",
    "HEREDIA",
    "LIMON"
    ]

# API

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


# Auxiliares
def normalize_text ( text ):
    return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').upper()

def leerCsv(nombreArchivo, nombreMatriz):   
    archivo = open(nombreArchivo, "rU")
    lector = csv.reader(archivo, delimiter=",")
    for fila in lector:
        filaTmp = []
        for atributo in fila:
            atributoTmp = normalize_text(atributo)
            filaTmp.append(atributoTmp.decode('UTF-8'))
        nombreMatriz.append (filaTmp)
    archivo.close()


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

# Indicadores
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
    sexo = "HOMBRES" if esHombre else "MUJERES"
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
            return age + int(uniform(0,4))
    return -1


def obtenerCantonesPoblacion(provincia=""): 
    cantones = []
    ultimoCanton = ""
    for i in matrizJrv:
        if (provincia != "") & (provincia != i[0]):
            continue
        if i[1] != ultimoCanton:
            ultimoCanton = i[1]
            cant = i[1]
            if cant == "central":
                cant = i[0]
            if cant not in cantones:
                cantones.append([cant,int(i[-1])])
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


def obtenerCantonesTodos():
    return sum(list(obtenerCantones(y) for y in provincias), [])


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
                return fila[16]
            else:
                return fila[17]


def porcentajeAsistenciaEducacionRegular(canton, edad):
    for fila in matrizIndicadores:
        cantonCsv = fila[0]
        annoCsv = fila [1]
        if (cantonCsv == canton and annoCsv == "2011" ): 
            if (edad<=24):
                return fila[21]
            else: 
                return fila[22]


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

#funciones #1
#obtiene provincia del votante ---------------------------------------------
    
def cantidadVotantesSegunProvincia(provincia):
    votantes = 0
    for i in range(len(matrizJrv)):
        if ( len(matrizJrv[i])!=0 and matrizJrv[i][0]==provincia ):
            votantes = votantes + int(matrizJrv[i][5])
    return votantes

def obtienePorcentaje(x,total):
    return (x*100)/total
    
def provinciaSegunVotante():
    random = randint(1,100)
    sanJose =  cantidadVotantesSegunProvincia("SAN JOSE")
    alajuela =  cantidadVotantesSegunProvincia("ALAJUELA")
    cartago = cantidadVotantesSegunProvincia("CARTAGO")
    heredia =  cantidadVotantesSegunProvincia("HEREDIA")
    guanacaste =  cantidadVotantesSegunProvincia("GUANACASTE")
    puntarenas = cantidadVotantesSegunProvincia("PUNTARENAS")
    limon = cantidadVotantesSegunProvincia("LIMON")
    costaRica = sanJose + alajuela + cartago + heredia + guanacaste + puntarenas + limo    
    if(random<=32):
        return "San Jose"
    elif(random>32 and random<=51):
        return "Alajuela"
    elif(random>51 and random<=63):
        return "Cartago"
    elif(random>63 and random<=80):
        return "Heredia"
    elif(random>80 and random<=84):
        return "Guanacaste"
    elif(random>84 and random<=89):
        return "Puntarenas"
    elif(random>89 and random<=100):
        return "Limon"

#funciones #2
#----- obtiene si votante pertenece a zona urbana o no

def obtienePorcPoblacionUrbana(canton):
    porcentajePoblacionUrb = ""
    for i in range(len(matrizIndicadores)):
        if (len(matrizIndicadores[i])!= 0 and matrizIndicadores[i][0]==canton and matrizIndicadores[i][1]=="2011"):
            porcentajePoblacionUrb = matrizIndicadores[i][5]        
    return float(porcentajePoblacionUrb)
    

def viveZonaUrbana(canton, r=-1):
    densidadPoblacionUrbana = obtienePorcPoblacionUrbana(canton)
    random = randint(1,100) if r==-1 else r
    return random<densidadPoblacionUrbana
#funciones #3
#------obtiene si vive en hacinamiento

def porcentajeHacinamiento(canton):
    porcentajeHacinamiento = ""
    for i in range(len(matrizIndicadores)):
        if (len(matrizIndicadores[i])!= 0 and matrizIndicadores[i][0]==canton and matrizIndicadores[i][1]=="2011"):
            porcentajeHacinamiento = matrizIndicadores[i][11]   
    return float(porcentajeHacinamiento)

def viveHacinamiento(canton, r=-1):
    hacinamientoCanton = porcentajeHacinamiento(canton)
    random = randint(1,100) if r==-1 else r
    return random<hacinamientoCanton

#funciones #4   
#-------- obtiene si esta dentro de la tasa neta de participacion economica

def porcentajeParticipacionNeta(canton):
    porc_neto = ""
    for i in range(len(matrizIndicadores)):
        if (len(matrizIndicadores[i])!= 0 and matrizIndicadores[i][0]==canton and matrizIndicadores[i][1]=="2011"):
            porc_neto = matrizIndicadores[i][24]        
    return float(porc_neto)

def estaDentroParticipacionEconomica(canton, r=-1):
    porc_participacionNeta = porcentajeParticipacionNeta(canton)
    random = randint(1,100) if r==-1 else r
    return random<porc_participacionNeta
    
    
#funciones #5
#---------obtiene si votante tiene discapacidad

def porcentajeDiscapacitados(canton):
    porc_discapacitados = ""
    for i in range(len(matrizIndicadores)):
        if (len(matrizIndicadores[i])!= 0 and matrizIndicadores[i][0]==canton and matrizIndicadores[i][1]=="2011"):
            porc_discapacitados = matrizIndicadores[i][30]         
    return float(porc_discapacitados)

def esDiscapacitado(canton, r=-1):
    porc_discapacitados = porcentajeDiscapacitados(canton)
    random = randint(1,100) if r==-1 else r
    return random<porc_discapacitados

#funciones #5
#---------obtiene si votante vive en hogar con jefatura compartida

def porcHogarJefaturaCompartida(canton):
    porc_jefaturaComp = ""
    for i in range(len(matrizIndicadores)):
        if (len(matrizIndicadores[i])!= 0 and matrizIndicadores[i][0]==canton and matrizIndicadores[i][1]=="2011"):
            porc_jefaturaComp = matrizIndicadores[i][32]
    return float(porc_jefaturaComp)

def viveHogarJefaturaCompartida(canton, r=-1):
    porc_jefaturaComp = porcHogarJefaturaCompartida(canton)
    random = randint(1,100) if r==-1 else r
    return random<porc_jefaturaComp


# Carga de datos
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


# Ejecución

# print(len(obtenerCantonesTodos()))
# print("esHombre: "+str(esHombre()))
# print("obtenerVotantesCanton: "+str(obtenerVotantesCanton("ESCAZU", "SAN JOSE")))
# print("obtenerPromedioDeOcupantes: "+str(obtenerPromedioDeOcupantes("MORAVIA")))
# print("obtenerPromedioAlfabetismo: "+str(obtenerPromedioAlfabetismo("MORAVIA", 20)))
# print("estaDesempleado: "+str(estaDesempleado("MORAVIA")))
# print("estaAsegurado: "+str(estaAsegurado("MORAVIA")))
# print("obtenerEdad: "+str(obtenerEdad("MORAVIA", esHombre())))
# print(len(obtenerCantonesPoblacion()))
# print(obtenerCantonAleatorio())
# print(obtenerCantonAleatorio("CARTAGO"))

print(datetime.now().time())
obtener_muestra_pais(500)
print(datetime.now().time())
