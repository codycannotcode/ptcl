from grid import Grid
from random import random

class Particle():
  grid: Grid
  color = (255,255,255)

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.grid.set(x, y, self)

  def step(self):
    pass

class Sand(Particle):
  color: tuple = (255, 242, 122)

  def step(self):
    replace = random() < 0.5
    if self.grid.in_range(self.x, self.y+1):
      down = self.grid.get(self.x, self.y+1)
      if not down or isinstance(down, Water):
        if replace and down:
          self.grid.set(self.x, self.y+1, None)
        self.grid.swap(self.x, self.y, self.x, self.y+1)
        return
    if self.grid.in_range(self.x+1, self.y+1):
      down_right = self.grid.get(self.x+1, self.y+1)
      if not down_right or isinstance(down_right, Water):
        if replace and down_right:
          self.grid.set(self.x+1, self.y+1, None)
        self.grid.swap(self.x, self.y, self.x+1, self.y+1)
        return
    if self.grid.in_range(self.x-1, self.y+1):
      down_left = self.grid.get(self.x-1, self.y+1)
      if not down_left or isinstance(down_left, Water):
        if replace and down_left:
          self.grid.set(self.x-1, self.y+1, None)
        self.grid.swap(self.x, self.y, self.x-1, self.y+1)

class Water(Particle):
  color: tuple = (84, 133, 255)

  def step(self):
    if self.grid.in_range(self.x, self.y+1):
      below = self.grid.get(self.x, self.y+1)
      if not below and type(below) != Sand:
        self.grid.swap(self.x, self.y, self.x, self.y+1)
        return
    if random() < 0.5:
      if not self.__try_left():
        self.__try_right()
    else:
      if not self.__try_right():
        self.__try_left()
  
  def __try_right(self):
    if self.grid.in_range(self.x+1, self.y):
      right = self.grid.get(self.x+1, self.y)
      if not right:
        self.grid.swap(self.x, self.y, self.x+1, self.y)
        return True
      return False
  
  def __try_left(self):
    if self.grid.in_range(self.x-1, self.y):
      left = self.grid.get(self.x-1, self.y)
      if not left:
        self.grid.swap(self.x, self.y, self.x-1, self.y)
        return True
    return False