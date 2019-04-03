# -*- coding: utf-8 -*-
import pygame # Librería de pygameame
import math
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores RGB
BLANCO = (255,255,255)  
VERDE = (27,94,32)    
ROJO = (255,0,0)     
AZUL = (0,0,255)
negro = (0,0,0)
listColors=[VERDE,BLANCO,ROJO,AZUL]

def main():
    print('            Mision 06')
    print('-----------------------------------')
    r = int(input("Dame r: "))
    R = int(input("Dame R: "))
    l = float(input("Dame l: "))
    print('-----------------------------------')
    dibujar(r,R,l)
    
def dibujar(r,R,l):
    # Inicializa pygameame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    window = pygame.display.set_mode((ANCHO, ALTO))  
    clock = pygame.time.Clock()  
    ends = False  

    while not ends:  #ciclo para ejecutar el pygame hasta que se cierre la ventana
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  
                ends = True
        # Borrar pantalla
        window.fill(negro)

        for angulo in range(0, 360 * (r // math.gcd(r, R)),1):
            a = math.radians(angulo)
            k = r / R
            x = R*(((l-k)*math.cos(a))+(l*k*math.cos(((l-k)*a)/k)))
            y = R*(((l-k)*math.sin(a))-(l*k*math.sin(((l-k)*a)/k)))
            indexColorRandom=random.randrange(4) #genera el indice aleatorio para seleccionar un color
            color=listColors[indexColorRandom] #se llama al color correspondiente al indice aleatorio en la lista de colores
            pygame.draw.circle(window, color, (int(x + ANCHO//2), int(ALTO //2 - y)), 1) #dibujar circulo
            
        pygame.display.flip()  # actualizar pantalla
        clock.tick(60)  # frecuencia de actualizacion = 60 fps

    
    pygame.quit()

main()