#!/usr/bin/env python3

import os, pygame
from pygame.locals import *
from sys import exit

SCREEN_DEFAULT_SIZE = (720, 480)
screen = pygame.display.set_mode((0,0),  pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

full_screen = True
bgcolor = [0, 0, 0]
screen.fill(bgcolor)
pygame.display.update()
infoObject = pygame.display.Info()
print(infoObject)

# colors
ENCODERCOLOR=(0,128,128)
lineCol=(128,128,120)

running = True
radius=80


pygame.init()
pygame.draw.line(screen,lineCol,(0,240),(720,240))
pygame.draw.line(screen,lineCol,(180,0),(180,480))
pygame.draw.line(screen,lineCol,(360,0),(360,480))
pygame.draw.line(screen,lineCol,(540,0),(540,480))


font = pygame.font.SysFont('Arial', 90)
textsurface = font.render('Flipotronics', False, (255, 255, 255))
screen.blit(textsurface,(150,185))



while running:
    mouse = pygame.mouse.get_pos()

    positions = [0,1,2,3]
    for x in positions:
        pygame.draw.circle(screen,ENCODERCOLOR,[x*180 + 90,90],radius)
        pygame.display.update()
    for x in positions:
        pygame.draw.circle(screen,ENCODERCOLOR,[x*180 + 90,390],radius)
        pygame.display.update()

    if mouse[0] > 700:
      running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False  

                