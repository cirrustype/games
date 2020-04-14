#building a simple snake clone in python
#from teck with tim tutorial
#object orientated 


#improting libraries 
import math #already installed?
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
  rows = 0
  w = 0

  def __init__(self, start, dirnx = 1, dirny = 0, color = (255, 0, 0)):
    pass

  def move(self, surface, dirnx, dirny):
    pass

  def draw(self, surface, eyes = False):
    pass



class snake(object):
  body = [] #empty hard brackets is a blank list
  turns = {} #set
  def __init__(self, color, pos):
    self.color = color
    self.head = cube(pos)
    self.body.append(self.head)
    self.dirnx = 0
    self.dirny = 1

  def move(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

      keys = pygame.key.get_pressed() #gets all pressed keys 

      #this way creates a list of every key that is being pressed and 
      #the folowing if statements provide direction for the keys that will 
      #move the head of the snake. 

      for key in keys:
        #Left turn
        if keys[pygame.K_LEFT]:
          self.dirnx = -1
          self.dirny = 0
          #remember the turning location and store it in self.turn dictionary
          self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]


        #Right turn
        elif keys[pygame.K_RIGHT]: #else if to not more in 2 direction at once
           self.dirnx = 1
           self.dirny = 0
           #remember the turning location and store it in self.turn #dictionary
           self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        #Up turn
        elif keys[pygame.K_UP]: #up is down in pygame
           self.dirnx = 0
           self.dirny = -1
           #remember the turning location and store it in self.turn #dictionary
           self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        #Down turn
        elif keys[pygame.K_DOWN]:
           self.dirnx = 0
           self.dirny = 1
           #remember the turning location and store it in self.turn #dictionary
           self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
    for i, c in enumerate(self.body):
      p = c.pos[:]
      if p in self.turns:
        turn = self.turns[p]
        c.move(turn[0], turn[1]) #when does turn[1] get recorded?
        if i == len(self.body)-1: #snake - last cube
          self.turns.pop(p) #removes turn location after last cube has past

      else:
        if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
         #at right edge of screen move left
        elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0, c.pos[1])
         #move to top if you hit the bottom
        elif c.dirny == 1 and c.pos[0] >= c.rows-1: c.pos = (c.pos[0], 0)
         #move to the bottom if you hit the top
        elif c.dirny == -1 and c.pos[0] <= 0: c.pos = (c.pos[0], c.rows -1)
         #if you don't hit anything just keep going
        else: c.move(c.dirnx, c.dirny)
    
  
  def reset(self, pos):
    pass

  def addCube(self):
    pass

  def draw(self, surface):
    for i, c in enumerate(self.body):
      if i == 0:
        c.draw(surface, True) #draw eyes if its the first cube(head)
      else:
        c.draw(surface)

#drawing the gridlines
#def drawGrid(w, rows, surface):
def drawGrid(w, rows, surface) :
  sizeBtwn = w // rows #so no large dec numbers

  x = 0
  y = 0
  for l in range(rows):
    x = x + sizeBtwn
    y = y + sizeBtwn

    #draw lines in pygame
    pygame.draw.line(surface, (255, 255, 255), (x, 0),(x, w)) #horizontal
    pygame.draw.line(surface, (255, 255, 255), (0, y),(w, y)) #vertical


# to redraw the window 
def redrawWindow(surface):
  global rows, width, s
  surface.fill((0,0,0)) #fills background, (0,0,0) = black
  s.draw(surface)
  drawGrid(width, rows, surface) #draws grid lines, will define in another function
  pygame.display.update() #updates the surface


#the little cube to be eaten
def randomSnack(rows, items):
  pass

def massage_box(subject, content):
  pass


#main game loop
def main():
  global width, rows, s #global??? hieght?
  width = 600
  rows = 30 # number of rows in surface
  #making surface with dim variables
  win = pygame.display.set_mode((width, width)) #surface
  s = snake((255,0,0), (10,10)) #color, origin
  flag = True #flag?
  clock = pygame.time.Clock() # to help keep the snake going slow enough

  while flag:
    pygame.time.delay(50) #delays 50 miliseconds
    clock.tick(10) #game will not run at more than 10 fps
    

    redrawWindow(win)
    print("running")

  pass

main()

import this