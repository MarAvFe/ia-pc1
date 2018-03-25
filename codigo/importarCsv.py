import csv

matrizActas = []
matrizJrv = []
matrizIndicadores = []

def leercsv(nombreArchivo, nombreMatriz):	
    archivo = open(nombreArchivo, "rU")
    lector = csv.reader(archivo, delimiter = ",")
    indice = 0	
    for fila in lector:
        nombreMatriz.append (fila)
        indice += 1
    archivo.close()


leercsv("../resources/actas.csv", matrizActas)
leercsv("../resources/indicadores.csv", matrizJrv)
leercsv("../resources/jrv.csv", matrizIndicadores)

