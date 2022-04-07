from grid import Grid

class Particle():
  grid: Grid
  color: tuple = (255,255,255)

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.grid.set(x, y, self)

  def step(self):
    pass

class Sand(Particle):
  color: tuple = (255, 242, 122)

  def step(self):
    if self.grid.in_range(self.x, self.y+1):
      if not self.grid.get(self.x, self.y+1):
        self.grid.swap(self.x, self.y, self.x, self.y+1)
        return
    if self.grid.in_range(self.x+1, self.y+1):
      if not self.grid.get(self.x+1, self.y+1):
        self.grid.swap(self.x, self.y, self.x+1, self.y+1)
        return
    if self.grid.in_range(self.x-1, self.y+1):
      if not self.grid.get(self.x-1, self.y+1):
        self.grid.swap(self.x, self.y, self.x-1, self.y+1)

class Water(Particle):
  color: tuple = (84, 133, 255)

  def step(self):
    if self.grid.in_range(self.x, self.y+1):
      below = self.grid.get(self.x, self.y+1)
      if not below and type(below) != Sand:
        self.grid.swap(self.x, self.y, self.x, self.y+1)
        return
    if self.grid.in_range(self.x+1, self.y):
      if not self.grid.get(self.x+1, self.y):
        self.grid.swap(self.x, self.y, self.x+1, self.y)
        return
    if self.grid.in_range(self.x-1, self.y):
      if not self.grid.get(self.x-1, self.y):
        self.grid.swap(self.x, self.y, self.x-1, self.y)