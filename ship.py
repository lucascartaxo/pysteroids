import pygame, sys, os
import math
from common import *

class Ship:

    def __init__(self, screen):
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

    def draw(self, screen):
        print "DRAWING!!!"
        print "position: " + str(self.pos["x"]) + ", " + str(self.pos["y"])
        print "rotation: " + str(self.rotation)

        surface = pygame.Surface(Common.SCREEN_SIZE)
        surface.fill((0,255,255))

        surface.set_colorkey((255, 0, 255))

        # rect = pygame.Rect(self.pos["x"], self.pos["y"], self.width, self.height)
        # pygame.draw.line(surface, self.color, [self.pos["x"] - 8, self.pos["y"] - 4], [self.pos["x"] ,self.pos["y"] + 20], 3)
        # pygame.draw.line(surface, self.color, [self.pos["x"] ,self.pos["y"] + 20], [self.pos["x"] + 8, self.pos["y"] - 4], 3)
        # pygame.draw.line(surface, self.color, [self.pos["x"] - 7 ,self.pos["y"]], [self.pos["x"] + 7, self.pos["y"]], 3)

        pygame.draw.line(surface, self.color, [0 - 8, 0 - 4], [0,0 + 20], 3)
        pygame.draw.line(surface, self.color, [0,0 + 20], [0+ 8, 0 - 4], 3)
        pygame.draw.line(surface, self.color, [0 - 7 ,0], [0+ 7, 0], 3)

        rotated_surface = pygame.transform.rotate(surface, self.rotation)
        # rect = rotated_surface.get_rect(center = (self.pos["x"], self.pos["y"]))

        # self.old_center = self.surface.get_rect().center
        # self.surface = pygame.transform.rotate(self.surface, angle)

        screen.blit(rotated_surface, (self.pos["x"], self.pos["y"]))

        # rotated_rect = rotated_surface.get_rect()
        # rotated_rect.center = self.pos["x"], self.pos["y"]

        # screen.blit(surface, [self.pos["x"], self.pos["y"]])

        #################

        ### might work
        # autorect = pygame.Rect(round(autox,0), round(autoy,0), auto.get_width(), auto.get_height())
        # dirty = background.subsurface(autorect.clip(screen.get_rect()))
        # dirtyrect = dirty.get_rect()
        # screen.blit(dirty, (round(autox), round(autoy)))

    def rotate_left(self):
        self.rotation -= 5


    def rotate_right(self):
        self.rotation += 5


    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1

    def update(self):
        self.pos["x"] = self.pos["x"] + math.cos(math.radians(self.rotation)) * self.speed
        self.pos["y"] = self.pos["y"] + math.sin(math.radians(self.rotation)) * self.speed

    def position():
        return self.pos["x"], self.pos["y"]



