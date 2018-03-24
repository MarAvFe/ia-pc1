import csv
from random import randint
import unicodedata
from random import uniform
from unicodedata import normalize
matrizActas = []
matrizJrv = []
matrizIndicadores = []



'''Marcello'''
def esHombre():
    return (uniform(0, 1) * 100) < 49


'''Stefi'''

def normalize_text ( text ):
  return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').upper()

  
def leercsv(nombreArchivo, nombreMatriz):	
	archivo = open(nombreArchivo, "rU")
	lector = csv.reader(archivo, delimiter=",")
	for fila in lector:
		filaTmp=[]
		for atributo in fila:
			atributoTmp= normalize_text(atributo)
			filaTmp.append(atributoTmp.decode('UTF-8'))
		nombreMatriz.append (filaTmp)
	archivo.close()


def cargarCsvMemoria():
	leercsv("actas.csv", matrizActas)
	leercsv("indicadores.csv", matrizIndicadores )
	leercsv("jrv.csv", matrizJrv)	


def getDensidad(canton):
	for fila in matrizIndicadores:
		cantonCsv = fila[0]
		annoCsv = fila [1]
		densidad = fila [4]
		if (cantonCsv == canton and annoCsv == "2011" ): 
			densidad = fila[4] 
			return densidad


def esDependiente(canton):
	random = randint(1,100)
	for fila in matrizIndicadores:
		cantonCsv = fila[0]
		annoCsv = fila [1]
		if (cantonCsv == canton and annoCsv == "2011" ): 
			dependencia = float(fila [7])
			if (random>dependencia):
				return False
			else:
				return True


def esBuenoEstadoDeVivienda(canton):
	random = randint(1,100)
	for fila in matrizIndicadores:
		cantonCsv = fila[0]
		annoCsv = fila [1]
		if (cantonCsv == canton and annoCsv == "2011" ): 
			estadoVivienda = float(fila [10])
			if (random<estadoVivienda):
				return True
			else:
				return False

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


def tieneTrabajo(canton, genero):
	random = randint(1,100)
	for fila in matrizIndicadores:
		cantonCsv = fila[0]
		annoCsv = fila [1]
		if (cantonCsv == canton and annoCsv == "2011" ): 
			if (genero==True):
				trabaja=  float(fila [25])
			else: 
				trabaja=  float(fila [26])
			if (random<trabaja):
				return True
			else:
				return False

def esNacidoEnElExtranjero(canton):
	random = randint(1,100)
	for fila in matrizIndicadores:
		cantonCsv = fila[0]
		annoCsv = fila [1]
		if (cantonCsv == canton and annoCsv == "2011" ): 
			nacidoExtranjero = float(fila [28])
			if (random<nacidoExtranjero):
				return True
			else:
				return False

cargarCsvMemoria()
