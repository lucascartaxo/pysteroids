import pygame
import sys
import random

pygame.init()
tela = pygame.display.set_mode((640,480))
tela.fill((255,255,255))

fonte = pygame.font.SysFont("arial",42)
textGameOver = fonte.render("GAME OVER", True, (255,0,0))
textVitoria = fonte.render("VOCE VENCEU", True, (0,255,0))

fim = False
vitoria = False

barra1 = (320,110,40,random.randint(50,300))
barra2 = (400,10,40,random.randint(50,300))
barra3 = (480,10,40,random.randint(50,300))
barra4 = (560,10,40,random.randint(50,300))

velbarra1 = random.randint(12,25)
velbarra2 = random.randint(12,25)
velbarra3 = random.randint(12,25)
velbarra4 = random.randint(12,25)

sentbarra1 = "abaixo"
sentbarra2 = "abaixo"
sentbarra3 = "abaixo"
sentbarra4 = "abaixo"


def detectaColisao(personagem, barra):
    x1a = personagem[0]
    y1a = personagem[1]
    x2a = personagem[2]
    y2a = personagem[3]

    x1b=barra[0]
    y1b=barra[1]
    x2b=x1b+barra[2]
    y2b=y1b+barra[3]

    if x2a > x1b and x1a < x2b and y2a > y1b and y1a < y2b:
        return True
    else:
        return False

def desenhaBarra(tela, coords):
    pygame.draw.rect(tela, (0,0,0), coords, 0)

def moveBarra(barra,sentido,velocidade):
    if sentido=="abaixo":
        if (barra[1]+barra[3])>=480:
            sentido="acima"
            velocidade=velocidade*-1
    elif sentido=="acima":
        if barra[1]<=0:
            sentido="abaixo"
            velocidade=velocidade*-1

    return (sentido,velocidade)

def desenhaPersonagem(tela, coords):
    pygame.draw.circle(tela, (255, 0, 0), (coords [0], coords[1]), 19, 0)
    return (coords[0] - 19, coords [1] -19, coords [0] +19, coords[1] +19)

while True:
    # evento = pygame.event.poll()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                fim = False
                vitoria = False
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


    if not fim:
        desenhaBarra(tela, barra1)
        desenhaBarra(tela, barra2)
        desenhaBarra(tela, barra3)
        desenhaBarra(tela, barra4)

        pygame.time.delay(30)
        pygame.display.flip()

        tela.fill((255,255,255))

        sentbarra1,velbarra1=moveBarra(barra1,sentbarra1,velbarra1)
        sentbarra2,velbarra2=moveBarra(barra2,sentbarra2,velbarra2)
        sentbarra3,velbarra3=moveBarra(barra3,sentbarra3,velbarra3)
        sentbarra4,velbarra4=moveBarra(barra4,sentbarra4,velbarra4)

        barra1=(barra1[0],barra1[1]+velbarra1,barra1[2],barra1[3])
        barra2=(barra2[0],barra2[1]+velbarra2,barra2[2],barra2[3])
        barra3=(barra3[0],barra3[1]+velbarra3,barra3[2],barra3[3])
        barra4=(barra4[0],barra4[1]+velbarra4,barra4[2],barra4[3])

        mousecoords = pygame.mouse.get_pos()
        coordsPersonagem = desenhaPersonagem(tela,mousecoords)

        if detectaColisao (coordsPersonagem, barra1) or detectaColisao (coordsPersonagem, barra2) or detectaColisao (coordsPersonagem, barra3) or detectaColisao (coordsPersonagem, barra4):
            fim = True

        elif mousecoords[0] >= 621:
            fim = True
            vitoria = True

    elif fim and vitoria == True:
        tela.fill((0,0,0))
        tela.blit(textVitoria, (220,200))
        pygame.display.flip()
    else:
        tela.fill ((0,0,0))
        tela.blit(textGameOver, (230,200))
        pygame.display.flip()