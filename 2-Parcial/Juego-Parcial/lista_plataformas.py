import pygame

class Plataforma():
    def __init__(self, tamaño, posicion, colision):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.posicion = posicion
        self.colision = colision

    def reescalar_imagenes(lista_imagenes, tamaño):
        for i in range(len(lista_imagenes)):
            lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], tamaño)