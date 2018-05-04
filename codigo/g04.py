'''
*****************************************
*  + Proyecto #1
*  + Autores: 
*		Marcello Ávila Feoli
*		Stefi Falcón Chávez
*		Nelson Gómez Alvarado
*****************************************
'''
import argparse
from simuladorDeVotantes import *
#from red_neuronal import *
#from arboles_decision import *
#from KKN import *
#from regresion_logistica import *
def getArgumentos():
	parser = argparse.ArgumentParser()
	#General
	parser.add_argument('--prefijo', nargs = 1, type = str) #archivos # --prefijo <nombre_del_archivo>
	parser.add_argument('--provincia', nargs = 1, type = str)
	parser.add_argument('--poblacion', nargs = 1, type = int, default = 500) # --poblacion <numero>
	parser.add_argument('--porcentaje-pruebas', nargs = 1, type = int, default = 0.1) # --porcentaje-pruebas <porcentaje>
	#Regresión Logística
	parser.add_argument('--regresion-logistica', action = 'store_true')
	parser.add_argument('--l1', action = 'store_true')
	parser.add_argument('--l2', action = 'store_true')
	#Redes Neuronales
	parser.add_argument('--red-neuronal', action = 'store_true')
	parser.add_argument('--numero-capas', nargs = 1, type = int)
	parser.add_argument('--unidades-por-capa', nargs = 1, type = int)
	parser.add_argument('--funcion-activacion', nargs = 1, type = str)
	#Árboles de Decisión
	parser.add_argument('--arbol', action = 'store_true')
	parser.add_argument('--umbral-poda', nargs=1, type=float, default=10)
	#KNN
	parser.add_argument('--knn', action='store_true')
	parser.add_argument('--k', nargs=1, type=int, default=5)
	return parser.parse_args()


def main():
	argumentos = getArgumentos()
	if argumentos.arbol:
		print("árbol")
		#guardarResultados(argumentos.umbral-poda)
	elif argumentos.red-neuronal:
		print("red neuronal")
	elif argumentos.regresion.logistica:
		print("árbol")
	elif argumentos.knn:
		print("knn")

if __name__ == '__main__':
	main()