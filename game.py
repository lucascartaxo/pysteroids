# import pygame
# import sys
# import random

import pygame, sys,os
from pygame.locals import *
# from Ship import Ship
# from Asteroid import Asteroid
import math
import random
# from common import *

class Game :

    def __init__(self):
        self.playing = True
        self.over = False
        self.win = False
        
        
        #tamanho da tela.
        self.screen_size = (640,480)
        
        #inicializa o pygame
        pygame.init()
        
        #ajusta o display para o tamanho informado.
        self.window = pygame.display.set_mode(self.screen_size)
        
        #pega a referencia para a "superficie"
        self.screen = pygame.display.get_surface()
        
        #caption da janela.
        pygame.display.set_caption("PYSTEROIDS")
        
        #Nave principal.
        self.ship = Ship(self.screen)
        
        self.start_field()

    def game_loop(self):
        clock = pygame.time.Clock()
        while True:
            # self.process_input(pygame.event.get())
            if self.playing :
                #Move os objetos
                self.move_objects()
                
                #passa os objetos para a tela
                self.draw_objects()
                
                clock.tick(200)
            elif self.over:
                self.window.fill((0,0,0))
                self.draw_over()
                self.reset()
                pygame.display.flip()
            elif self.win:
                self.window.fill((0,0,0))
                self.draw_win()
                pygame.display.flip()
            else:
                self.window.fill((0,0,0))
                self.draw_menu()
                pygame.display.flip()
