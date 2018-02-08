import pygame, sys

from color import *

class Target:
  def __init__(self, x, y):
    self.rect = pygame.Rect(0,y,40,10)
    self.rect.centerx = x

  def draw(self,surf):
    pygame.draw.rect(surf, BLACK, self.rect)

  def hitBy(self, obj):
    return self.rect.colliderect(obj.getRect())
