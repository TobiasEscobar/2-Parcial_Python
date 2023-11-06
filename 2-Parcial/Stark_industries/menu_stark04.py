#Escobar Tobias Fabricio 
#1-J
#Clase 3

#Ejercicio Integrador Data Stark #04 (segunda entregada)

from os import system
system("cls")

from funciones_stark04 import *

# 6.Crear la función stark_marvel_app la cual recibirá por parámetro la lista de héroes
# y se encargará de la ejecución principal de nuestro programa.
# Utilizar if/elif o match según prefiera. Debe informar por consola en caso de
# seleccionar una opción incorrecta y volver a pedir el dato al usuario. Reutilizar las
# funciones con prefijo stark_ donde crea correspondiente.

menu = [" ",
        "1.Normalizar datos", "2.Mostrar heroes del género NB: ", "3.Mostrar heroe mas alto del genero F: ",
        "4.Mostrar heroe mas alto del genero M: ", "5.Mostrar heroe mas debil del genero M: ", 
        "6.Mostrar heroe mas debil del genero NB: ", "7.Mostrar fuerza promedio del genero NB: ",
        "8.Mostrar la cantidad de cada tipo de color de ojos: ", "9.Mostrar la cantidad de cada tipo de color de pelo: ",
        "10.Mostrar los heroes agrupados por color de ojos: ", "11.Mostrar los heroes agrupados por inteligencia: ",
        "12.Salir\n"]

def mostrar_menu():
    for opcion in menu:
        print(opcion)

seguir = True
while seguir:

    mostrar_menu()
    
    while True:
        respuesta = input("Ingresa una opcion: ")
        if respuesta.isdigit():
            respuesta = int(respuesta)
            if 1 <= respuesta <= 6:
                break
        print("Opción no válida. Ingresa un número del 1 al 6.")

    match respuesta:
        case 1:
            extraer_iniciales("Howard the Duck")
        case 2:
            pass
        case 6:
            seguir = False