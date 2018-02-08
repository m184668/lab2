import pygame, sys, math

Max_Mag = 100
Min_Mag = 10
Max_Ang = 90
Min_Ang = 1

RED=(255,0,0)

class Launcher:
  def __init__(self, x, y): #constructor
    self.x = x
    self.y = y
    self.mag = 20
    self.ang = 45

  def changeMagnitude(self,delta):
    self.mag = self.mag + delta
    if(self.mag > Max_Mag):
      self.mag = Max_Mag
    if(self.mag < Min_Mag):
      self.mag = Min_Mag
  
  def changeAngle(self,delta):
    self.ang = self.ang + delta
    if(self.ang > Max_Ang):
      self.ang = Max_Ang
    if(self.ang <= Min_Ang):
      self.ang = Min_Ang

  def fire(self, rock):
    rock.v_x= self.mag*math.cos(math.radians(self.ang))
    rock.v_y= -1*self.mag*math.sin(math.radians(self.ang))

  def draw(self,surf):
    ex=self.x+self.mag*math.cos(math.radians(self.ang))
    ey=self.y-self.mag*math.sin(math.radians(self.ang))
    pygame.draw.line(surf, RED, (self.x, self.y), (ex,ey), 6)


#pygame.display.update() #I do not know if we want this here or somewhere else
