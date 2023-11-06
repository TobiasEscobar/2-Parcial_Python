import pygame
from sprites  import *
from clase_personaje import Personaje
from lista_enemigos import *
from modo_programador import *
from constantes import * 

######################################################################

def actualizar_pantalla(pantalla, un_personaje: Personaje, lados_piso, tamaño_pantalla):
    un_personaje.update(pantalla, lados_piso, tamaño_pantalla)
######################################################################

pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA =  pygame.display.set_mode((TAMAÑO_PANTALLA))

fondo = pygame.image.load("2-Parcial/Juego-Parcial/Sprites/fondo_casa3_copia.png")
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)

plataforma_1 = pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Terrenos/terreno (58).png")
plataforma_1 = pygame.transform.scale(plataforma_1, (800,200))

#PERSONAJE
posicion_inicial = (H/2 - 350, 620)
tamaño = (75,85)
acumular_daño = 0
hizo_daño = False

#Animaciones del personaje
diccionario_animaciones = {}
diccionario_animaciones["quieto_derecha"] = personaje_quieto_derecho
diccionario_animaciones["quieto_izquierda"] = personaje_quieto_izquierda
diccionario_animaciones["salta"] = personaje_salta
diccionario_animaciones["camina_derecha"] = personaje_camina
diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda
diccionario_animaciones["personaje_preparado"] = personaje_prepara_ataque
diccionario_animaciones["personaje_ataque"] = personaje_lanza_ataque
diccionario_animaciones["personaje_preparado_izquierda"] = personaje_prepara_ataque_izquierda
diccionario_animaciones["personaje_ataque_izquierda"] = personaje_lanza_ataque_izquierda
diccionario_animaciones["personaje_muere"] = personaje_muere


#Creacion de personaje y jefe
mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, 10, 3)


#PISO
piso = pygame.Rect(0,0,W,10)
piso.top = mi_personaje.lados["main"].bottom + 50
lados_piso = obtener_rectangulos(piso)


#TIMERS

#Timer de tiempo de juego
segundos = "25"
fin_tiempo = False
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos, 1000)
fuente = pygame.font.SysFont("Arial", 20)

#Timer de enemigos
timer_enemigos = pygame.USEREVENT + 1
pygame.time.set_timer(timer_enemigos, 500)

flag = True
while flag:
    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
        if evento.type == timer_segundos:
            if fin_tiempo == False:
                segundos = int(segundos) - 1
                if int(segundos) == 0:
                    fin_tiempo = True
                    lista_enemigos[0].simular_movimiento(0, PANTALLA)
                    lista_enemigos[1].simular_movimiento(0, PANTALLA)
                    #lista_enemigos[2].simular_movimiento(0, PANTALLA)
        elif evento.type == timer_enemigos:
            if fin_tiempo == False:
                lista_enemigos[0].simular_movimiento(10, PANTALLA)
                lista_enemigos[1].simular_movimiento(10, PANTALLA)
                #lista_enemigos[2].simular_movimiento(10, PANTALLA)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        mi_personaje.que_hace = "derecha"
        camino_derecha = True
    elif keys[pygame.K_LEFT]:
        mi_personaje.que_hace = "izquierda"
        camino_izquierda = True
    elif keys[pygame.K_UP]:
        mi_personaje.que_hace = "salta"
    elif keys[pygame.K_SPACE]:
        mi_personaje.que_hace = "preparado"
        if keys[pygame.K_d]:
            mi_personaje.que_hace = "ataca"
            mi_personaje.bala_personaje(PANTALLA, "proyectil_derecha", 10, (mi_personaje.lados["main"].x, mi_personaje.lados["main"].y))
    else:
        mi_personaje.que_hace = "quieto"

    #Fondo e informacion para el usuario
    PANTALLA.blit(fondo, (0,0))
    segundos_texto = fuente.render("Tiempo: " + str(segundos), True, COLOR_BLANCO)
    PANTALLA.blit(segundos_texto, (0,0))
    #PANTALLA.blit(plataforma_1, (0,600))

    #Mostrar en pantalla enemigo, personaje, y jefes
    for enemigo in lista_enemigos:
        actualizar_pantalla(PANTALLA, enemigo, lados_piso, TAMAÑO_PANTALLA)
    actualizar_pantalla(PANTALLA, mi_personaje, lados_piso, TAMAÑO_PANTALLA)

    
    #Vida y daño de personaje y enemigos
    for enemigo in lista_enemigos:
        colisiono = enemigo.colisionar(mi_personaje.lados["main"])
        hacer_daño = mi_personaje.dañar(enemigo.lados["top"])

        if colisiono == True:
            acumular_daño += 1
            restar_vida = mi_personaje.vidas(acumular_daño)
            if restar_vida == True:
                print("MURIO EL PJ")
            else:
                print("Sigue vivo")
        
        if hacer_daño == True:
            print("Enemigo muerto")

    if get_modo():
        for lado in lados_piso:
            pygame.draw.rect(PANTALLA, "Black", lados_piso[lado], 2)
        for lado in mi_personaje.lados:
            pygame.draw.rect(PANTALLA, "Orange", mi_personaje.lados[lado], 2)
        for enemigo in lista_enemigos:
            for lado in enemigo.lados:
                pygame.draw.rect(PANTALLA, "Black", enemigo.lados[lado], 2)
        #for proyectil in lista_proyectiles:
        #    for lado in proyectil.lados:
        #        pygame.draw.rect(PANTALLA, "Black", proyectil.lados[lado], 2)

    pygame.display.flip()
pygame.display.quit()