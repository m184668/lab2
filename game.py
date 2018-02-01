#! /usr/bin/python

import serial
import pygame,sys
from pygame.locals import *

#Set up Window
pygame.init()
surf = pygame.display.set_mode((400,400),0,32)

#set up colors
BLUE = (0,0,255)
GREEN = (0,255,0)

#Drawing world 
def draw_world(surf):
  surf.fill(BLUE)
  fontObj = pygame.font.Font('freesansbold.ttf',32)
  textSurfaceObj = fontObj.render('Launchr 1.0',True, GREEN,BLUE) 
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (200,15)
  surf.blit(textSurfaceObj,textRectObj)
  pygame.draw.rect(surf,GREEN,(0,380,500,400))
  pygame.display.update()



while(True):
  draw_world(surf)
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
