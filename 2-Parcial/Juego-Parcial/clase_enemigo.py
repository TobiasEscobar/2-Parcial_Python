from sprites import reescalar_imagenes, obtener_rectangulos

class Enemigo():
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad, vida, que_lado):
        #TAMAÑO ENEMIGO
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
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

        self.delta_tiempo = 0
        self.tiempo_reaccion = 10
        self.lado_I = que_lado[0]
        self.lado_R = que_lado[1]

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

    def update(self, pantalla, piso, tamaño_pantalla):
        match self.que_hace:
            case "derecha":
                self.ultimo_movimiento = "derecha"
                self.animar(pantalla, "camina_derecha")
                self.mover(self.velocidad, tamaño_pantalla)
            case "izquierda":
                self.ultimo_movimiento = "izquierda"
                self.animar(pantalla, "camina_izquierda")
                self.mover(self.velocidad * - 1, tamaño_pantalla)
            #case "preparado":
            #    if self.ultimo_movimiento == "derecha":
            #        self.animar(pantalla, "personaje_preparado")
            #    else:
            #        self.animar(pantalla, "personaje_preparado_izquierda")
            #case "ataca":
            #    if self.ultimo_movimiento == "derecha":
            #        self.animar(pantalla, "personaje_ataque")
            #    else:
            #        self.animar(pantalla, "personaje_ataque_izquierda")
            case "quieto":
                if self.ultimo_movimiento == "derecha":
                    self.animar(pantalla, "quieto_derecha")
                if self.ultimo_movimiento == "izquierda":
                    self.animar(pantalla, "quieto_izquierda")

    def animar_enemigo(self, pantalla, que_animacion):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1

    def mover(self, pantalla):
        lado_izquierdo = self.lado_I
        lado_derecho = self.lado_R

        #Verifica que no se vaya del limite derecho
        if self.lados["main"].right + self.velocidad > lado_derecho:
            diferencia = lado_derecho - self.lados["main"].right
            if diferencia > 0:
                self.velocidad = diferencia
                self.animar_enemigo(pantalla, "camina_derecha")
            else:
                self.velocidad = - 30
                self.animar_enemigo(pantalla, "camina_izquierda")

        #Verifica que no se vaya del limite izquierdo
        if self.lados["main"].left + self.velocidad < lado_izquierdo:
            diferencia = lado_izquierdo - self.lados["main"].left
            if diferencia > 0:
                self.velocidad = diferencia
                self.animar_enemigo(pantalla, "camina_izquierda")
            else:
                self.velocidad = + 30
                self.animar_enemigo(pantalla, "camina_derecha")

        #Aplica la velocidad a todos los lados del rectangulo
        for lado in self.lados:
            self.lados[lado].x += self.velocidad

    def simular_movimiento(self, tiempo, pantalla):
        self.delta_tiempo += tiempo
        if self.delta_tiempo > self.tiempo_reaccion:
            self.mover(pantalla)

    def colisionar(self, rect_personaje):
        if self.lados["right"].colliderect(rect_personaje) or self.lados["left"].colliderect(rect_personaje):
            self.colisiona = True
            return True