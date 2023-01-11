import pygame
from pygame.locals import *

import pygame_functions

import sys

import random

pygame.init()
resolution = (700,500)

def apple():
    appleSurf = pygame.Surface((50,50))
    appleSurf.fill((255,255,255))
    
    posX = random.randint(1,14)
    posY = random.randint(1,10)
    posX = (posX) * 25 * 2 - 25
    posY = (posY) * 25 * 2 - 25
    
    return posX, posY


screen = pygame.display.set_mode(resolution)

background = pygame.image.load("background.png")

playerSurf = pygame.image.load("player.png")
playerRect = playerSurf.get_rect(center = (100,100))
segmentSurf = pygame.Surface((50,50))
segmentSurf.fill((255,255,255))


clock = pygame.time.Clock()
x = 75
y = 75

_count = 0

xDest = x
yDest = y

segments = 5

coords = []
destCoords = []

pastPos = (25,25)

segX = 75
segY = 75

applePos = apple()

appleSurf = segmentSurf


appleRect = appleSurf.get_rect(center = applePos)

while True:
    clock.tick(30)
    
    # if playerRect.colliderect
    
    keys = pygame.key.get_pressed()
    
    # if appleRect.colliderect    

    if playerRect.center in coords:
        pygame.quit()
        sys.exit()
    
    if playerRect.center == appleRect.center:
        applePos = apple()
        segments += 1
        appleRect = appleSurf.get_rect(center = applePos)
    
    if yDest == y and xDest == x:
        if keys[K_LSHIFT]:
            speed = 10
        else:
            speed = 5
        if keys[K_w] or keys[K_UP]:
            pastPos = (x,y)
            yDest = y - 50
            if not (resolution[1] < yDest or yDest < 0):
                coords.append(pastPos)
                destCoords.append((xDest,yDest))
                
        
        elif keys[K_s] or keys[K_DOWN]:
            pastPos = (x,y)
            yDest = y + 50
            if not (resolution[1] < yDest or yDest < 0):
                coords.append(pastPos)
                destCoords.append((xDest,yDest))

        elif keys[K_a] or keys[K_LEFT]:
            pastPos = (x,y)
            xDest = x - 50
            if not (resolution[0] < xDest or xDest < 0):
                coords.append(pastPos)
                destCoords.append((xDest,yDest))
        elif keys[K_d] or keys[K_RIGHT]:
            pastPos = (x,y)
            xDest = x + 50
            if not (resolution[0] < xDest or xDest < 0):
                coords.append(pastPos)
                destCoords.append((xDest,yDest))
    
    if  resolution[1] < yDest or yDest < 0:
        yDest = y
    elif resolution[0] < xDest or xDest < 0:
        xDest = x
        
    if xDest != x:
        x += speed * ((xDest-x)/abs(xDest-x))
    
    if yDest != y:
        y += speed * ((yDest-y)/abs(yDest-y))
    
    
    
    playerRect = playerSurf.get_rect(center = (x,y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(background, (0,0))

    _count = 0
    for i in coords:
        if xDest == x and yDest == y:
            segX = coords[0][0]
            segY = coords[0][1]
        _count += 1
        screen.blit(segmentSurf, segmentSurf.get_rect(center = i))
    

    if len(coords) > segments:
        coords.pop(0)
    if len(destCoords) > segments:
        destCoords.pop(0)

    screen.blit(appleSurf, appleRect)

    screen.blit(playerSurf,playerRect)
    # screen.blit(playerSurf, playerRect)    
    pygame.display.update()        
    
    
