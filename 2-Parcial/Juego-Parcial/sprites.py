import pygame

def reescalar_imagenes(lista_imagenes, tamaño):
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], tamaño)

def girar_imagenes(lista, flip_x, flip_y):
    lista_girada = []
    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

def obtener_rectangulos(principal)->dict:
    diccionario = {}

    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom -10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right -10, principal.top, 10, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 10, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)

    return diccionario

#PERSONAJE PRINCIPAL:
personaje_quieto_derecho = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Quieto/Quieto.png")]

personaje_quieto_izquierda =  girar_imagenes(personaje_quieto_derecho, True, False)

personaje_camina = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Caminar/caminar-m (2).png"), 
                    pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Caminar/caminar-m (3).png"), 
                    pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Caminar/caminar-m (4).png"), 
                    pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Caminar/caminar-m (5).png")
                    ]

personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)

personaje_salta = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Saltar/Salta (1).png")]

personaje_prepara_ataque = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Golpear/Golpe (2).png")]

personaje_lanza_ataque = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Golpear/Golpe (1).png")]

personaje_prepara_ataque_izquierda = girar_imagenes(personaje_prepara_ataque, True, False)

personaje_lanza_ataque_izquierda = girar_imagenes(personaje_lanza_ataque, True, False)

personaje_muere = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Daño/Daño.png")]

#PROYECTIL 
proyectil_derecha = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Golpear/Puño (1).png"), 
                    pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Golpear/Puño (2).png"),
                    pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Golpear/Puño (3).png")]

proyectil_izquierda = girar_imagenes(proyectil_derecha, True, False)

#ENEMIGO BASICO:
enemigo_camina_izquierda = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Enemigos/Camina(1).png"), 
                            pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Enemigos/Camina(2).png")]

enemigo_camina = girar_imagenes(enemigo_camina_izquierda, True, False)

enemigo_quieto = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Enemigos/Quieto.png")]

enemigo_quieto_izquierda = girar_imagenes(enemigo_quieto, True, False)

enemigo_ataca = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Enemigos/Ataca(1).png")]

enemigo_muere = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Enemigos/Muere.png")]


#ENEMIGO JEFE:
#jefe_camina = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Enemigos/camina1.png")]
#
#jefe_camina_izquierda = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Enemigos/camina1.png")]
#
#jefe_quieto = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Enemigos/camina1.png")]
#
#jefe_ataca = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Enemigos/camina1.png")]
#
#jefe_muere = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Enemigos/camina1.png")]



#Plataformas

