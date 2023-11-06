from sprites import reescalar_imagenes, obtener_rectangulos

class Proyectil():
    def __init__(self, tamaño, ubicacion_personaje, animaciones, velocidad):
        #TAMAÑO PROYECTIL
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #TRAYECTORIA Y VELOCIDAD
        self.x = ubicacion_personaje[0]
        self.y = ubicacion_personaje[1]
        self.trayectoria_x = 5
        self.trayectoria_y = 0 
        self.velocidad = velocidad
        #ANIMACIONES
        self.contador_trayecto = 0
        self.animaciones = animaciones
        self.que_hace = "quieto"
        self.reescalar_animaciones()
        #RECTANGULOS
        rectangulo = self.animaciones["proyectil_derecha"][0].get_rect()
        self.lados = obtener_rectangulos(rectangulo)

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    def animar(self, pantalla, que_animacion):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_trayecto >= largo:
            self.contador_trayecto = 0
        
        pantalla.blit(animacion[self.contador_trayecto], self.lados["main"])
        self.contador_trayecto += 1

    def mover(self, velocidad):
        limite_derecho = 1400
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

    def daño(self, rect_enemigo):
        if self.lados["right"].colliderect(rect_enemigo):
            print("SIIIIII")
            si = True
        if self.lados["left"].colliderect(rect_enemigo):
            si = True
        return si
    
    def bala(self, pantalla, trayecto_es, velocidad):
        self.animar(pantalla, trayecto_es)
        self.mover(velocidad)

