import pygame, sys, os
import math
from common import *

class Ship(pygame.sprite.Sprite):

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.init(screen)

    def init(self, screen):
        self.invulnerable = True
        self.timer  = pygame.time.get_ticks()

        #velocidade maxima
        self.max_speed = 1.7
        self.min_speed = -1.7

        #angulo inicial da nave.
        self.rotation = 0

        #tamanho
        self.width = 16
        self.height = 24

        self.size = self.width, self.height

        #posicao inicial da nave
        self.pos = {}
        self.pos["x"] = screen.get_width() / 2 
        self.pos["y"] = screen.get_height() / 2 #posicao inicial

        self.speed = 0 #velocidade inicial

        self.thrust = 0.01  #ganho de velocidade enqto pressiona para cima.

        #cor da nave
        self.color = (255,0,255)

        #variaveis de controle das teclas
        self.left = False
        self.right = False
        self.up = None
        self.shooting = False
        self.lives = 3

        #shape original
        self.shape = [[0, 20], [-140, 20], [180, 7.5], [140, 20]]
        
        #shape que sera rotacionado e reposicionado
        self.draw_shape = [[0, 20], [-140, 20], [180, 7.5], [140, 20]]

        ###########
        # self.rect = pygame.draw.aalines(screen,self.color,True,self.draw_shape,True) 

    def draw(self, screen):
        self.rect = pygame.draw.aalines(screen,self.color,True,self.draw_shape,True)

    def rotate_left(self):
        self.rotation -= 5


    def rotate_right(self):
        self.rotation += 5


    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1

    def update(self):
        pass
        self.pos["x"] = self.pos["x"] + math.cos(math.radians(self.rotation)) * self.speed
        self.pos["y"] = self.pos["y"] + math.sin(math.radians(self.rotation)) * self.speed

    def position():
        return self.pos["x"], self.pos["y"]



