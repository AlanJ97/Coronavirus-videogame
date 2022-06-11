#IMPORTANDO LO NECESARIO PARA CREAR EL VIDEOJUEGO
import pygame, random

#INICIALIZAR PYGAMEEEEEEE
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
playerRect = playerImg.get_rect()
playerRect.x, playerRect.y = 300, 500
player_movementX = 0
salto = 10
Jumping = False

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
virusRect = []
virus_movementX = []
virus_movementY = []
num_of_enemies = 3

for i in range(num_of_enemies):
    virusImg.append(pygame.image.load('Imagenes/virus2.png'))
    virusRectX.append(random.randint(100,900))
    virusRectY.append(random.randint(50,450))
    virusRect.append(virusImg[i].get_rect())
    virus_movementX.append( random.choice([4,-4]) )
    virus_movementY.append(  random.choice([4,-4]) )

#FUNCIÓN QUE COLOCA AL PERSONAJE ENEMIGO EN PANTALLA CON SUS MOVIMIENTOS
def fijar_personaje_enemigo():
    for i in range(len(virusImg)):
        screen.blit(virusImg[i], (virusRectX[i], virusRectY[i]))


#CARACTERISTICAS DE LAS PERSONAS EXTRAS
personasImg = []
personasRectX = []
personasRectY = []
personasRect = []
personas_movementX = []
num_of_personas = 5

for i in range(num_of_personas):
    personasImg.append(pygame.image.load('Imagenes/persona1.png'))
    personasRectX.append(random.randint(100,900))
    personasRectY.append(600)
    personasRect.append(personasImg[i].get_rect())
    personas_movementX.append( random.choice([4,-4]) )

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

        #MOVIMIENTOS DE LOS PERSONAJES CON LAS TECLAS (WASD)
            #ESTO PASA CUANDO PRECIONAMOS UNA TECLA
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_movementX = -5
            if event.key == pygame.K_d:
                player_movementX = 5
            if event.key == pygame.K_w:
                Jumping = True
            #ESTO PASA CUANDO SOLTAMOS UNA TECLA
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player_movementX = 0


    #ASIGNANDO RESTRICCIONES A PERSONAJES POR LA RESOLUCION
        #PERSONAJE PRINCIPAL
    playerRect.x += player_movementX
    if playerRect.x<0:
        playerRect.x=0
    if playerRect.x >1230:
        playerRect.x = 1230
        #PERSONAJE ENEMIGO
    for i in range(num_of_enemies):
        if virusRectX[i] <=0:
            virus_movementX[i] = 4
        if virusRectX[i] >=1220:
            virus_movementX[i] = -4
        if virusRectY[i] <=0:
            virus_movementY[i] = 4
        if virusRectY[i] >=580:
            virus_movementY[i] = -4
        virusRectX[i] += virus_movementX[i]
        virusRectY[i] += virus_movementY[i]
        #PERSONAS EXTRAS
    for i in range(num_of_personas):
        if personasRectX[i]<0:
            personas_movementX[i] = 4
        if personasRectX[i] >1230:
            personas_movementX[i] = -4
        personasRectX[i]  += personas_movementX[i]



    #SALTO DEL PERSONAJE PRINCIPAL
    if Jumping:
        if salto >= -10:
            playerRect.y -= (salto * abs(salto)) * 0.5
            salto -= 1
        else:   
            salto = 10
            Jumping = False

    #EJECUTANDO ACTUALIZACIONES
    fijar_plataformas()
    fijar_personaje_enemigo()
    fijar_personas_extras()
    fijar_corazones()
    fijar_puntaje()
    fijar_personaje_principal(playerRect.x, playerRect.y)
    pygame.display.update()
    clock.tick(30)
