from funcion4 import *


def test_obtenerVotantesCanton():
	funcion = obtenerVotantesCanton("NARANJO", "ALAJUELA")
	assert funcion == 31782

def test_obtenerPromedioDeOcupantes():
	funcion = obtenerPromedioDeOcupantes("POAS")
	assert funcion == '3.69'

def test_obtenerPromedioAlfabetismo():	
	funcion = obtenerPromedioAlfabetismo("BARVA", 20)
	assert funcion == '99.5'

def test_estaDesempleado():
	funcion = estaDesempleado ("SAN JOSE", 0)
	assert funcion == True

def test_estaDesempleado_false():
	funcion = estaDesempleado ("SAN JOSE", 1)
	assert funcion == False

def test_estaAsegurado():
	funcion = estaAsegurado("CARTAGO", 0)
	assert funcion == True

def test_estaAsegurado_falso():
	funcion = estaAsegurado("CARTAGO", 1)
	assert funcion == False

def test_esDependiente_cartago_falso():
	funcion = esDependiente("CARTAGO", 18)
	assert funcion == False

def test_esDependiente_cartago_verdadero():
	funcion = esDependiente("CARTAGO", 99)
	assert funcion == True

def test_esDependiente_Heredia_F():
	funcion = esDependiente("HEREDIA", 30)
	assert funcion == False

def test_esDependiente_Puntaarenas_F():
	funcion = esDependiente("PUNTARENAS", 40)
	assert funcion == False

def test_esBuenoEstadoDeVivienda_limon_f():
	funcion = esBuenoEstadoDeVivienda("LIMON",99)
	assert funcion == False

def test_esBuenoEstadoDeVivienda_limon_verdadero():
	funcion = esBuenoEstadoDeVivienda("LIMON", 5)
	assert funcion == True

def test_esBuenoEstadoDeVivienda_guanacaste_verdadero():
	funcion = esBuenoEstadoDeVivienda("LIBERIA", 5)
	assert funcion == True

def test_annosAprobadosEducacionRegular():
	funcion = annosAprobadosEducacionRegular("SAN RAMON", 55)
	assert funcion == "6.9"

def test_porcentajeAsistenciaEducacionRegular():
	funcion = porcentajeAsistenciaEducacionRegular("LIBERIA", 33)
	assert funcion == "8.5"

def test_tieneTrabajo():
	funcion = tieneTrabajo ("CORREDORES", True, 55)
	assert funcion == True

def test_esNacidoEnElExtranjero_verdadero ():
	funcion = esNacidoEnElExtranjero("POCOCI", 6)
	assert funcion == True

def test_esNacidoEnElExtranjero_falso ():
	funcion = esNacidoEnElExtranjero("POCOCI", 15)
	assert funcion == False

def test_cantidadVotantesSegunProvincia():
	funcion = cantidadVotantesSegunProvincia("CARTAGO")
	assert funcion == 387905

def test_obtienePorcPoblacionUrbana():
	funcion = obtienePorcPoblacionUrbana("FLORES")
	assert funcion == 100.0

def test_viveZonaUrbana():
	funcion = viveZonaUrbana("SARAPIQUI", 15)
	assert funcion == True

def test_porcentajeHacinamiento():
	funcion = porcentajeHacinamiento("GRECIA")
	assert funcion == 3.2

def test_viveHacinamiento():
	funcion = viveHacinamiento("OSA",12)
	assert funcion == False

def test_porcentajeParticipacionNeta():
	funcion = porcentajeParticipacionNeta("PARRITA")
	assert funcion == 50.4

def test_estaDentroParticipacionEconomica():
	funcion = estaDentroParticipacionEconomica("BELEN", 99)
	assert funcion == False

def test_porcentajeDiscapacitados():
	funcion = porcentajeDiscapacitados("SANTO DOMINGO")
	assert funcion == 9.3

def test_esDiscapacitado():
	funcion = esDiscapacitado("TURRIALBA", 5)
	assert funcion == True

def test_porcHogarJefaturaCompartida():
	funcion = porcHogarJefaturaCompartida("PARAISO")
	assert funcion == 4.9

def test_viveHogarJefaturaCompartida():
	funcion = viveHogarJefaturaCompartida("ATENAS", 14)
	assert funcion == False

