#! /usr/bin/python

import serial
import pygame,sys
from pygame.locals import *


import launcher
import rock
import target

from color import *

#Set up Window
pygame.init()
surf = pygame.display.set_mode((400,400),0,32)

#set up colors
BLUE = (0,0,255)
GREEN = (0,255,0)

#Set up launcher
my_launcher = launcher.Launcher(0,400)
my_rock = rock.Rock(0,400)
my_target = target.Target(200, 380)

#Set up FPS
FPS = 30
fpsClock = pygame.time.Clock()

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
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        my_launcher.changeAngle(3)
      if event.key == pygame.K_DOWN:
        my_launcher.changeAngle(-3)
      if event.key == pygame.K_LEFT:
        my_launcher.changeMagnitude(-5)
      if event.key == pygame.K_RIGHT:
        my_launcher.changeMagnitude(10)
      if event.key == pygame.K_SPACE and (not my_rock.isMoving()):
        my_launcher.fire(my_rock)
  
  # 2. Do game logic
  my_rock.move(1.0/FPS)
 
  # 3. draw Everything
  my_launcher.draw(surf)
  my_target.draw(surf)
  my_rock.draw(surf)
  pygame.display.update()
  fpsClock.tick(FPS)
