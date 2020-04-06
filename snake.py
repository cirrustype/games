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
  def __init__(self, color, pos):
    pass

  def move(self):
    pass
  
  def reset(self, pos):
    pass

  def addCube(self):
    pass

  def draw(self, surface):
    pass

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
  global rows, width
  surface.fill((0,0,0)) #fills background, (0,0,0) = black
  drawGrid(width, rows, surface) #draws grid lines, will define in another function
  pygame.display.update() #updates the surface


#the little cube to be eaten
def randomSnack(rows, items):
  pass

def massage_box(subject, content):
  pass


#main game loop
def main():
  global width, rows #global??? hieght?
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

