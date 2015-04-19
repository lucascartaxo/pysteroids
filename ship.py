import pygame, sys, os
import math

class Ship:

    def __init__(self, screen):
        self.invulnerable = True
        self.timer  = pygame.time.get_ticks()

        #velocidade maxima
        self.max_speed = 1.7
        self.min_speed = -1.7

        #angulo inicial da nave.
        self.rotation = 0

        #posicao inicial da nave
        self.pos = {}
        self.pos["x"] = screen.get_width() / 2 
        self.pos["y"] = screen.get_height() / 2 #posicao inicial
        
        
        self.speed = 0 #velocidade inicial

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
        pygame.draw.line(screen, (0,0,255), [self.pos["x"] - 8, self.pos["y"] - 4], [self.pos["x"] ,self.pos["y"] + 20], 3)
        pygame.draw.line(screen, (0,0,255), [self.pos["x"] ,self.pos["y"] + 20], [self.pos["x"] + 8, self.pos["y"] - 4], 3)
        pygame.draw.line(screen, (0,0,255), [self.pos["x"] - 7 ,self.pos["y"]], [self.pos["x"] + 7, self.pos["y"]], 3)

    def rotate_left(self):
        self.rotation -= 1


    def rotate_right(self):
        self.rotation += 1


    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1

    def update(self):
        self.pos["x"] = self.pos["x"] + math.cos(self.rotation) * self.speed
        self.pos["y"] = self.pos["y"] + math.sin(self.rotation) * self.speed



