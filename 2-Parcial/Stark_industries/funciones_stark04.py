# Desafío #04:
# IMPORTANTE: Para todas y cada una de las funciones creadas, documentarlas
# escribiendo que es lo que hacen, que son los parámetros que reciben (si es una lista,
# un string, etc y que contendrá) y que es lo que retorna la función!

import re
from data_stark import *

# 1.1. Crear la función ‘extraer_iniciales’ que recibirá como parámetro:
# ● nombre_heroe: un string con el nombre del personaje
# La función deberá devolver a partir del parámetro recibido un nuevo string con
# las iniciales del nombre del personaje seguidos por un punto (.)
# ● En el caso que el nombre del personaje contenga el artículo ‘the’ se
# deberá omitir de las iniciales
# ● Se deberá verificar si el nombre contiene un guión ‘-’ y sólo en el caso
# que lo tenga se deberá reemplazar por un espacio en blanco
# La función deberá validar:
# ● Que el string recibido no se encuentre vacío
# Devolver ‘N/A’ en caso de no cumplirse la validación
# Ejemplo de la salida de la función para Howard the Duck:
# H.D.
# ATENCIÓN: Usar regex

def extraer_iniciales(nombre_heroe:str)->str:
    if nombre_heroe == "":
        return print("N/A")
    else:
        nombre = re.findall(r'[A-Z]+', nombre_heroe)
        iniciales = ".".join(nombre) + "."
        return iniciales

# 1.2. Crear la función obtener_dato_formato’ la cual recibirá como
# parámetro:
# ● dato: un string con un dato especifico
# La función deberá convertir el dato pasado a minúsculas y con formato
# snake_case
# por ejemplo: Howard the Duck -&gt; howard_the_duck
# La función deberá validar:
# ● Que el dato recibido sea del tipo str
# En caso de encontrar algún error retornar False, caso contrario el nombre con
# el formato especificado
# ATENCIÓN: Usar regex

def obtener_dato_formato(dato:str)->str:
    if type(dato) == str:
        dato = dato.lower()  
        dato = re.sub(r'[\s-]', '_', dato)
        return dato
    else:
        return False

# 1.3. Crear la función ‘stark_imprimir_nombre_con_iniciales’ la cual recibirá
# como parámetro:
# ● nombre_heroe: un string con el nombre del personaje
# Se deberá validar:
# ● Que el dato recibido sea del tipo diccionario
# ● Que el diccionario contengan la clave ‘nombre’
# La función deberá imprimir el dato en cuestión con el siguiente formato
# Delante de cada nombre se deberá agregar un asterisco ‘*’ (de forma de
# viñeta) seguido de un espacio.
# Si el superhéroe es Howard the Duck se deberá mostrar

# * howard_the_duck (H.W.)
# La función deberá devolver True en caso de haber finalizado con éxito o False
# en caso de que haya ocurrido un error

def stark_imprimir_nombre_con_iniciales(nombre_heroe:str)->str:
    if type(nombre_heroe) != dict or "nombre" not in nombre_heroe:
        return False
    else:
        nombre = nombre_heroe['nombre']
        formato = obtener_dato_formato(nombre)
        iniciales = extraer_iniciales(nombre)
        nombre_con_iniciales = f"* {formato} ({iniciales})"
        print(nombre_con_iniciales)
        return True

# 1.4 Crear la función ‘stark_imprimir_nombres_con_iniciales’ la cual recibirá
# como parámetro:
# ● lista_heroes: la lista de personajes
# La función deberá utilizar la función anterior
# Luego deberá imprimir la lista completa de los nombres de los personajes
# con el mismo formato de la anterior
# Se deberá validar:
# ● Que lista_heroes sea del tipo lista
# ● Que la lista contenga al menos un elemento
# La función retornara True si salió todo bien y False si ocurrió algún error

def stark_imprimir_nombres_con_iniciales(lista_heroes:list):
    if type(lista_heroes) != list or len(lista_heroes) == 0:
        return False
    else:
        for heroe in lista_heroes:
            stark_imprimir_nombre_con_iniciales(heroe)
        return True