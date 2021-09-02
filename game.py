#IMPORTANDO LO NECESARIO PARA CREAR EL VIDEOJUEGO
import pygame, random

#INICIALIZAR PYGAME
pygame.init()

#ESPECIFICANDO LOS FPS
clock = pygame.time.Clock()

#TÍTULO DEL JUEGO
pygame.display.set_caption("LA PANDEMIA: SURVIVORS")

#CREANDO LA PANTALLA
screen_width, screen_height = 1300, 685
screen = pygame.display.set_mode((screen_width, screen_height))

#FONDO DEL JUEGO EN UNA VARIABLE
background = pygame.image.load("Fondos/fondo1.png")

#CARACTERISTICAS DEL PERSONAJE PRINCIPAL
playerImg = pygame.image.load('Imagenes/doctor1.png')

#FUNCIÓN QUE COLOCA AL PERSONAJE PRINCIPAL EN PANTALLA CON SUS MOVIMIENTOS
def fijar_personaje_principal(personajeX, personajeY):
    screen.blit(playerImg, (personajeX, personajeY ))

#CARACTERISTICAS DE PLATAFORMAS PARA SALTAR
plataformaImg = []
plataformaRectX = [60,650,270,450, 820,950] 
plataformaRectY = [450,450,300, 150, 175, 375]
number_of_platforms = 6
for i in range(number_of_platforms):
    plataformaImg.append(pygame.image.load('Imagenes/plataforma.png'))
   
#FUNCION QUE COLOCA LAS PLATAFORMAS EN PANTALLA
def fijar_plataformas():
    for i in range(number_of_platforms):
        screen.blit(plataformaImg[i], (plataformaRectX[i], plataformaRectY[i]))

#CARACTERISTICAS DEL PERSONAJE ENEMIGO (CORONAVIRUS)
virusImg = []
virusRectX = []
virusRectY = []
num_of_enemies = 3

for i in range(num_of_enemies):
    virusImg.append(pygame.image.load('Imagenes/virus2.png'))
    virusRectX.append(random.randint(100,900))
    virusRectY.append(random.randint(50,450))

#FUNCIÓN QUE COLOCA AL PERSONAJE ENEMIGO EN PANTALLA CON SUS MOVIMIENTOS
def fijar_personaje_enemigo():
    for i in range(len(virusImg)):
        screen.blit(virusImg[i], (virusRectX[i], virusRectY[i]))


#CARACTERISTICAS DE LAS PERSONAS EXTRAS
personasImg = []
personasRectX = []
personasRectY = []
num_of_personas = 5

for i in range(num_of_personas):
    personasImg.append(pygame.image.load('Imagenes/persona1.png'))
    personasRectX.append(random.randint(100,900))
    personasRectY.append(600)

#FUNCION QUE FIJA A LOS PERSONAJES EXTRAS EN PANTALLA
def fijar_personas_extras():
    for i in range(len(personasImg)):
        screen.blit(personasImg[i],(personasRectX[i] , personasRectY[i]) )


#CARACTERISTICAS DE LAS VIDAS QUE TENEMOS
corazonImg = []
corazon_rotoImg = pygame.image.load('Imagenes/broken-heart1.png')
corazonRectX = [10, 80, 150, 220, 290]
corazonRectY = [20, 20 , 20, 20, 20]
for i in range(len(corazonRectX)):
    corazonImg.append(pygame.image.load('Imagenes/heart2.png'))

#FUNCION QUE COLOCA LOS CORAZONES EN PANTALLA
def fijar_corazones():
    for i in range(len(corazonRectX)):
        screen.blit(corazonImg[i], (corazonRectX[i], corazonRectY[i]))

#CARACTERISTICAS DE LAS VACUNAS QUE TENEMOS QUE CONSEGUIR
puntajeImg = []
puntajeRectX = [910, 990, 1060, 1130, 1200]
puntajeRectY = [20, 20 , 20, 20, 20]
for i in range(5):
    puntajeImg.append(pygame.image.load('Imagenes/Salud-incompleta.png'))

def fijar_puntaje():
    for i in range(len(puntajeImg)):
        screen.blit(puntajeImg[i], (puntajeRectX[i], puntajeRectY[i]))

#LOOP DEL JUEGO, AQUÍ SE EJECUTA PARA ACTUALIZAR CADA FRAME
jugando = True
while jugando:
    #COLOCANDO FONDO DE PANTALLA 
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        #CERRAR JUEGO
        if event.type == pygame.QUIT:
            jugando = False

    #EJECUTANDO ACTUALIZACIONES
    fijar_personaje_principal(300, 500)
    fijar_plataformas()
    fijar_personaje_enemigo()
    fijar_personas_extras()
    fijar_corazones()
    fijar_puntaje()
    pygame.display.update()
    clock.tick(30)