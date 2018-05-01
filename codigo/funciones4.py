"""Modulo de generacion de muestras de votantes

Este modulo genera tiene 2 funciones principales
1. generar_muestra_pais(n)
2. generar_muestra_provincia(n,provincia)

Donde cada una, genera una cantidad n de votantes
con atributos aleatorios que siguen la distribucion
de los datos de las actas de escrutinio, sensos del 2011
y los mapeos de las juntas

Autores: Marcello Avila Feoli
         Steffi Falcon Chaves
         Nelson Gomez Alvarado
"""

import time
import csv
import unicodedata

from bisect import bisect_left
from datetime import datetime
from random import uniform
from random import randint
from random import uniform
from unicodedata import normalize
from pprint import pprint

INDICES = []
VOTXCANTON = []
VOTXCANTONSEGUNDA = []
matrizActas1 = []
matrizActas2 = []
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
        nombreMatriz.append(filaTmp)
    archivo.close()

def obtenerVotantesCanton(canton, provincia):
    total = 0
    for i in matrizJrv:
        if (i[0] == provincia) & (i[1] == canton):
            total += int(i[5])
    return total

def esHombre():
    return (uniform(0, 1) * 100) < 49


# Indicadores

def obtenerPromedioAlfabetismo(canton, edad):
    for i in matrizIndicadores:
        if i[0] == canton:
            if edad < 25:
                return float(i[13])
            return float(i[14])
    return -1

def estaDesempleado(canton, r=-1):
    aleatorio = uniform(0, 1) if r==-1 else r
    for i in matrizIndicadores:
        if i[0] == canton:
            return (aleatorio*100) < float(i[23])
    return -1

def estaAsegurado(canton,r=-1):
    aleatorio = uniform(0, 1) if r==-1 else r
    for i in matrizIndicadores:
        if i[0] == canton:
            return (aleatorio*100) < float(i[27])
    return -1

def obtenerEdad(canton,esHombre):
    ages = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
    sexo = "HOMBRES" if esHombre else "MUJERES"
    for i in matrizPiramide:
        if (i[0] == canton) & (i[1] == sexo):
            rangos = i[6:]
            total = sum(float(n) for n in rangos)
            ageSeed = uniform(0, total)
            ageIndex = -1
            for j, k in enumerate(rangos):
                if ageSeed <= sum(float(n) for n in rangos[:j]):
                    ageIndex = j
                    break
            age = ages[ageIndex]
            return age + int(uniform(0, 4))
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
                cantones.append([cant, int(i[-1])])
        else:
            cantones[-1][1] += int(i[-1])
    return cantones

def obtenerCantonAleatorio(provincia = ""):
    cantonesPoblacion = obtenerCantonesPoblacion(provincia)
    total = sum(i[1] for i in cantonesPoblacion)
    cantonSeed = uniform(0,total)
    cantonIndex = -1
    for j, k in enumerate(cantonesPoblacion):
        if cantonSeed <= sum(float(n[1]) for n in cantonesPoblacion[:j]):
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
            return int(densidad)
    return -1

def esDependiente(canton, r=-1):
    random = randint(1, 100) if r==-1 else r
    for fila in matrizIndicadores:
        cantonCsv = fila[0]
        annoCsv = fila [1]
        if (cantonCsv == canton and annoCsv == "2011" ):
            dependencia = float(fila [7])
            return random > dependencia
    return -1

def esBuenoEstadoDeVivienda(canton, r=-1):
    random = randint(1, 100) if r==-1 else r
    for fila in matrizIndicadores:
        cantonCsv = fila[0]
        annoCsv = fila [1]
        if (cantonCsv == canton and annoCsv == "2011" ):
            estadoVivienda = float(fila [10])
            return random<estadoVivienda
    return -1

def annosAprobadosEducacionRegular(canton, edad):
    for fila in matrizIndicadores:
        cantonCsv = fila[0]
        annoCsv = fila [1]
        if (cantonCsv == canton and annoCsv == "2011" ):
            if (edad <=49):
                return float(fila[16])
            else:
                return float(fila[17])
    return -1

def porcentajeAsistenciaEducacionRegular(canton, edad):
    for fila in matrizIndicadores:
        cantonCsv = fila[0]
        annoCsv = fila [1]
        if (cantonCsv == canton and annoCsv == "2011" ):
            if (edad<=24):
                return float(fila[21])
            else:
                return float(fila[22])
    return -1

def tieneTrabajo(canton,genero, r=-1):
    random = randint(1,100) if r==-1 else r
    for fila in matrizIndicadores:
        cantonCsv = fila[0]
        annoCsv = fila [1]
        if (cantonCsv == canton and annoCsv == "2011" ):
            if (genero == True):
                trabaja=  float(fila [25])
            else:
                trabaja=  float(fila [26])
            return random < trabaja
    return -1

def esNacidoEnElExtranjero(canton, r=-1):
    random = randint(1,100) if r == -1 else r
    for fila in matrizIndicadores:
        cantonCsv = fila[0]
        annoCsv = fila [1]
        if (cantonCsv == canton and annoCsv == "2011" ):
            nacidoExtranjero = float(fila [28])
            return random < nacidoExtranjero
    return -1

def cantidadVotantesSegunProvincia(provincia):
    votantes = 0
    for i in range(len(matrizJrv)):
        if ( len(matrizJrv[i]) != 0
                 and matrizJrv[i][0] == provincia ):
            votantes = votantes + int(matrizJrv[i][5])
    return votantes

def obtienePorcentaje(x, total):
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
    costaRica = sanJose + alajuela + cartago + heredia + guanacaste + puntarenas + limon
    if(random <= 32):
        return "San Jose"
    elif(random > 32 and random <= 51):
        return "Alajuela"
    elif(random > 51 and random <= 63):
        return "Cartago"
    elif(random > 63 and random <= 80):
        return "Heredia"
    elif(random > 80 and random <= 84):
        return "Guanacaste"
    elif(random > 84 and random <= 89):
        return "Puntarenas"
    elif(random > 89 and random <= 100):
        return "Limon"

def viveZonaUrbana(canton):
    densidadPoblacionUrbana = ""
    for i in range(len(matrizIndicadores)):
        if ((matrizIndicadores[i][0] == canton)
                and (matrizIndicadores[i][1] == "2011")):
            densidadPoblacionUrbana = matrizIndicadores[i][5]
    random = randint(1,100)
    if random < float(densidadPoblacionUrbana):
        return True
    else:
        return False

def viveHacinamiento(canton, r=-1):
    hacinamientoCanton = ""
    random = randint(1,100)
    for i in range(len(matrizIndicadores)):
        if (len(matrizIndicadores[i])!= 0
                and matrizIndicadores[i][0] == canton
                and matrizIndicadores[i][1] == "2011"):
            hacinamientoCanton = matrizIndicadores[i][11]
            if random<float(hacinamientoCanton):
                return True
            else:
                return False
    return False

def estaDentroParticipacionEconomica(canton, r=-1):
    porc_participacionNeta = ""
    random = randint(1,100)
    for i in range(len(matrizIndicadores)):
        if (len(matrizIndicadores[i])!= 0
                and matrizIndicadores[i][0] == canton
                and matrizIndicadores[i][1] == "2011"):
            porc_participacionNeta = matrizIndicadores[i][24]
            if random<float(porc_participacionNeta):
                return True
            else:
                return False
    return False

def esDiscapacitado(canton,
                    r=-1):
    random = randint(1, 100)
    porc_discapacitados = ""
    for i in range(len(matrizIndicadores)):
        if (len(matrizIndicadores[i])!= 0
                and matrizIndicadores[i][0] == canton
                and matrizIndicadores[i][1] == "2011"):
            porc_discapacitados = matrizIndicadores[i][30]
            if random<float(porc_discapacitados):
                return True
            else:
                return False
    return False

def viveHogarJefaturaCompartida(canton,
                                r=-1):
    porc_jefaturaComp = ""
    random = randint(1,100)
    for i in range(len(matrizIndicadores)):
        if (len(matrizIndicadores[i])!= 0
                and matrizIndicadores[i][0] == canton
                and matrizIndicadores[i][1] == "2011"):
            porc_jefaturaComp = matrizIndicadores[i][32]
            if random<float(porc_jefaturaComp):
                return True
            else:
                return False
    return False

def obtenerPromedioDeOcupantes(canton):
    for i in matrizIndicadores:
        if i[0] == canton:
            return float(i[9])
    return -1

def timeNow():
    #print(int(round(time.time() * 1000)))
    pass

def obtenerVotante(provincia=""):
    votante = []
    canton = obtenerCantonAleatorio(provincia)
    timeNow()
    sexo = esHombre()
    timeNow()
    edad = obtenerEdad(canton, sexo)
    timeNow()
    votante.append(obtenerVotoPorPartido(canton))
    votante.append(obtenerVotoPorPartidoSegunda(canton))
    votante.append(canton)
    votante.append(sexo)
    votante.append(edad)
    # Todos los indicadores
    #Demograficos
    timeNow()
    votante.append(getDensidad(canton))
    #votante.append(viveZonaUrbana(canton))
    timeNow()
    votante.append(esDependiente(canton))
    #vivienda
    timeNow()
    votante.append(obtenerPromedioDeOcupantes(canton))
    timeNow()
    votante.append(esBuenoEstadoDeVivienda(canton))
    timeNow()
    votante.append(viveHacinamiento(canton))
    #Educativos
    timeNow()
    votante.append(obtenerPromedioAlfabetismo(canton, edad))
    timeNow()
    votante.append(annosAprobadosEducacionRegular(canton, edad))
    timeNow()
    votante.append(porcentajeAsistenciaEducacionRegular(canton, edad))
    #Economicos
    timeNow()
    votante.append(estaDesempleado(canton))
    timeNow()
    votante.append(estaDentroParticipacionEconomica(canton))
    timeNow()
    votante.append(estaAsegurado(canton))
    #Sociales
    timeNow()
    votante.append(esNacidoEnElExtranjero(canton))
    timeNow()
    votante.append(esDiscapacitado(canton))
    timeNow()
    votante.append(viveHogarJefaturaCompartida(canton))
    return votante


# API ----------
def generar_muestra_pais(n):
    print("COSTA RICA")
    muestra = []
    for i in range(n):
        muestra.append(obtenerVotante())
    return muestra

def generar_muestra_provincia(n, provincia):
    print(provincia)
    muestra = []
    for i in range(n):
        muestra.append(obtenerVotante(provincia))
    return muestra

def obtenerJuntasXCanton():
    #retorna los numeros de junta de cada canton
    retorno = []
    ultimoCanton = ""
    for i in matrizJrv:
        if i[1] != ultimoCanton:
            ultimoCanton = i[1]
            retorno.append([i[1], []])
        else:
            retorno[-1][1].append(i[4])
    return retorno

def obtenerJuntasIndices():
    global INDICES
    if INDICES != []:
        return INDICES
    # Obtiene los índices de cambio de cantón en la lista de juntas
    retorno = []
    ultimoCanton = ""
    for k, i in enumerate(matrizJrv):
        if i[1] != ultimoCanton:
            ultimoCanton = i[1]
            retorno.append([i[1], k])
    INDICES = retorno + [["NONE", -1]]
    return INDICES

def obtenerVotosPorCanton(primeraRonda=True):
    if(primeraRonda):
        global VOTXCANTON
        if VOTXCANTON != []:
            return VOTXCANTON
        totalPartidos = 14 # 1ra ronda
        matrizActas = matrizActas1
    else:
        global VOTXCANTONSEGUNDA
        if VOTXCANTONSEGUNDA != []:
            return VOTXCANTONSEGUNDA
        totalPartidos = 3  # 2da ronda
        matrizActas = matrizActas2
    cantonVotos = []
    indices = obtenerJuntasIndices()
    ultimoCanton = 0

    for j, acta in enumerate(matrizActas):
        if j == indices[ultimoCanton][1]:
            cantonVotos.append([indices[ultimoCanton][0], (acta[1:totalPartidos]+acta[totalPartidos+1:totalPartidos+3])])
            ultimoCanton += 1
            continue
        cantonVotos[-1][1] = [int(x)+int(y) for x,y in zip(cantonVotos[-1][1], (acta[1:totalPartidos]+acta[totalPartidos+1:totalPartidos+3]))]
    if(primeraRonda):
        VOTXCANTON = cantonVotos
        return VOTXCANTON
    VOTXCANTONSEGUNDA = cantonVotos
    return VOTXCANTONSEGUNDA


def obtenerVotos(canton, lista):
    for i in lista:
        if i[0] == canton:
            return i[1]
    return []

def obtenerVotoPorPartido(canton):
    # Elije aleatoriamente pero con cierta densidad, el voto de un elector
    partidos = [
        "ACCESIBILIDAD SIN EXCLUSION",
        "ACCION CIUDADANA",
        "ALIANZA DEMOCRATA CRISTIANA",
        "DE LOS TRABAJADORES",
        "FRENTE AMPLIO",
        "INTEGRACION NACIONAL",
        "LIBERACION NACIONAL",
        "MOVIMIENTO LIBERTARIO",
        "NUEVA GENERACION",
        "RENOVACION COSTARRICENSE",
        "REPUBLICANO SOCIAL CRISTIANO",
        "RESTAURACION NACIONAL",
        "UNIDAD SOCIAL CRISTIANA",
        "NULO",
        "BLANCO"
    ]
    # Lista de pesos con los votos del cantón por cada partido
    votosDelCanton = obtenerVotos(canton, obtenerVotosPorCanton())
    # Total de votos del cantón
    total = sum(int(n) for n in votosDelCanton)
    # Número aleatorio dentro del total de votos
    seed = uniform(0, total)
    indVoto = -1
    for j, k in enumerate(votosDelCanton):
        # Sumar los votos y ver si superan el valor aleatorio.
        # Una vez que lo superan, se ha alcanzado un step que define el
        #  rango en que se determina el voto.
        if seed <= sum(float(n) for n in votosDelCanton[:j+1]):
            indVoto = j
            break
    voto = partidos[indVoto]
    return voto

def obtenerVotoPorPartidoSegunda(canton):
    # Elije aleatoriamente pero con cierta densidad, el voto de un elector
    partidos = [
        "ACCION CIUDADANA",
        "RESTAURACION NACIONAL",
        "NULO",
        "BLANCO"
    ]
    # Lista de pesos con los votos del cantón por cada partido
    votosDelCanton = obtenerVotos(canton, obtenerVotosPorCanton(False))
    # Total de votos del cantón
    total = sum(int(n) for n in votosDelCanton)
    # Número aleatorio dentro del total de votos
    seed = uniform(0, total)
    indVoto = -1
    for j, k in enumerate(votosDelCanton):
        # Sumar los votos y ver si superan el valor aleatorio.
        # Una vez que lo superan, se ha alcanzado un step que define el
        #  rango en que se determina el voto.
        if seed <= sum(float(n) for n in votosDelCanton[:j+1]):
            indVoto = j
            break
    voto = partidos[indVoto]
    return voto

def contarDiferentes(lista):
    # Cuenta los valores diferentes de una lista y su
    #  cantidad de ocurrencias
    retorno = [[],[]]
    for e in lista:
        if e in retorno[0]:
            k = retorno[0].index(e)
            retorno[1][k] += 1
        else:
            retorno[0].append(e)
            retorno[1].append(1)
    return retorno


#----------------------
def analisis(muestra):
    n = len(muestra)

    partidos = []
    partidosSegunda = []
    cantones = []
    sexos = []
    edades = []
    for v in muestra:
        partidos.append(v[0])
        partidosSegunda.append(v[1])
        cantones.append(v[2])
        sexos.append(v[3])
        edades.append(v[4])
    print("Cantidad de votantes: " + str(len(partidos)))

    #partidos
    # ------------------
    print("Partidos predominantes 1ra ronda")
    partidosDiferentes = contarDiferentes(partidos)
    totalPartidos = len(partidos)
    porcentPartidos = [obtienePorcentaje(x, totalPartidos) for x in partidosDiferentes[1]]
    porcentPartidos, partidosDiferentes[0] = (list(x) for x in zip(*sorted(zip(porcentPartidos,
                                                                               partidosDiferentes[0]),
                                                                               key=lambda pair: pair[0])))
    assert len(porcentPartidos) == len(partidosDiferentes[0])
    for i in range((len(porcentPartidos)-3), len(porcentPartidos)):
        print("  " + str(round(porcentPartidos[i], 2)) + "%\t" + str(partidosDiferentes[0][i]))

    # ------------------
    print("Resultados 2da ronda")
    partidosDiferentes2 = contarDiferentes(partidosSegunda)
    totalPartidos2 = len(partidosSegunda)
    porcentPartidos2 = [obtienePorcentaje(x, totalPartidos2) for x in partidosDiferentes2[1]]
    porcentPartidos, partidosDiferentes[0] = (list(x) for x in zip(*sorted(zip(porcentPartidos2,
                                                                               partidosDiferentes2[0]),
                                                                               key=lambda pair: pair[0])))
    assert len(porcentPartidos2) == len(partidosDiferentes2[0])
    for i in range((len(porcentPartidos2))):
        print("  " + str(round(porcentPartidos2[i], 2)) + "%\t" + str(partidosDiferentes2[0][i]))


    #sexos
    totalHombres = sum(1 if (n) else 0 for n in sexos)
    print("Razón de sexos")
    print("  " + str(round(obtienePorcentaje(totalHombres, n), 2)) + "%\tHombres")
    print("  " + str(round(obtienePorcentaje(n-totalHombres, n), 2)) + "%\tMujeres")

    #edades
    print("Promedio de edad: " + str(round(sum(edades)/n)) + " años")
    print("")


# Carga de datos
leerCsv("../resources/actas1.csv", matrizActas1)
leerCsv("../resources/actas2.csv", matrizActas2)
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

ff = map(lambda x: analisis(generar_muestra_provincia(500, x)), provincias)
set(ff)

muestra_pais = generar_muestra_pais(1000)
analisis(muestra_pais)
print(muestra_pais[-10:-1])
