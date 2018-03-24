import csv
from random import randint

matrizActas = []
matrizJrv = []   #<provincia>,<cantón>,<distrito>,<barrio>,<#junta>,<electores>
matrizIndicadores = []

def leercsv(nombreArchivo, nombreMatriz):	
    archivo = open(nombreArchivo, "rU")
    lector = csv.reader(archivo, delimiter=",")
    indice = 0	
    for fila in lector:
        nombreMatriz.append (fila)
        #print(fila)
        indice += 1
    archivo.close()

#funciones #1
#obtiene provincia del votante ---------------------------------------------
    
def cantidadVotantesSegunProvincia(provincia):
    votantes = 0
    for i in range(len(matrizJrv)):
        if ( len(matrizJrv[i])!=0 and matrizJrv[i][0]==provincia ):
            #print(matrizJrv[i][0],matrizJrv[i][5])
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
    costaRica = sanJose + alajuela + cartago + heredia + guanacaste + puntarenas + limon
    print(sanJose)
    print(alajuela)
    print(cartago)
    print(heredia)
    print(guanacaste)
    print(puntarenas)
    print(limon)
    print("Votantes en Costa Ria: " + str(costaRica))
    print("% votantes en San Jose: "  + str(obtienePorcentaje(sanJose,costaRica)))
    print("% votantes en Alajuela: "  + str(obtienePorcentaje(alajuela,costaRica)))
    print("% votantes en Cartago: " + str(obtienePorcentaje(cartago,costaRica)))
    print("% votantes en Heredia: " + str(obtienePorcentaje(heredia,costaRica)))
    print("% votantes en Guanacaste: " + str(obtienePorcentaje(guanacaste,costaRica)))
    print("% votantes en Puntarenas: " + str(obtienePorcentaje(puntarenas,costaRica)))
    print("% votantes en Limon: " + str(obtienePorcentaje(limon,costaRica)))
    print(random)
    
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
    print("El % de poblacion urbana en el canton es " + porcentajePoblacionUrb)            
    return float(porcentajePoblacionUrb)
    

def viveZonaUrbana(canton):
    densidadPoblacionUrbana = obtienePorcPoblacionUrbana(canton)
    random = randint(1,100)
    print(random)
    if (random<densidadPoblacionUrbana):
        return True
    else:
        return False
#funciones #3
#------obtiene si vive en hacinamiento

def porcentajeHacinamiento(canton):
    porcentajeHacinamiento = ""
    for i in range(len(matrizIndicadores)):
        if (len(matrizIndicadores[i])!= 0 and matrizIndicadores[i][0]==canton and matrizIndicadores[i][1]=="2011"):
            porcentajeHacinamiento = matrizIndicadores[i][11]
    print("El % de hacinamiento es " + porcentajeHacinamiento)            
    return float(porcentajeHacinamiento)

def viveHacinamiento(canton):
    hacinamientoCanton = porcentajeHacinamiento(canton)
    random = randint(1,100)
    print(random)
    if(random<hacinamientoCanton):
        return True
    else:
        return False
#funciones #4   
#-------- obtiene si esta dentro de la tasa neta de participacion economica

def porcentajeParticipacionNeta(canton):
    porc_neto = ""
    for i in range(len(matrizIndicadores)):
        if (len(matrizIndicadores[i])!= 0 and matrizIndicadores[i][0]==canton and matrizIndicadores[i][1]=="2011"):
            porc_neto = matrizIndicadores[i][24]
    print("El % participacion neta es: " + porc_neto)            
    return float(porc_neto)

def estaDentroParticipacionEconomica(canton):
    porc_participacionNeta = porcentajeParticipacionNeta(canton)
    random = randint(1,100)
    print(random)
    if(random<porc_participacionNeta):
        return True
    else:
        return False
    
    
#funciones #5
#---------obtiene si votante tiene discapacidad

def porcentajeDiscapacitados(canton):
    porc_discapacitados = ""
    for i in range(len(matrizIndicadores)):
        if (len(matrizIndicadores[i])!= 0 and matrizIndicadores[i][0]==canton and matrizIndicadores[i][1]=="2011"):
            porc_discapacitados = matrizIndicadores[i][30]
    print("El % de discapacitados es: " + porc_discapacitados)            
    return float(porc_discapacitados)

def esDiscapacitado(canton):
    porc_discapacitados = porcentajeDiscapacitados(canton)
    random = randint(1,100)
    print(random)
    if(random<porc_discapacitados):
        return True
    else:
        return False

#funciones #5
#---------obtiene si votante vive en hogar con jefatura compartida

def porcHogarJefaturaCompartida(canton):
    porc_jefaturaComp = ""
    for i in range(len(matrizIndicadores)):
        if (len(matrizIndicadores[i])!= 0 and matrizIndicadores[i][0]==canton and matrizIndicadores[i][1]=="2011"):
            porc_jefaturaComp = matrizIndicadores[i][32]
    print("El % de hogar con jefatura compartida es: " + porc_jefaturaComp)            
    return float(porc_jefaturaComp)

def viveHogarJefaturaCompartida(canton):
    porc_jefaturaComp = porcHogarJefaturaCompartida(canton)
    random = randint(1,100)
    print(random)
    if(random<porc_jefaturaComp):
        return True
    else:
        return False

    
leercsv("actas.csv", matrizActas)
leercsv("jrv.csv", matrizJrv)
leercsv("indicadores.csv", matrizIndicadores)
#print(provinciaSegunVotante())
print(viveZonaUrbana("Barva"))
print(viveHacinamiento("Barva"))
print(esDiscapacitado("Desamparados"))
print(estaDentroParticipacionEconomica("Barva"))
print(viveHogarJefaturaCompartida("Dota"))


    



