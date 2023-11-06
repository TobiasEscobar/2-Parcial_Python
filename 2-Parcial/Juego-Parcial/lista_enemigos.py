from clase_enemigo import Enemigo
from sprites import *
from constantes import *

diccionario_animaciones_enemigas = {}
diccionario_animaciones_enemigas["quieto_derecha"] = enemigo_quieto
diccionario_animaciones_enemigas["quieto_izquierda"] = enemigo_quieto_izquierda
diccionario_animaciones_enemigas["camina_derecha"] = enemigo_camina
diccionario_animaciones_enemigas["camina_izquierda"] = enemigo_camina_izquierda
diccionario_animaciones_enemigas["muere"] = enemigo_muere

posicion_inicial = (H/2 + 300 ,550) #550 es la altura de la pantalla
posicion_inicial_2 = (H/2 + 700 ,550)
posicion_inicial_3 = (H/2 + 100 ,550)
lados_enemigo = (600, 900)
lados_enemigo_2 = (200, 600)
lados_enemigo_3 = (900, 1000)
tamaño_enemigo = (75,85)

enemigo_basico = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posicion_inicial, 30, 3, lados_enemigo)
enemigo_basico_dos = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posicion_inicial_2, 30, 3, lados_enemigo_2)
enemigo_basico_tres = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posicion_inicial_3, 30, 3, lados_enemigo_3)

lista_enemigos = []

lista_enemigos.append(enemigo_basico)
lista_enemigos.append(enemigo_basico_dos)
#lista_enemigos.append(enemigo_basico_tres)