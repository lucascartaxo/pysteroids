# import pygame
# import sys
# import random

import pygame, sys,os
from pygame.locals import *
from ship import *
from common import *
import math
import random

class Game :

    def __init__(self):
        self.playing = True
        self.over = False
        self.win = False

        self.sprite_list = [];

        #tamanho da tela.
        self.screen_size = (Common.SCREEN_SIZE)
        
        #inicializa o pygame
        pygame.init()
        
        #ajusta o display para o tamanho informado.
        self.window = pygame.display.set_mode(self.screen_size)
        
        #pega a referencia para a "superficie"
        self.screen = pygame.display.get_surface()
        
        #caption da janela.
        pygame.display.set_caption("PYSTEROIDS")
        
        #Nave principal.
        self.sprite_list.append(Ship(self.screen))
        self.ship = self.sprite_list[0]
        
        # self.start_field()

    def game_loop(self):
        clock = pygame.time.Clock()
        while True:
            self.process_input(pygame.event.get())
            if self.playing:
                self.update()
                
                #passa os objetos para a tela
                self.draw_objects()

                time = pygame.time.get_ticks()
                pygame.display.update()
                clock.tick(24)  

            elif self.over:
                self.window.fill((255,255,255))
                self.draw_over()
                self.reset()
                pygame.display.flip()
            elif self.win:
                self.window.fill((255,255,255))
                self.draw_win()
                pygame.display.flip()
            else:
                self.window.fill((255,255,255))
                self.draw_menu()
                pygame.display.flip()

    def process_input(self,events):
        #pega as teclas pressionadas
        keystate = pygame.key.get_pressed() 
        
        #processa os eventos
        for event in events: 
            if event.type == QUIT or keystate[K_ESCAPE]:
                    sys.exit(0)

            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.ship.rotate_left()

                if event.key == pygame.K_RIGHT:
                    self.ship.rotate_right()
                
                if event.key == pygame.K_UP:
                    self.ship.accelerate()

                if event.key == pygame.K_DOWN:
                    self.ship.decelerate()

                if event.key == pygame.K_RETURN:
                    if self.playing ==  False or self.win == True:
                        self.playing = True
                        self.over = False
                        self.win = False
                        self.ship.lives = 3
                        self.reset()
                        self.start_field()

            print(event)

    def draw_objects(self):
        self.screen.fill((255,255,255))

        if self.win == True:
            self.draw_win()

        self.ship.draw(self.screen)

        pygame.display.flip()

    def update(self):
        self.ship.update()
