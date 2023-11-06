from sprites import reescalar_imagenes, obtener_rectangulos
from lista_proyectiles import *

class Personaje:
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad, vida):
        #TAMAÑO PERSONAJE
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #GRAVEDAD
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False
        #ANIMACIONES
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.ultimo_movimiento = "derecha"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        #RECTANGULOS
        rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)
        #MOVIMIENTO
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        #ATRIBUTOS
        self.vida = vida
        self.colisiona = False
        self.hizo_daño = False
        #PROYECTIL
        self.lista_de_proyectiles = []

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    def animar(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1

    def mover(self, velocidad, tamaño_pantalla):

        limite_derecho = tamaño_pantalla[0]
        limite_izquierdo = 0

        #Verifica que no se vaya del limite derecho
        if self.lados["main"].right + velocidad > limite_derecho:
            diferencia = limite_derecho - self.lados["main"].right
            if diferencia > 0:
                velocidad = diferencia
            else:
                velocidad = 0

        #Verifica que no se vaya del limite izquierdo
        if self.lados["main"].left + velocidad < limite_izquierdo:
            diferencia = limite_izquierdo - self.lados["main"].left
            if diferencia > 0:
                velocidad = diferencia
            else:
                velocidad = 0

        #Aplica la velocidad a todos los lados del rectangulo
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def aplicar_gravedad(self, pantalla,piso):
        if self.esta_saltando:
            self.animar(pantalla, "salta")
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

            if self.lados["bottom"].colliderect(piso["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados["main"].bottom = piso["main"].top 
            else:
                self.esta_saltando = True

    def update(self, pantalla, piso, tamaño_pantalla):
        match self.que_hace:
            case "derecha":
                self.ultimo_movimiento = "derecha"
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_derecha")
                self.mover(self.velocidad, tamaño_pantalla)
            case "izquierda":
                self.ultimo_movimiento = "izquierda"
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_izquierda")
                self.mover(self.velocidad * - 1, tamaño_pantalla)
            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            case "preparado":
                if not self.esta_saltando:
                    if self.ultimo_movimiento == "derecha":
                        self.animar(pantalla, "personaje_preparado")
                    else:
                        self.animar(pantalla, "personaje_preparado_izquierda")
            case "ataca":
                if not self.esta_saltando:
                    if self.ultimo_movimiento == "derecha":
                        self.animar(pantalla, "personaje_ataque")
                    else:
                        self.animar(pantalla, "personaje_ataque_izquierda")
            case "quieto":
                if not self.esta_saltando:
                    if self.ultimo_movimiento == "derecha":
                        self.animar(pantalla, "quieto_derecha")
                    if self.ultimo_movimiento == "izquierda":
                        self.animar(pantalla, "quieto_izquierda")

        self.aplicar_gravedad(pantalla, piso)

    def bala_personaje(self, pantalla, trayecto_es, velocidad, ubicacion_personaje):
        puño = Proyectil(tamaño, ubicacion_personaje, diccionario_animaciones, velocidad)
        self.lista_de_proyectiles.append(puño)
        for puño in self.lista_de_proyectiles:
            if trayecto_es == "proyectil_derecha":
                puño.bala(pantalla, trayecto_es, velocidad)
            if trayecto_es == "proyectil_izquierda":
                puño.bala(pantalla, trayecto_es, velocidad)

    def dañar(self, rect_enemigo):
        if self.lados["bottom"].colliderect(rect_enemigo):
            self.hizo_daño = True
            return True

    def vidas(self, vida:int):
        match vida:
            case 1:
                self.vida = self.vida - 1
            case 2:
                self.vida = self.vida - 1
            case 3:
                self.vida = self.vida - 1
        if self.vida == 0:
            return True
        else:
            return False