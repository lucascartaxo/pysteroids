import pygame, sys, os

class Ship:

    def __init__(self, screen):
        self.invulnerable = True
        self.timer  = pygame.time.get_ticks()

        #velocidade maxima
        self.max_speed = 1.7
        self.min_speed = -1.7

        #graus de rotacao por loop
        self.rotate_speed = 2
        self.last_rotation = 0

        #angulo inicial da nave.
        self.rotation = 180.0

        #posicao inicial da nave
        self.pos = [screen.get_width() / 2 ,screen.get_height() / 2] #posicao inicial
        
        
        self.speed = [0,0] #velocidade inicial

        self.thrust = 0.01  #ganho de velocidade enqto pressiona para cima.

        #cor da nave
        self.color = (255,255,255)

        #variaveis de controle das teclas
        self.left = False
        self.right = False
        self.up = None
        self.shooting = False
        self.lives = 3

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.pos[0],self.pos[1], 10,10), 0)
